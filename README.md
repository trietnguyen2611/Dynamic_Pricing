<div style="background-color: #faf9f5; color: #141413; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 40px; border-radius: 16px; border: 1px solid #e6dfd8; max-width: 960px; margin: 20px auto; box-shadow: 0 4px 24px rgba(20,20,19,0.04);">

<div align="center" style="margin-bottom: 40px; border-bottom: 1px solid #e6dfd8; padding-bottom: 32px;">
  <span style="font-size: 24px; color: #cc785c; display: block; margin-bottom: 8px;">✦</span>
  <h1 style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-weight: 400; font-size: 32px; color: #141413; margin: 0 0 12px 0; letter-spacing: -0.5px; line-height: 1.2;">
    AI2008 - Group 7: AI-Driven Dynamic Pricing in Freight & Shipping Logistics
  </h1>
  <p style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-size: 20px; color: #6c6a64; margin: 0 0 24px 0; font-style: italic;">
    Phân Tích & Định Giá Động Bằng Trí Tuệ Nhân Tạo Trong Logistics
  </p>
  
  <div style="display: flex; justify-content: center; gap: 8px; flex-wrap: wrap;">
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8+-cc785c?style=flat-square&logo=python&logoColor=white" alt="Python"/></a>
    <a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter-Notebook-181715?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/></a>
    <a href="https://sqlite.org/"><img src="https://img.shields.io/badge/SQLite-Database-cc785c?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite"/></a>
    <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/scikit--learn-Machine--Learning-181715?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/></a>
    <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Pandas-Data--Analysis-cc785c?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/></a>
  </div>
</div>

<div style="margin-bottom: 48px;">
  <h2 style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-weight: 400; font-size: 24px; color: #141413; border-bottom: 1px solid #e6dfd8; padding-bottom: 8px; margin-top: 0; margin-bottom: 16px;">
    ✦ Giới thiệu dự án
  </h2>
  <p style="font-size: 16px; color: #3d3d3a; line-height: 1.6; margin-bottom: 16px; text-align: justify;">
    Dự án tập trung vào việc nghiên cứu và ứng dụng các phương pháp phân tích dữ liệu, truy vấn SQL nâng cao và thuật toán học máy (Machine Learning) để giải quyết bài toán <strong>Định giá động (Dynamic Pricing)</strong> trong ngành Logistics và vận tải hàng hóa (Freight & Shipping).
  </p>
  <p style="font-size: 16px; color: #3d3d3a; line-height: 1.6; text-align: justify; margin-top: 0;">
    Thông qua việc khai thác tập dữ liệu chuỗi cung ứng thực tế (DataCo Supply Chain Dataset), dự án phân tích các yếu tố thị trường, phương thức vận chuyển và hành vi khách hàng. Từ đó, hướng tới mục tiêu tối ưu hóa doanh số vận chuyển, cải thiện hiệu suất chuỗi cung ứng, và xây dựng các mô hình dự báo cũng như tối ưu hóa giá cước động nhằm gia tăng lợi thế cạnh tranh cho doanh nghiệp logistics.
  </p>
</div>

