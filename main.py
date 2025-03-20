import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Order to Delivery Time Prediction")
st.write("Enter order details to predict the expected delivery time.")

# Input Fields
product_category = st.selectbox("Product Category", ["Electronics", "Books", "Clothing", "Furniture", "Toys"]) # Example categories
customer_location = st.text_input("Customer Location (City)")
shipping_method = st.selectbox("Shipping Method", ["Standard", "Express", "Same-day"])

# Simple rule-based model to predict delivery time
def predict_delivery_time(product_category, shipping_method):
    base_time = {
        "Electronics": 5,
        "Books": 3,
        "Clothing": 4,
        "Furniture": 7,
        "Toys": 2
    }
    shipping_modifier = {"Standard": 0, "Express": -1, "Same-day": -2}
    
    return max(1, base_time.get(product_category, 5) + shipping_modifier.get(shipping_method, 0))

if st.button("Predict Delivery Time"):
    prediction = predict_delivery_time(product_category, shipping_method)
    st.success(f"Expected Delivery Time: {prediction} days")

# Delivery Time Visualization
st.write("## Delivery Time Estimation Chart")
delivery_times = {category: [predict_delivery_time(category, method) for method in ["Standard", "Express", "Same-day"]] for category in ["Electronics", "Books", "Clothing", "Furniture", "Toys"]}
df_delivery = pd.DataFrame(delivery_times, index=["Standard", "Express", "Same-day"])

st.line_chart(df_delivery)
