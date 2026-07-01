# AI2008 - Group 7: AI-Driven Dynamic Pricing in Freight & Shipping Logistics
## Phân Tích & Định Giá Động Bằng Trí Tuệ Nhân Tạo Trong Logistics

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine--Learning-F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data--Analysis-150458.svg?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

---

## 📌 Giới thiệu dự án

Dự án tập trung vào việc nghiên cứu và ứng dụng các phương pháp phân tích dữ liệu, truy vấn SQL nâng cao và thuật toán học máy (Machine Learning) để giải quyết bài toán **Định giá động (Dynamic Pricing)** trong ngành Logistics và vận tải hàng hóa (Freight & Shipping). 

Thông qua việc khai thác tập dữ liệu vận hành thực tế, dự án hướng tới mục tiêu tối ưu hóa doanh thu cho đơn vị vận chuyển, đồng thời cân bằng giữa cung (tài xế sẵn có) và cầu (yêu cầu đặt xe của khách hàng) tại các thời điểm và khu vực khác nhau.

---

## 💻 Hướng dẫn chạy dự án

### Yêu cầu hệ thống
*   Python 3.8 trở lên.
*   Trình quản lý gói `pip`.

### Các bước cài đặt

1.  **Clone thư mục dự án hoặc tải mã nguồn về máy tính.**

2.  **Tạo môi trường ảo Python (Nên sử dụng để tránh làm nhiễu môi trường Python gốc trên máy):**
    ```bash
    # Trên macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # Trên Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn notebook scipy sqlite3
    ```

4.  **Khởi động Jupyter Notebook:**
    *Mở file `Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb` trong Jupyter Notebook (hoặc bất kỳ nền tảng nào hỗ trợ chạy .ipynb) và chạy tuần tự các cell.*

---

## ❓ Câu hỏi nghiên cứu (Research Questions)

Dự án được xây dựng xoay quanh **3 câu hỏi nghiên cứu cốt lõi**:

**RQ1:** *Yếu tố thị trường nào ảnh hưởng đến giá cước vận chuyển? - Which market factors affect transport price?*

**RQ2:** *Mô hình AI nào dự báo và tối ưu giá cước động? - Which AI model can guess and improve the price in real time?*

**RQ3:** *Dynamic pricing giúp tăng doanh thu freight bao nhiêu % so với giá cố định? - How much can dynamic pricing increase freight revenue over fixed price?*

---

## 📂 Cấu trúc thư mục dự án

```text
├── Group_7_AI_Driven......ipynb     # Jupyter Notebook chính chứa toàn bộ mã nguồn
├── dynamic_pricing.csv              # Tập dữ liệu gốc (Dataset)
├── freight_pricing_research.db      # Cơ sở dữ liệu SQLite sau khi xử lý dữ liệu sạch
├── charts_img/                      # Thư mục lưu trữ các biểu đồ được xuất ra
└── README.md                        # Hướng dẫn dự án
```

---

## 📊 Mô tả Tập dữ liệu (Dataset Metadata)

Dataset `dynamic_pricing.csv` mô phỏng thông tin vận hành của **1,000 chuyến đi**, bao gồm các thuộc tính sau:

| Tên cột | Kiểu dữ liệu | Mô tả ý nghĩa |
| :--- | :--- | :--- |
| `Number_of_Riders` | Integer | Số lượng khách hàng có nhu cầu đặt chuyến đi tại thời điểm đó (Cầu) |
| `Number_of_Drivers` | Integer | Số lượng tài xế đang hoạt động và sẵn có (Cung) |
| `Location_Category` | Categorical | Phân loại địa điểm chuyến đi (`Urban` - Thành thị, `Suburban` - Ngoại ô, `Rural` - Nông thôn) |
| `Customer_Loyalty_Status` | Categorical | Hạng thân thiết của khách hàng (`Gold`, `Silver`, `Regular`) |
| `Number_of_Past_Rides` | Integer | Số chuyến đi khách hàng đã thực hiện trong quá khứ |
| `Average_Ratings` | Float | Điểm đánh giá trung bình của tài xế/khách hàng |
| `Time_of_Booking` | Categorical | Khung thời gian đặt chuyến (`Morning`, `Afternoon`, `Evening`, `Night`) |
| `Vehicle_Type` | Categorical | Phân khúc xe vận chuyển (`Premium` - Cao cấp, `Economy` - Tiết kiệm) |
| `Expected_Ride_Duration` | Integer | Thời gian di chuyển dự kiến của chuyến đi (tính theo phút) |
| `Historical_Cost_of_Ride` | Float | Chi phí thực tế (giá cước lịch sử) của chuyến đi (tính theo USD) |

---

## 👥 Thành viên thực hiện (Nhóm 7)
*   **Môn học:** ADY201m
*   **Lớp:** AI2008
*   **Đề tài:** AI-Driven Dynamic Pricing in Freight & Shipping Logistics
*   **Thành viên:** Nguyễn Phạm Minh Triết, Nguyễn Mạnh Hoàng, Nguyễn Hoàng Duy Tiến, Nguyễn Bùi Anh Duy
