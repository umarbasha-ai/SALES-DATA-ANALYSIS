import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:/MY_AI_AND_ML_PROJECTS/Sales-data-analysis/DATASET/online_sales_dataset.csv")
print(df.columns)
print(df.info())
print("stastical information\n",df.describe())
print(df.isna().sum()) # null values in CustomerID, ShippingCost , WarehouseLocation
df.dropna(subset=['CustomerID', 'ShippingCost' , 'WarehouseLocation'],inplace=True)
print(df.isna().sum()) #after dropping - check for null values
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'],errors='coerce')
#create new column Total Sales
df['Total Sales'] = df['Quantity'] * df['UnitPrice'] * (1-df['Discount'])

# top 10 products by total sales
top_10_products = df.groupby('Description')['Total Sales'].sum().sort_values().head(10)
print("TOP 10 PRODUCTS")
print(top_10_products)
top_10_prod_names = top_10_products.index.tolist()

# visualize top 10 products 
#using bar plot
plt.figure(figsize=(10,6))
top_10_products.plot(kind='bar',color='teal')
# top_10_products.plot(kind='line',color='red')
plt.title("TOP 10 PRODUCTS BY SALE")
plt.xlabel("product description")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# visualize top 10 products 
#using line plot
plt.figure(figsize=(10,6))
top_10_products.plot(kind='line',color='blue',linestyle = "--",marker='o',markersize=10)
# top_10_products.plot(kind='line',color='red')
plt.title("TOP 10 PRODUCTS BY SALE")
plt.xlabel("product description")
plt.ylabel("Total Sales")
plt.xticks([i for i in range(1,len(top_10_prod_names)+1)],top_10_prod_names,rotation=90)
plt.tight_layout()
plt.grid(True)
plt.show()

# top 10 customers by purchase volume
df['CustomerID'] = df['CustomerID'].astype('Int64')
top_10_cust = df.groupby('CustomerID')['Total Sales'].sum().sort_values().head(10)
print("TOP 10 CUSTOMERS ")
print(top_10_cust)

#visualize top 10 customers 
plt.figure(figsize=(10,6))
top_10_cust.plot(kind='bar', color = 'coral')
plt.title("TOP 10 CUSTOMERS BY PURCHASE VOLUME")
plt.xlabel("CUSTOMER ID")
plt.ylabel("TOTAL SALES")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()