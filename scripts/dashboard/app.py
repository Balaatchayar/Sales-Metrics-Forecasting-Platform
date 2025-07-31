import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly
from datetime import datetime

# Load cleaned data
df = pd.read_csv("../../clean_data/cleaned_sales_data_2025.csv", parse_dates=["Date"])

# ------------------- UI Config -------------------
st.set_page_config(page_title="Smart Sales Insights", layout="wide")
st.title(" Smart Sales Insights Engine")
st.markdown("###  Empowering Sales Decisions with Data")

# ------------------- KPI Cards -------------------
total_sales = df["TotalPrice"].sum()
total_quantity = df["Quantity"].sum()
num_orders = df["InvoiceID"].nunique()
avg_order_value = total_sales / num_orders

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Sales", f"₹{total_sales:,.0f}")
col2.metric("📦 Total Quantity", total_quantity)
col3.metric("🧾 Number of Orders", num_orders)
col4.metric("📊 Avg Order Value", f"₹{avg_order_value:,.0f}")

# ------------------- Filters -------------------
st.sidebar.header("🔍 Filter Data")

regions = st.sidebar.multiselect("Select Region", df["Region"].unique(), default=df["Region"].unique())
categories = st.sidebar.multiselect("Select Category", df["Category"].unique(), default=df["Category"].unique())
start_date = st.sidebar.date_input("Start Date", df["Date"].min().date())
end_date = st.sidebar.date_input("End Date", df["Date"].max().date())

# Apply filters safely
filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories)) &
    (df["Date"].dt.date >= start_date) &
    (df["Date"].dt.date <= end_date)
]

# ------------------- Visualizations -------------------
st.markdown("### 📊 Visual Insights")

# Time Series
time_chart = filtered_df.groupby(filtered_df["Date"].dt.to_period("M"))["TotalPrice"].sum().reset_index()
time_chart["Date"] = time_chart["Date"].dt.to_timestamp()
fig_time = px.line(time_chart, x="Date", y="TotalPrice", title="📈 Monthly Sales Trend")
st.plotly_chart(fig_time, use_container_width=True)

# Category Sales
cat_chart = filtered_df.groupby("Category")["TotalPrice"].sum().reset_index()
fig_cat = px.bar(cat_chart, x="Category", y="TotalPrice", title="📦 Sales by Category", color="Category")
st.plotly_chart(fig_cat, use_container_width=True)

# Region Pie Chart
region_chart = filtered_df.groupby("Region")["TotalPrice"].sum().reset_index()
fig_region = px.pie(region_chart, values="TotalPrice", names="Region", title="🌍 Region-wise Sales Share")
st.plotly_chart(fig_region, use_container_width=True)

# Top Products
st.markdown("### 🏆 Top 5 Products by Revenue")
top_products = filtered_df.groupby("Product")["TotalPrice"].sum().nlargest(5).reset_index()
st.dataframe(top_products)

# ------------------- Download -------------------
st.markdown("### 📥 Export Filtered Data")
custom_name = st.text_input("Enter file name (without .csv)", "sales_report")
st.download_button(
    label="Download CSV",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name=f"{custom_name}.csv",
    mime="text/csv"
)

# ------------------- Smart Insights -------------------
st.markdown("### 🔍 Smart Insights")

best_region = region_chart.sort_values("TotalPrice", ascending=False).iloc[0]["Region"]
worst_category = cat_chart.sort_values("TotalPrice").iloc[0]["Category"]
peak_month = time_chart.sort_values("TotalPrice", ascending=False).iloc[0]["Date"].strftime("%B %Y")

st.info(f"""
✅ **Best Performing Region:** {best_region}  
🚫 **Worst Performing Category:** {worst_category}  
📈 **Peak Sales Month:** {peak_month}  
💡 **Tip:** Increase stock of top-selling product `{top_products.iloc[0]['Product']}`.
""")

# ------------------- Prophet Forecast -------------------
st.markdown("### 🔮 Sales Forecast")

# Prepare data for Prophet
prophet_df = df[["Date", "TotalPrice"]].rename(columns={"Date": "ds", "TotalPrice": "y"})
prophet_model = Prophet()
prophet_model.fit(prophet_df)

# Future predictions
future = prophet_model.make_future_dataframe(periods=180)
forecast = prophet_model.predict(future)

# Plot forecast
fig_forecast = plot_plotly(prophet_model, forecast)
st.plotly_chart(fig_forecast, use_container_width=True)
st.caption("📉 Prophet-based forecast for the next 6 months with confidence intervals.")

# ------------------- Branding -------------------
st.sidebar.markdown("---")
st.sidebar.caption("Built by Bala Atchaya R  with using Streamlit")

