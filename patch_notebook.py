import json

notebook_path = "/Users/trietnguyen/Downloads/AI2008-Group-7-Python_Notebook/Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and len(cell['source']) > 0 and '5.1' in cell['source'][0] and 'FEATURE 1' in cell['source'][0]:
        print("Found section 5.1!")
        # Update Markdown cell
        cell['source'] = ["### 5.1. FEATURE 1: Tổng nhu cầu (Demand) theo ngày đặt hàng\n",
                          "Vì dataset mới không có Cung và Cầu (như số lượng tài xế), ta tính tổng nhu cầu đặt hàng (`Order Item Quantity`) mỗi ngày làm Feature đại diện cho Demand."]
        
        # Update the next Code cell
        if i + 1 < len(nb['cells']) and nb['cells'][i+1]['cell_type'] == 'code':
            code_cell = nb['cells'][i+1]
            code_cell['source'] = [
                "import pandas as pd\n",
                "\n",
                "# 1. Đọc file dữ liệu gốc\n",
                "# Sử dụng encoding 'latin1' cho DataCoSupplyChainDataset\n",
                "df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding='latin1')\n",
                "\n",
                "# 2. Xử lý ngày tháng và tính tổng nhu cầu (Order Item Quantity) theo ngày\n",
                "df['order date (DateOrders)'] = pd.to_datetime(df['order date (DateOrders)'])\n",
                "df['Order_Date_Only'] = df['order date (DateOrders)'].dt.date\n",
                "daily_demand = df.groupby('Order_Date_Only')['Order Item Quantity'].sum().reset_index()\n",
                "daily_demand.rename(columns={'Order Item Quantity': 'Daily_Demand'}, inplace=True)\n",
                "\n",
                "# Merge lại vào dataframe gốc\n",
                "df = df.merge(daily_demand, on='Order_Date_Only', how='left')\n",
                "\n",
                "# 3. Lưu và kiểm tra kết quả\n",
                "df.to_csv('features.csv', index=False) # dùng file này để train model cho các Feature tiếp theo\n",
                "print('Feature 1: Daily_Demand')\n",
                "print(df[['Order_Date_Only', 'Order Item Quantity', 'Daily_Demand']].head())\n"
            ]
            # Clear outputs
            code_cell['outputs'] = []
            print("Patched code cell.")
        break

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Notebook saved.")
