import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")
payments = pd.read_csv("data/payments.csv")

# Merge all tables
df = orders.merge(customers, on="customer_id")
df = df.merge(order_items, on="order_id")
df = df.merge(products, on="product_id")
df = df.merge(payments, on="order_id")

print("Merged E-Commerce Data")
print(df)
# Total sales/revenue
total_sales = df["payment_value"].sum()

print("\nTotal Sales / Revenue")
print(total_sales)
# Top Selling Products
top_products = df.groupby("product_name")["quantity"].sum()

print("\nTop Selling Products")
print(top_products.sort_values(ascending=False))
# Monthly Revenue Trend
df["order_date"] = pd.to_datetime(df["order_date"])

monthly_sales = df.groupby(
    df["order_date"].dt.strftime("%Y-%m")
)["payment_value"].sum()

print("\nMonthly Revenue")
print(monthly_sales)
# Best Performing Categories
category_sales = df.groupby("category")["payment_value"].sum()

print("\nCategory-wise Revenue")
print(category_sales.sort_values(ascending=False))
# Best Customers
customer_sales = df.groupby("customer_name")["payment_value"].sum()

print("\nTop Customers")
print(customer_sales.sort_values(ascending=False))
# Region-wise Sales
region_sales = df.groupby("region")["payment_value"].sum()

print("\nRegion-wise Sales")
print(region_sales.sort_values(ascending=False))
# Export merged data for dashboard
df.to_csv("dashboard/dashboard_data.csv", index=False)

print("Dashboard data exported successfully!")
# Top Products Bar Chart
plt.figure()
top_products.sort_values(ascending=False).plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("images/top_products_chart.png")
plt.close()

# Monthly Revenue Line Chart
plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("images/monthly_revenue_chart.png")
plt.close()
# Category Revenue Chart
plt.figure()
category_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Category-wise Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("images/category_revenue_chart.png")
plt.close()
# Best Customer Chart
plt.figure()
customer_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Top Customers by Revenue")
plt.xlabel("Customer Name")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("images/top_customers_chart.png")
plt.close()
# Region-wise Sales Chart
plt.figure()
region_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("images/region_sales_chart.png")
plt.close()