<div style="margin-bottom: 48px;">
  <h2 style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-weight: 400; font-size: 24px; color: #141413; border-bottom: 1px solid #e6dfd8; padding-bottom: 8px; margin-bottom: 20px;">
    ✦ Câu hỏi nghiên cứu (Research Questions)
  </h2>
  <p style="font-size: 15px; color: #6c6a64; margin-bottom: 20px;">Dự án được xây dựng xoay quanh 3 câu hỏi nghiên cứu cốt lõi:</p>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 24px;">
    <!-- RQ1 Card -->
    <div style="background-color: #efe9de; border-radius: 12px; padding: 24px; border: 1px solid #e6dfd8; display: flex; flex-direction: column; justify-content: space-between;">
      <div>
        <span style="background-color: #cc785c; color: #ffffff; font-family: sans-serif; font-size: 11px; font-weight: 600; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; letter-spacing: 1px;">RQ1</span>
        <h4 style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-size: 18px; color: #141413; margin: 16px 0 8px 0; font-weight: 500;">Market Factors</h4>
        <p style="font-size: 14px; color: #252523; line-height: 1.5; margin: 0;">Yếu tố thị trường nào ảnh hưởng đến giá cước vận chuyển?</p>
      </div>
      <div style="margin-top: 12px; border-top: 1px solid #e6dfd8; padding-top: 8px;">
        <span style="font-size: 13px; color: #6c6a64; font-style: italic; display: block; line-height: 1.4;">Which market factors affect transport price?</span>
      </div>
    </div>
    
    <!-- RQ2 Card -->
    <div style="background-color: #efe9de; border-radius: 12px; padding: 24px; border: 1px solid #e6dfd8; display: flex; flex-direction: column; justify-content: space-between;">
      <div>
        <span style="background-color: #cc785c; color: #ffffff; font-family: sans-serif; font-size: 11px; font-weight: 600; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; letter-spacing: 1px;">RQ2</span>
        <h4 style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-size: 18px; color: #141413; margin: 16px 0 8px 0; font-weight: 500;">AI Modeling</h4>
        <p style="font-size: 14px; color: #252523; line-height: 1.5; margin: 0;">Mô hình AI nào dự báo và tối ưu giá cước động?</p>
      </div>
      <div style="margin-top: 12px; border-top: 1px solid #e6dfd8; padding-top: 8px;">
        <span style="font-size: 13px; color: #6c6a64; font-style: italic; display: block; line-height: 1.4;">Which AI model can predict and improve the price in real time?</span>
      </div>
    </div>
    
    <!-- RQ3 Card -->
    <div style="background-color: #efe9de; border-radius: 12px; padding: 24px; border: 1px solid #e6dfd8; display: flex; flex-direction: column; justify-content: space-between;">
      <div>
        <span style="background-color: #cc785c; color: #ffffff; font-family: sans-serif; font-size: 11px; font-weight: 600; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; letter-spacing: 1px;">RQ3</span>
        <h4 style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-size: 18px; color: #141413; margin: 16px 0 8px 0; font-weight: 500;">Revenue Impact</h4>
        <p style="font-size: 14px; color: #252523; line-height: 1.5; margin: 0;">Dynamic pricing giúp tăng doanh thu freight bao nhiêu % so với giá cố định?</p>
      </div>
      <div style="margin-top: 12px; border-top: 1px solid #e6dfd8; padding-top: 8px;">
        <span style="font-size: 13px; color: #6c6a64; font-style: italic; display: block; line-height: 1.4;">How much can dynamic pricing increase freight revenue over fixed price?</span>
      </div>
    </div>
  </div>
</div>

