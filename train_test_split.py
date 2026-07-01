# =============================================================================
# AI2008 - Group 7 - Train/Test Split
# Dự án: AI-Driven Dynamic Pricing in Freight & Shipping Logistics
# =============================================================================
# File này chứa toàn bộ code cho bước Train/Test Split (Section 6 trong notebook).
# Bạn có thể copy từng block vào notebook, hoặc chạy trực tiếp file .py này.
# =============================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# =============================================================================
# BƯỚC 1: ĐỌC DỮ LIỆU ĐÃ QUA FEATURE ENGINEERING
# =============================================================================
# Đọc file features.csv - file đã chứa đầy đủ 5 features mới:
#   Feature 1: Supply_Demand_Ratio  (tỷ lệ cung/cầu)
#   Feature 2: Is_Peak_Hour         (giờ cao điểm: Morning/Afternoon = 1)
#   Feature 3: Demand_Urgency       (nhu cầu khẩn cấp)
#   Feature 4: Customer_Segment     (phân khúc khách hàng: 0/1/2)
#   Feature 5: Cancellation_Risk_Index (rủi ro huỷ: High/Moderate/Low)

df = pd.read_csv("features.csv")
print(f"Tổng số mẫu trong dataset: {df.shape[0]} dòng x {df.shape[1]} cột")
print(f"Các cột hiện có: {list(df.columns)}\n")


# =============================================================================
# BƯỚC 2: XỬ LÝ CỘT CATEGORICAL TRƯỚC KHI CHIA TÁCH
# =============================================================================
# LÝ DO: Các mô hình ML (Linear Regression, XGBoost, Random Forest...) yêu cầu
# đầu vào là số (numeric). Các cột dạng văn bản (string/object) cần được mã hóa.
#
# Trong dataset hiện tại, có các cột categorical:
#   - Location_Category:        Urban / Suburban / Rural
#   - Customer_Loyalty_Status:  gold / silver / regular
#   - Time_of_Booking:          Morning / Afternoon / Evening / Night
#   - Vehicle_Type:             Premium / Economy
#   - Cancellation_Risk_Index:  High Risk / Moderate Risk / Low Risk
#
# PHƯƠNG PHÁP: Sử dụng pd.get_dummies() (One-Hot Encoding) với drop_first=True
# để tránh bẫy đa cộng tuyến (multicollinearity trap) - nghĩa là nếu có 3 loại
# khu vực (Urban, Suburban, Rural) thì chỉ cần 2 cột dummy là đủ biểu diễn.

# Liệt kê các cột categorical cần mã hóa
categorical_columns = df.select_dtypes(include=['object', 'string']).columns.tolist()
print(f"Các cột categorical cần mã hóa: {categorical_columns}")

# Thực hiện One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# Chuyển các cột bool (True/False) sang int (0/1) để đảm bảo toàn bộ là numeric
bool_cols = df_encoded.select_dtypes(include=['bool']).columns
df_encoded[bool_cols] = df_encoded[bool_cols].astype(int)

print(f"Shape sau khi mã hóa: {df_encoded.shape}")
print(f"Các cột sau mã hóa: {list(df_encoded.columns)}\n")


# =============================================================================
# BƯỚC 3: TÁCH BIẾN ĐẦU VÀO (X) VÀ BIẾN MỤC TIÊU (y)
# =============================================================================
# BIẾN MỤC TIÊU (y): Historical_Cost_of_Ride
#   - Đây là giá cước vận chuyển lịch sử - biến mà mô hình cần DỰ ĐOÁN.
#   - Trong bài toán Dynamic Pricing, mục tiêu là xây dựng mô hình có thể
#     dự báo giá cước dựa trên các yếu tố thị trường thời gian thực.
#
# BIẾN ĐẦU VÀO (X): Tất cả các cột còn lại
#   - Bao gồm cả features gốc lẫn 5 features mới đã tạo ở Section 5.
#   - Sau khi One-Hot Encoding, các cột text đã được chuyển thành số 0/1.

TARGET_COLUMN = "Historical_Cost_of_Ride"

X = df_encoded.drop(columns=[TARGET_COLUMN])
y = df_encoded[TARGET_COLUMN]

