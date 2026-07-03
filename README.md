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

Thông qua việc khai thác tập dữ liệu chuỗi cung ứng thực tế (DataCo Supply Chain Dataset), dự án phân tích các yếu tố thị trường, phương thức vận chuyển và hành vi khách hàng. Từ đó, hướng tới mục tiêu tối ưu hóa doanh số vận chuyển, cải thiện hiệu suất chuỗi cung ứng, và xây dựng các mô hình dự báo cũng như tối ưu hóa giá cước động nhằm gia tăng lợi thế cạnh tranh cho doanh nghiệp logistics.

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

**RQ2:** *Mô hình AI nào dự báo và tối ưu giá cước động? - Which AI model can predict and improve the price in real time?*

**RQ3:** *Dynamic pricing giúp tăng doanh thu freight bao nhiêu % so với giá cố định? - How much can dynamic pricing increase freight revenue over fixed price?*

---

## 📂 Cấu trúc thư mục dự án

```text
├── Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb     # Jupyter Notebook chính chứa toàn bộ mã nguồn
├── DataCoSupplyChainDataset.csv                                                # Tập dữ liệu chuỗi cung ứng gốc (Dataset mới)
├── freight_pricing_research.db                                                 # Cơ sở dữ liệu SQLite sau khi xử lý dữ liệu sạch
├── train_test_split.py                                                         # File script chia tập dữ liệu huấn luyện và kiểm tra
├── charts_img/                                                                 # Thư mục lưu trữ các biểu đồ được xuất ra
└── README.md                                                                   # Hướng dẫn dự án
```

---

## 📊 Mô tả Tập dữ liệu (Dataset Metadata)

Dataset `DataCoSupplyChainDataset.csv` chứa thông tin vận hành của **180,519 giao dịch/đơn hàng**, bao gồm **53 thuộc tính** khác nhau phục vụ phân tích chuỗi cung ứng và định giá. Dưới đây là các cột dữ liệu chính được sử dụng trong dự án:

| Tên cột | Kiểu dữ liệu | Mô tả ý nghĩa |
| :--- | :--- | :--- |
| `Type` | Categorical | Phương thức thanh toán (DEBIT, TRANSFER, CASH, PAYMENT) |
| `Days for shipping (real)` | Integer | Số ngày vận chuyển thực tế của đơn hàng |
| `Days for shipment (scheduled)` | Integer | Số ngày vận chuyển dự kiến theo lịch trình |
| `Benefit per order` | Float | Lợi nhuận thu được trên mỗi đơn hàng (USD) |
| `Sales` | Float | Doanh số/giá trị sản phẩm bán ra (đại diện cho doanh số vận chuyển hàng hóa - USD) |
| `Delivery Status` | Categorical | Trạng thái giao hàng (Late delivery, Advance shipping, Shipping on time, Shipping canceled) |
| `Late_delivery_risk` | Integer | Rủi ro giao hàng trễ (1: Có rủi ro giao hàng trễ, 0: Không) |
| `Category Name` | Categorical | Tên danh mục của sản phẩm được vận chuyển |
| `Customer Segment` | Categorical | Phân khúc khách hàng (Consumer, Corporate, Home Office) |
| `Market` | Categorical | Thị trường khu vực đích (Pacific Asia, USCA, Europe, LATAM, Africa) |
| `Order Item Quantity` | Integer | Số lượng sản phẩm của mặt hàng trong đơn hàng |
| `Order Item Product Price` | Float | Giá gốc của sản phẩm được đặt |
| `Order Profit Per Order` | Float | Lợi nhuận của đơn hàng (USD) |
| `Shipping Mode` | Categorical | Phương thức vận chuyển (Standard Class, Second Class, First Class, Same Day) |

---

## 👥 Thành viên thực hiện (Nhóm 7)
*   **Môn học:** ADY201m
*   **Lớp:** AI2008
*   **Đề tài:** AI-Driven Dynamic Pricing in Freight & Shipping Logistics
*   **Thành viên:** Nguyễn Phạm Minh Triết, Nguyễn Mạnh Hoàng, Nguyễn Hoàng Duy Tiến, Nguyễn Bùi Anh Duy