<div style="margin-bottom: 48px;">
  <h2 style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-weight: 400; font-size: 24px; color: #141413; border-bottom: 1px solid #e6dfd8; padding-bottom: 8px; margin-bottom: 20px;">
    ✦ Hướng dẫn chạy dự án
  </h2>
  
  <div style="background-color: #181715; border-radius: 12px; padding: 24px; color: #faf9f5; font-family: sans-serif; border: 1px solid #252320; line-height: 1.6;">
    <!-- Chrome-like header bar -->
    <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #252320; padding-bottom: 12px; margin-bottom: 20px;">
      <div style="display: flex; gap: 6px;">
        <span style="width: 10px; height: 10px; border-radius: 50%; background-color: #c64545; display: inline-block;"></span>
        <span style="width: 10px; height: 10px; border-radius: 50%; background-color: #e8a55a; display: inline-block;"></span>
        <span style="width: 10px; height: 10px; border-radius: 50%; background-color: #5db8a6; display: inline-block;"></span>
      </div>
      <span style="color: #a09d96; font-family: monospace; font-size: 12px; letter-spacing: 0.5px;">terminal &mdash; installation</span>
    </div>
    
    <!-- Content starts -->
    <div style="margin-bottom: 20px;">
      <h3 style="font-size: 15px; color: #ffffff; margin-top: 0; margin-bottom: 8px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Yêu cầu hệ thống</h3>
      <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #a09d96;">
        <li>Python 3.8 trở lên</li>
        <li>Trình quản lý gói <code style="font-family: monospace; color: #e8a55a; background-color: #1f1e1b; padding: 2px 6px; border-radius: 4px;">pip</code></li>
      </ul>
    </div>
    
    <div>
      <h3 style="font-size: 15px; color: #ffffff; margin-top: 20px; margin-bottom: 12px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Các bước cài đặt</h3>
      
      <ol style="margin: 0; padding-left: 20px; font-size: 14px; color: #a09d96; display: flex; flex-direction: column; gap: 16px;">
        <li>
          <strong style="color: #ffffff;">Clone thư mục dự án hoặc tải mã nguồn về máy tính.</strong>
        </li>
        <li>
          <strong style="color: #ffffff;">Tạo môi trường ảo Python (khuyên dùng):</strong>
          <div style="background-color: #1f1e1b; border-radius: 8px; padding: 12px 16px; margin-top: 6px; border: 1px solid #252320; font-family: monospace; font-size: 13px; color: #faf9f5;">
            <span style="color: #6c6a64;"># Trên macOS/Linux</span><br/>
            python3 -m venv .venv<br/>
            source .venv/bin/activate<br/><br/>
            <span style="color: #6c6a64;"># Trên Windows</span><br/>
            python -m venv .venv<br/>
            .venv\Scripts\activate
          </div>
        </li>
        <li>
          <strong style="color: #ffffff;">Cài đặt các thư viện cần thiết:</strong>
          <div style="background-color: #1f1e1b; border-radius: 8px; padding: 12px 16px; margin-top: 6px; border: 1px solid #252320; font-family: monospace; font-size: 13px; color: #faf9f5;">
            pip install pandas numpy matplotlib seaborn scikit-learn notebook scipy sqlite3
          </div>
        </li>
        <li>
          <strong style="color: #ffffff;">Khởi động Jupyter Notebook:</strong>
          <p style="margin: 6px 0 0 0; color: #a09d96;">
            Mở file <code style="font-family: monospace; color: #e8a55a; background-color: #1f1e1b; padding: 2px 6px; border-radius: 4px;">Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb</code> trong Jupyter Notebook (hoặc bất kỳ nền tảng nào hỗ trợ chạy .ipynb) và chạy tuần tự các cell.
          </p>
        </li>
      </ol>
    </div>
  </div>
</div>

<div style="margin-bottom: 48px;">
  <h2 style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-weight: 400; font-size: 24px; color: #141413; border-bottom: 1px solid #e6dfd8; padding-bottom: 8px; margin-bottom: 20px;">
    ✦ Cấu trúc thư mục dự án
  </h2>
  
  <div style="background-color: #181715; border-radius: 12px; padding: 24px; color: #faf9f5; font-family: sans-serif; border: 1px solid #252320; line-height: 1.6;">
    <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #252320; padding-bottom: 12px; margin-bottom: 16px;">
      <div style="display: flex; gap: 6px;">
        <span style="width: 10px; height: 10px; border-radius: 50%; background-color: #c64545; display: inline-block;"></span>
        <span style="width: 10px; height: 10px; border-radius: 50%; background-color: #e8a55a; display: inline-block;"></span>
        <span style="width: 10px; height: 10px; border-radius: 50%; background-color: #5db8a6; display: inline-block;"></span>
      </div>
      <span style="color: #a09d96; font-family: monospace; font-size: 12px; letter-spacing: 0.5px;">file-tree</span>
    </div>
    
    <div style="background-color: #1f1e1b; border-radius: 8px; padding: 16px; border: 1px solid #252320; font-family: monospace; font-size: 13px; overflow-x: auto; color: #faf9f5;">
      <strong>.</strong><br/>
      ├── <span style="color: #e8a55a;">Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb</span>  <span style="color: #6c6a64;"># Jupyter Notebook chính chứa toàn bộ mã nguồn</span><br/>
      ├── <span style="color: #cc785c;">DataCoSupplyChainDataset.csv</span>                                         <span style="color: #6c6a64;"># Tập dữ liệu chuỗi cung ứng gốc</span><br/>
      ├── <span style="color: #5db8a6;">freight_pricing_research.db</span>                                          <span style="color: #6c6a64;"># Cơ sở dữ liệu SQLite sạch</span><br/>
      ├── <span style="color: #e8a55a;">train_test_split.py</span>                                                  <span style="color: #6c6a64;"># Script chia tập train/test</span><br/>
      ├── <span style="color: #5db8a6;">charts_img/</span>                                                          <span style="color: #6c6a64;"># Thư mục lưu trữ biểu đồ xuất ra</span><br/>
      └── <span style="color: #faf9f5;">README.md</span>                                                            <span style="color: #6c6a64;"># Hướng dẫn dự án</span>
    </div>
  </div>