print(f"Biến mục tiêu (y): {TARGET_COLUMN}")
print(f"  - Giá trị min: {y.min():.2f} | max: {y.max():.2f} | trung bình: {y.mean():.2f}")
print(f"Số lượng features (X): {X.shape[1]} cột")
print(f"Danh sách features đầu vào:")
for i, col in enumerate(X.columns, 1):
    print(f"  {i:2d}. {col}")
print()


# =============================================================================
# BƯỚC 4: THỰC HIỆN TRAIN/TEST SPLIT
# =============================================================================
# ┌─────────────────────────────────────────────────────────────────────────┐
# │  LÝ DO CHỌN TỶ LỆ 80/20 (test_size=0.2)                             
# │                                                                        
# │  1. Dataset chỉ có 1000 mẫu - thuộc loại dataset NHỎ.                
# │     → Cần giữ lại càng nhiều dữ liệu Train càng tốt để mô hình      
# │       học được patterns đa dạng (800 mẫu train, 200 mẫu test).       
# │                                                                        
# │  2. Tỷ lệ 80/20 là "golden ratio" phổ biến nhất trong ML:           
# │     → Được khuyến nghị bởi Andrew Ng (Stanford) và scikit-learn docs. 
# │     → Đủ dữ liệu test (200 mẫu) để đánh giá tin cậy về performance. 
# │                                                                       
# │  3. So sánh với 70/30:                                            
# │     → 70/30 chỉ giữ 700 mẫu train - ít hơn 100 mẫu so với 80/20.   
# │     → Với dataset nhỏ (1000 mẫu), mỗi mẫu đều quý giá cho training.
# │     → 300 mẫu test thường chỉ cần thiết khi dataset lớn (>10,000).  
# │                                                                        
# │  4. random_state=42:                                                   
# │     → Cố định seed để mọi lần chạy đều cho kết quả giống nhau.  
# │     → Đảm bảo tính tái lập (reproducibility) khi báo cáo kết quả. 
# │     → Số 42 là convention phổ biến (từ "The Hitchhiker's Guide"). 
# └─────────────────────────────────────────────────────────────────────────┘

# --- Tỷ lệ 80/20 ---
TEST_SIZE = 0.2   # 20% cho test
RANDOM_STATE = 42  # Seed cố định

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE
)

print("=" * 65)
print("  KẾT QUẢ TRAIN/TEST SPLIT (80/20)")
print("=" * 65)
print(f"  Tổng số mẫu ban đầu: {len(df):>6d}")
print(f"  Tập Train (80%):    {X_train.shape[0]:>6d} mẫu x {X_train.shape[1]} features")
print(f"  Tập Test (20%):     {X_test.shape[0]:>6d} mẫu x {X_test.shape[1]} features")
print(f"  random_state:          {RANDOM_STATE}")
print("=" * 65)
print()


# =============================================================================
# BƯỚC 5: KIỂM TRA PHÂN PHỐI SAU KHI CHIA TÁCH
# =============================================================================
# LÝ DO: Cần đảm bảo phân phối giá cước trong tập Train và Test là tương đồng.
# Nếu phân phối lệch quá nhiều → mô hình sẽ học sai và đánh giá không chính xác.

print("KIỂM TRA PHÂN PHỐI BIẾN MỤC TIÊU (Historical_Cost_of_Ride):")
print("-" * 55)
print(f"  {'Thống kê':<20s} {'Toàn bộ':>10s} {'Train':>10s} {'Test':>10s}")
print("-" * 55)
print(f"  {'Số mẫu':<20s} {len(y):>10d} {len(y_train):>10d} {len(y_test):>10d}")
print(f"  {'Trung bình (Mean)':<20s} {y.mean():>10.2f} {y_train.mean():>10.2f} {y_test.mean():>10.2f}")
print(f"  {'Trung vị (Median)':<20s} {y.median():>10.2f} {y_train.median():>10.2f} {y_test.median():>10.2f}")
print(f"  {'Độ lệch chuẩn (Std)':<20s} {y.std():>10.2f} {y_train.std():>10.2f} {y_test.std():>10.2f}")
print(f"  {'Min':<20s} {y.min():>10.2f} {y_train.min():>10.2f} {y_test.min():>10.2f}")
print(f"  {'Max':<20s} {y.max():>10.2f} {y_train.max():>10.2f} {y_test.max():>10.2f}")
print("-" * 55)
print()

