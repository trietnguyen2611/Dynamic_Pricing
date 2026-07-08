# ✦ AI2008 - Nhóm 7: Phân Tích & Định Giá Động Trong Freight & Shipping Logistics

<p align="center">
  <strong>Phân Tích & Định Giá Động Bằng Trí Tuệ Nhân Tạo Trong Logistics</strong>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8+-cc785c?style=flat-square&logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter-Notebook-181715?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/></a>
  <a href="https://sqlite.org/"><img src="https://img.shields.io/badge/SQLite-Database-cc785c?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite"/></a>
  <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/scikit--learn-Machine--Learning-181715?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/></a>
  <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Pandas-Data--Analysis-cc785c?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/></a>
</p>

---

## ✦ Giới thiệu dự án

Dự án tập trung vào việc nghiên cứu và ứng dụng các phương pháp phân tích dữ liệu, truy vấn SQL nâng cao và thuật toán học máy (Machine Learning) để giải quyết bài toán **Định giá động (Dynamic Pricing)** trong ngành Logistics và vận tải hàng hóa (Freight & Shipping).

Thông qua việc khai thác tập dữ liệu chuỗi cung ứng thực tế (DataCo Supply Chain Dataset), dự án phân tích các yếu tố thị trường, phương thức vận chuyển và hành vi khách hàng. Từ đó, hướng tới mục tiêu tối ưu hóa doanh số vận chuyển, cải thiện hiệu suất chuỗi cung ứng, và xây dựng các mô hình dự báo cũng như tối ưu hóa giá cước động nhằm gia tăng lợi thế cạnh tranh cho doanh nghiệp logistics.

---

## ✦ Câu hỏi nghiên cứu (Research Questions)

Dự án được xây dựng xoay quanh 3 câu hỏi nghiên cứu cốt lõi:

> [!TIP]
> ### ✦ RQ1: Market Factors (Yếu tố thị trường)
> - **Yếu tố thị trường nào ảnh hưởng đến giá cước vận chuyển?**
> - *Which market factors affect transport price?*

> [!NOTE]
> ### ✦ RQ2: AI Modeling (Mô hình AI)
> - **Mô hình AI nào dự báo và tối ưu giá cước động?**
> - *Which AI model can predict and improve the price in real time?*

> [!IMPORTANT]
> ### ✦ RQ3: Revenue Impact (Hiệu quả doanh thu)
> - **Dynamic pricing giúp tăng doanh thu freight bao nhiêu % so với giá cố định?**
> - *How much can dynamic pricing increase freight revenue over fixed price?*

---

## ✦ Hướng dẫn chạy dự án

### Yêu cầu hệ thống
* Python 3.8 trở lên
* Trình quản lý gói `pip`

### Các bước cài đặt

1. **Clone thư mục dự án hoặc tải mã nguồn về máy tính.**
2. **Tạo môi trường ảo Python (khuyên dùng):**
   ```bash
   # Trên macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate

   # Trên Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn notebook scipy sqlite3
   ```
4. **Khởi động Jupyter Notebook:**
   Mở file `Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb` trong Jupyter Notebook (hoặc bất kỳ nền tảng nào hỗ trợ chạy `.ipynb`) và chạy tuần tự các cell.

---

## ✦ Cấu trúc thư mục dự án

```text
.
├── Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb  # Jupyter Notebook
├── DataCoSupplyChainDataset.csv                                         # Tập dữ liệu chuỗi cung ứng gốc
├── freight_pricing_research.db                                          # Cơ sở dữ liệu SQLite sạch
├── train_test_split.py                                                  # Script chia tập train/test
├── charts_img/                                                          # Thư mục lưu trữ biểu đồ xuất ra
└── README.md                                                            # Hướng dẫn dự án
```

---

## ✦ Mô tả Tập dữ liệu (Dataset Metadata)

Tập dữ liệu `DataCoSupplyChainDataset.csv` chứa thông tin vận hành của **180,519 giao dịch/đơn hàng**, bao gồm **53 thuộc tính** khác nhau. Dưới đây là các cột dữ liệu chính được sử dụng:

| Tên cột | Kiểu dữ liệu | Mô tả ý nghĩa |
| :--- | :--- | :--- |
| **Type** | `Categorical` | Phương thức thanh toán (DEBIT, TRANSFER, CASH, PAYMENT) |
| **Days for shipping (real)** | `Integer` | Số ngày vận chuyển thực tế của đơn hàng |
| **Days for shipment (scheduled)** | `Integer` | Số ngày vận chuyển dự kiến theo lịch trình |
| **Benefit per order** | `Float` | Lợi nhuận thu được trên mỗi đơn hàng (USD) |
| **Sales** | `Float` | Doanh số/giá trị sản phẩm bán ra (đại diện cho doanh số vận chuyển hàng hóa - USD) |
| **Delivery Status** | `Categorical` | Trạng thái giao hàng (Late delivery, Advance shipping, Shipping on time, Shipping canceled) |
| **Late_delivery_risk** | `Integer` | Rủi ro giao hàng trễ (1: Có rủi ro giao hàng trễ, 0: Không) |
| **Category Name** | `Categorical` | Tên danh mục của sản phẩm được vận chuyển |
| **Customer Segment** | `Categorical` | Phân khúc khách hàng (Consumer, Corporate, Home Office) |
| **Market** | `Categorical` | Thị trường khu vực đích (Pacific Asia, USCA, Europe, LATAM, Africa) |
| **Order Item Quantity** | `Integer` | Số lượng sản phẩm của mặt hàng trong đơn hàng |
| **Order Item Product Price** | `Float` | Giá gốc của sản phẩm được đặt |
| **Order Profit Per Order** | `Float` | Lợi nhuận của đơn hàng (USD) |
| **Shipping Mode** | `Categorical` | Phương thức vận chuyển (Standard Class, Second Class, First Class, Same Day) |

---

## ✦ Thông tin dự án (Project Metadata)

<table width="100%">
  <tr>
    <td width="33%" valign="top">
      <strong>Thông tin môn học</strong><br>
      • Môn học: ADY201m<br>
      • Lớp học: AI2008
    </td>
    <td width="34%" valign="top">
      <strong>Đề tài nghiên cứu</strong><br>
      <em>AI-Driven Dynamic Pricing in Freight & Shipping Logistics</em>
    </td>
    <td width="33%" valign="top">
      <strong>Thành viên nhóm (Nhóm 7)</strong><br>
      • Nguyễn Phạm Minh Triết<br>
      • Nguyễn Mạnh Hoàng<br>
      • Nguyễn Hoàng Duy Tiến<br>
      • Nguyễn Bùi Anh Duy
    </td>
  </tr>
</table>
