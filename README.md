# AI-Driven Dynamic Pricing in Freight & Shipping Logistics

**AI2008 – Group 7**  
Research project on **dynamic pricing** for freight and shipping using machine learning and data analysis.

This project studies how market factors, shipping modes, and customer behavior affect transport prices. We build AI models to predict and optimize shipping prices in real time to increase revenue for logistics companies.

---

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8+-cc785c?style=flat-square&logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter-Notebook-181715?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/></a>
  <a href="https://sqlite.org/"><img src="https://img.shields.io/badge/SQLite-Database-cc785c?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite"/></a>
  <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/scikit--learn-Machine--Learning-181715?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/></a>
  <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Pandas-Data--Analysis-cc785c?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/></a>
</p>

---

## Project Overview

We use the real **DataCo Supply Chain Dataset** (180,519 orders) to answer three research questions about dynamic pricing in logistics:

> [!TIP]
> ### RQ1: Market Factors
> Which market factors affect transport and shipping prices?

> [!NOTE]
> ### RQ2: AI Modeling
> Which machine learning model can best predict and improve dynamic pricing in real time?

> [!IMPORTANT]
> ### RQ3: Revenue Impact
> How much extra revenue can dynamic pricing create compared to fixed prices?

---

## How to Run the Project

### Requirements
- Python 3.8 or higher
- `pip` package manager

### Installation Steps

1. Clone or download this repository.
2. Create a virtual environment (recommended):

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

3. Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn notebook scipy
```

4. Open the main notebook and run all cells:

`Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb`

---

## Project Structure

```text
.
├── Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb  # Main Jupyter Notebook
├── DataCoSupplyChainDataset.csv                                         # Original supply chain data
├── freight_pricing_research.db                                          # Cleaned SQLite database
├── train_test_split.py                                                  # Train/test split script
├── charts_img/                                                          # Output charts folder
└── README.md                                                            # This file
```

---

## Dataset Overview

The dataset contains **180,519 orders** and **53 columns**. Main columns used in this research:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| Type | Categorical | Payment method (DEBIT, TRANSFER, CASH, PAYMENT) |
| Days for shipping (real) | Integer | Actual shipping days |
| Days for shipment (scheduled) | Integer | Planned shipping days |
| Benefit per order | Float | Profit per order (USD) |
| Sales | Float | Order value / sales (USD) |
| Delivery Status | Categorical | Late, on time, canceled, etc. |
| Late_delivery_risk | Integer | 1 = risk of late delivery, 0 = no risk |
| Category Name | Categorical | Product category |
| Customer Segment | Categorical | Consumer, Corporate, Home Office |
| Market | Categorical | Pacific Asia, USCA, Europe, LATAM, Africa |
| Order Item Quantity | Integer | Quantity of items |
| Order Item Product Price | Float | Product unit price |
| Order Profit Per Order | Float | Order profit (USD) |
| Shipping Mode | Categorical | Standard, Second, First, Same Day |

---

## Project Information

| Course | Research Topic | Group Members |
| :--- | :--- | :--- |
| ADY201m – AI2008 | AI-Driven Dynamic Pricing in Freight & Shipping Logistics | Nguyễn Phạm Minh Triết<br>Nguyễn Mạnh Hoàng<br>Nguyễn Hoàng Duy Tiến<br>Nguyễn Bùi Anh Duy |

---

## Keywords

`dynamic pricing` `freight logistics` `shipping price prediction` `machine learning logistics` `supply chain AI` `scikit-learn` `pandas` `DataCo dataset` `revenue optimization`
