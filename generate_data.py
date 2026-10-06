import pandas as pd
import numpy as np

np.random.seed(42)
n_rows = 5000

categories = {
    "Direct Materials": ["Raw Metals", "Polymers", "Electronic Components"],
    "Logistics & Freight": ["Road Transport", "Ocean Freight", "Warehousing"],
    "IT & Software": ["Cloud Infrastructure", "SaaS Subscriptions", "Hardware"],
    "Professional Services": ["Legal", "Management Consulting", "Audit"],
    "Facilities & MRO": ["Maintenance", "Cleaning Services", "Office Supplies"]
}

cat_list = list(categories.keys())
cat_weights = [0.45, 0.20, 0.15, 0.12, 0.08]

business_units = ["Nordics", "Central Europe", "North America", "APAC"]
bu_weights = [0.40, 0.30, 0.20, 0.10]

strategic_suppliers = [f"Strategic Partner {i:02d}" for i in range(1, 31)]
tail_suppliers = [f"Vendor {i:03d}" for i in range(1, 301)]

data = []
dates = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")

for i in range(1, n_rows + 1):
    inv_id = f"INV-2025-{i:05d}"
    date = np.random.choice(dates)
    formatted_date = pd.to_datetime(date).strftime("%Y-%m-%d")
    category = np.random.choice(cat_list, p=cat_weights)
    subcategory = np.random.choice(categories[category])
    bu = np.random.choice(business_units, p=bu_weights)
    
    if np.random.rand() < 0.70:
        supplier = np.random.choice(strategic_suppliers)
        contract = np.random.choice(["Active Contract", "No Contract"], p=[0.92, 0.08])
        spend = np.round(np.random.exponential(scale=25000) + 3000, 2)
    else:
        supplier = np.random.choice(tail_suppliers)
        contract = np.random.choice(["Active Contract", "No Contract"], p=[0.25, 0.75])
        spend = np.round(np.random.exponential(scale=2500) + 150, 2)
        
    data.append([inv_id, formatted_date, supplier, category, subcategory, spend, bu, contract])

df = pd.DataFrame(data, columns=[
    "Invoice_ID", "Invoice_Date", "Supplier_Name", "Category", 
    "Subcategory", "Spend_EUR", "Business_Unit", "Contract_Status"
])

df.to_csv("procurement_spend_data_2025.csv", index=False)
print("Data luotu onnistuneesti! Rivimäärä:", len(df))