</div>

<div style="margin-bottom: 48px;">
  <h2 style="font-family: 'Cormorant Garamond', 'EB Garamond', 'Georgia', serif; font-weight: 400; font-size: 24px; color: #141413; border-bottom: 1px solid #e6dfd8; padding-bottom: 8px; margin-bottom: 20px;">
    ✦ Mô tả Tập dữ liệu (Dataset Metadata)
  </h2>
  <p style="font-size: 15px; color: #6c6a64; margin-bottom: 20px;">
    Dataset <code style="font-family: monospace; color: #cc785c; background-color: #efe9de; padding: 2px 6px; border-radius: 4px;">DataCoSupplyChainDataset.csv</code> chứa thông tin vận hành của <strong>180,519 giao dịch/đơn hàng</strong>, bao gồm <strong>53 thuộc tính</strong> khác nhau. Dưới đây là các cột dữ liệu chính được sử dụng:
  </p>
  
  <div style="overflow-x: auto; border: 1px solid #e6dfd8; border-radius: 12px;">
    <table style="width: 100%; border-collapse: collapse; font-family: sans-serif; font-size: 14px; color: #3d3d3a;">
      <thead>
        <tr style="background-color: #efe9de; border-bottom: 1px solid #e6dfd8; color: #141413;">
          <th style="padding: 12px 16px; text-align: left; font-weight: 600;">Tên cột</th>
          <th style="padding: 12px 16px; text-align: left; font-weight: 600; width: 120px;">Kiểu dữ liệu</th>
          <th style="padding: 12px 16px; text-align: left; font-weight: 600;">Mô tả ý nghĩa</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #faf9f5;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Type</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e8e0d2; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Categorical</span></td>
          <td style="padding: 12px 16px;">Phương thức thanh toán (DEBIT, TRANSFER, CASH, PAYMENT)</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #ffffff;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Days for shipping (real)</td>
          <td style="padding: 12px 16px;"><span style="background-color: #efe9de; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Integer</span></td>
          <td style="padding: 12px 16px;">Số ngày vận chuyển thực tế của đơn hàng</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #faf9f5;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Days for shipment (scheduled)</td>
          <td style="padding: 12px 16px;"><span style="background-color: #efe9de; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Integer</span></td>
          <td style="padding: 12px 16px;">Số ngày vận chuyển dự kiến theo lịch trình</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #ffffff;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Benefit per order</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e6dfd8; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Float</span></td>
          <td style="padding: 12px 16px;">Lợi nhuận thu được trên mỗi đơn hàng (USD)</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #faf9f5;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Sales</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e6dfd8; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Float</span></td>
          <td style="padding: 12px 16px;">Doanh số/giá trị sản phẩm bán ra (đại diện cho doanh số vận chuyển hàng hóa - USD)</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #ffffff;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Delivery Status</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e8e0d2; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Categorical</span></td>
          <td style="padding: 12px 16px;">Trạng thái giao hàng (Late delivery, Advance shipping, Shipping on time, Shipping canceled)</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #faf9f5;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Late_delivery_risk</td>
          <td style="padding: 12px 16px;"><span style="background-color: #efe9de; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Integer</span></td>
          <td style="padding: 12px 16px;">Rủi ro giao hàng trễ (1: Có rủi ro giao hàng trễ, 0: Không)</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #ffffff;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Category Name</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e8e0d2; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Categorical</span></td>
          <td style="padding: 12px 16px;">Tên danh mục của sản phẩm được vận chuyển</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #faf9f5;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Customer Segment</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e8e0d2; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Categorical</span></td>
          <td style="padding: 12px 16px;">Phân khúc khách hàng (Consumer, Corporate, Home Office)</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #ffffff;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Market</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e8e0d2; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Categorical</span></td>
          <td style="padding: 12px 16px;">Thị trường khu vực đích (Pacific Asia, USCA, Europe, LATAM, Africa)</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #faf9f5;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Order Item Quantity</td>
          <td style="padding: 12px 16px;"><span style="background-color: #efe9de; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Integer</span></td>
          <td style="padding: 12px 16px;">Số lượng sản phẩm của mặt hàng trong đơn hàng</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #ffffff;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Order Item Product Price</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e6dfd8; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Float</span></td>
          <td style="padding: 12px 16px;">Giá gốc của sản phẩm được đặt</td>
        </tr>
        <tr style="border-bottom: 1px solid #ebe6df; background-color: #faf9f5;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Order Profit Per Order</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e6dfd8; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Float</span></td>
          <td style="padding: 12px 16px;">Lợi nhuận của đơn hàng (USD)</td>
        </tr>
        <tr style="border-bottom: none; background-color: #ffffff;">
          <td style="padding: 12px 16px; font-family: monospace; font-weight: bold; color: #141413;">Shipping Mode</td>
          <td style="padding: 12px 16px;"><span style="background-color: #e8e0d2; color: #141413; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; display: inline-block;">Categorical</span></td>
          <td style="padding: 12px 16px;">Phương thức vận chuyển (Standard Class, Second Class, First Class, Same Day)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div style="background-color: #181715; color: #a09d96; border-radius: 12px; padding: 32px; border: 1px solid #252320; font-family: sans-serif; line-height: 1.6;">
  <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #252320; padding-bottom: 16px; margin-bottom: 24px; flex-wrap: wrap; gap: 12px;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="color: #cc785c; font-size: 20px;">✦</span>
      <span style="font-weight: bold; font-size: 16px; letter-spacing: 0.5px; color: #faf9f5;">NHÓM 7 &bull; LỚP AI2008</span>
    </div>
    <span style="font-size: 12px; color: #6c6a64; font-family: monospace;">ADY201m &mdash; PROJECT FOOTER</span>
  </div>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px;">
    <div>
      <h4 style="color: #faf9f5; font-size: 14px; margin-top: 0; margin-bottom: 12px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Thông tin môn học</h4>
      <p style="margin: 0 0 6px 0; font-size: 14px;"><strong style="color: #faf9f5;">Môn học:</strong> ADY201m</p>
      <p style="margin: 0; font-size: 14px;"><strong style="color: #faf9f5;">Lớp học:</strong> AI2008</p>
    </div>
    <div>
      <h4 style="color: #faf9f5; font-size: 14px; margin-top: 0; margin-bottom: 12px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Đề tài nghiên cứu</h4>
      <p style="margin: 0; font-size: 14px; line-height: 1.5; color: #faf9f5; font-style: italic;">
        AI-Driven Dynamic Pricing in Freight & Shipping Logistics
      </p>
    </div>
    <div>
      <h4 style="color: #faf9f5; font-size: 14px; margin-top: 0; margin-bottom: 12px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Thành viên nhóm</h4>
      <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #a09d96; display: flex; flex-direction: column; gap: 4px;">
        <li>Nguyễn Phạm Minh Triết</li>
        <li>Nguyễn Mạnh Hoàng</li>
        <li>Nguyễn Hoàng Duy Tiến</li>
        <li>Nguyễn Bùi Anh Duy</li>
      </ul>
    </div>
  </div>
</div>
</div>