# Kiểm tra chênh lệch Mean giữa Train và Test
mean_diff = abs(y_train.mean() - y_test.mean())
mean_diff_pct = mean_diff / y.mean() * 100
print(f"  → Chênh lệch Mean giữa Train và Test: {mean_diff:.2f} ({mean_diff_pct:.2f}%)")
if mean_diff_pct < 5:
    print("  ✅ Phân phối TƯƠNG ĐỒNG - Dữ liệu được chia tách tốt!")
else:
    print("  ⚠️  Phân phối có chênh lệch - Cân nhắc dùng stratified split.")
print()


# =============================================================================
# BƯỚC 6: XÁC NHẬN DỮ LIỆU SẴN SÀNG CHO MODEL TRAINING
# =============================================================================
print("TRẠNG THÁI SẴN SÀNG CHO MODEL TRAINING:")
print("-" * 55)

# Kiểm tra NaN
nan_in_X_train = X_train.isnull().sum().sum()
nan_in_X_test = X_test.isnull().sum().sum()
nan_in_y = y_train.isnull().sum() + y_test.isnull().sum()

print(f"  Giá trị NaN trong X_train : {nan_in_X_train}")
print(f"  Giá trị NaN trong X_test  : {nan_in_X_test}")
print(f"  Giá trị NaN trong y       : {nan_in_y}")

# Kiểm tra data types
non_numeric = X_train.select_dtypes(exclude=['number']).columns.tolist()
if len(non_numeric) == 0:
    print(f"  Kiểu dữ liệu X           : ✅ Tất cả numeric")
else:
    print(f"  Kiểu dữ liệu X           : ⚠️  Còn cột non-numeric: {non_numeric}")

# Kiểm tra data leakage
print(f"  Data leakage check        : ✅ Target '{TARGET_COLUMN}' đã được loại khỏi X")
print("-" * 55)
print()

# Tóm tắt cuối cùng
print("╔═══════════════════════════════════════════════════════════════╗")
print("║          CÁC BIẾN ĐÃ SẴN SÀNG ĐỂ TRAINING:")
print("║                                                               ")
print(f"║   X_train : ({X_train.shape[0]}, {X_train.shape[1]})  - Features tập huấn luyện ")
print(f"║   X_test  : ({X_test.shape[0]}, {X_test.shape[1]})  - Features tập kiểm tra")
print(f"║   y_train : ({len(y_train)},)     - Giá cước tập huấn luyện")
print(f"║   y_test  : ({len(y_test)},)     - Giá cước tập kiểm tra ")
print("║                                                               ")
print("║   → Tiếp tục sang Section 7: Training Model Machine Learning ")
print("╚═══════════════════════════════════════════════════════════════╝")


# =============================================================================
# HƯỚNG DẪN ĐƯA VÀO NOTEBOOK
# =============================================================================
# Khi copy vào notebook, bạn có thể chia thành các cell như sau:
#
# CELL 1 (Markdown):
#   ## 6. Train / Test Split
#   **Mục tiêu:** Chia dữ liệu thành 2 tập:
#   - **Train (80%)**: Dùng để huấn luyện mô hình AI.
#   - **Test (20%)**: Dùng để đánh giá hiệu suất mô hình trên dữ liệu chưa thấy.
#
#   **Lý do chọn 80/20:**
#   - Dataset chỉ có 1000 mẫu → cần tối đa hóa dữ liệu training.
#   - 200 mẫu test đủ để đánh giá đáng tin cậy.
#   - `random_state=42` đảm bảo kết quả tái lập được.
#
# CELL 2 (Code): Copy BƯỚC 2 + BƯỚC 3 + BƯỚC 4
# CELL 3 (Code): Copy BƯỚC 5 (kiểm tra phân phối)
# CELL 4 (Code): Copy BƯỚC 6 (xác nhận sẵn sàng)
