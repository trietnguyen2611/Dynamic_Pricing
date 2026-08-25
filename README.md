# ✦ AI2008 - Group 7: Analysis & Dynamic Pricing in Freight & Shipping Logistics

<p align="center">
  <strong>Analysis & Dynamic Pricing with Artificial Intelligence in Logistics</strong>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8+-cc785c?style=flat-square&logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter-Notebook-181715?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/></a>
  <a href="https://sqlite.org/"><img src="https://img.shields.io/badge/SQLite-Database-cc785c?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite"/></a>
  <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/scikit--learn-Machine--Learning-181715?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/></a>
  <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Pandas-Data--Analysis-cc785c?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/></a>
</p>

---

## ✦ Project Introduction

This project studies and uses data analysis, advanced SQL queries, and machine learning algorithms to solve the **Dynamic Pricing** problem in Logistics and freight transport (Freight & Shipping).

We use a real supply chain dataset (DataCo Supply Chain Dataset) to study market factors, shipping methods, and customer behavior. The goal is to improve shipping sales, make the supply chain better, and build models that can predict and optimize shipping prices in real time. This helps logistics companies compete better.

---

## ✦ Research Questions

The project is built around 3 main research questions:

> [!TIP]
> ### ✦ RQ1: Market Factors
> - **Which market factors affect shipping prices?**
> - *Which market factors affect transport price?*

> [!NOTE]
> ### ✦ RQ2: AI Modeling
> - **Which AI model can predict and improve dynamic shipping prices?**
> - *Which AI model can predict and improve the price in real time?*

> [!IMPORTANT]
> ### ✦ RQ3: Revenue Impact
> - **How much can dynamic pricing increase freight revenue compared to fixed prices?**
> - *How much can dynamic pricing increase freight revenue over fixed price?*

---

## ✦ How to Run the Project

### System Requirements
* Python 3.8 or higher
* Package manager `pip`

### Installation Steps

1. **Clone the project folder or download the source code to your computer.**
2. **Create a Python virtual environment (recommended):**
   ```bash
   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate

   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. **Install the needed libraries:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn notebook scipy sqlite3
   ```
4. **Start Jupyter Notebook:**
   Open the file `Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb` in Jupyter Notebook (or any platform that supports `.ipynb` files) and run the cells one by one.

---

## ✦ Project Folder Structure

```text
.
├── Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb  # Jupyter Notebook
├── DataCoSupplyChainDataset.csv                                         # Original supply chain dataset
├── freight_pricing_research.db                                          # Clean SQLite database
├── train_test_split.py                                                  # Script to split train/test sets
├── charts_img/                                                          # Folder for output charts
└── README.md                                                            # Project guide
```

---

## ✦ Dataset Description (Dataset Metadata)

The dataset `DataCoSupplyChainDataset.csv` has information about **180,519 transactions/orders** and **53 different attributes**. Below are the main columns we use:

| Column Name | Data Type | Meaning |
| :--- | :--- | :--- |
| **Type** | `Categorical` | Payment method (DEBIT, TRANSFER, CASH, PAYMENT) |
| **Days for shipping (real)** | `Integer` | Real number of days to ship the order |
| **Days for shipment (scheduled)** | `Integer` | Planned number of days to ship |
| **Benefit per order** | `Float` | Profit from each order (USD) |
| **Sales** | `Float` | Sales / product value (represents shipping sales - USD) |
| **Delivery Status** | `Categorical` | Delivery status (Late delivery, Advance shipping, Shipping on time, Shipping canceled) |
| **Late_delivery_risk** | `Integer` | Risk of late delivery (1: Yes, 0: No) |
| **Category Name** | `Categorical` | Name of the product category being shipped |
| **Customer Segment** | `Categorical` | Customer group (Consumer, Corporate, Home Office) |
| **Market** | `Categorical` | Target market area (Pacific Asia, USCA, Europe, LATAM, Africa) |
| **Order Item Quantity** | `Integer` | Number of items in the order |
| **Order Item Product Price** | `Float` | Original price of the ordered product |
| **Order Profit Per Order** | `Float` | Order profit (USD) |
| **Shipping Mode** | `Categorical` | Shipping method (Standard Class, Second Class, First Class, Same Day) |

---

## ✦ Project Information (Project Metadata)

<table width="100%">
  <tr>
    <td width="33%" valign="top">
      <strong>Course Information</strong><br>
      • Course: ADY201m<br>
      • Class: AI2008
    </td>
    <td width="34%" valign="top">
      <strong>Research Topic</strong><br>
      <em>AI-Driven Dynamic Pricing in Freight & Shipping Logistics</em>
    </td>
    <td width="33%" valign="top">
      <strong>Group Members (Group 7)</strong><br>
      • Nguyễn Phạm Minh Triết<br>
      • Nguyễn Mạnh Hoàng<br>
      • Nguyễn Hoàng Duy Tiến<br>
      • Nguyễn Bùi Anh Duy
    </td>
  </tr>
</table>
