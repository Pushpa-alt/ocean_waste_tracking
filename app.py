import streamlit as st
from utils import load_data
from model import train_model

st.set_page_config(page_title="Ocean Waste Tracker", layout="wide")

st.title("🌊 Ocean Waste Tracking System")

# Load data
df, le = load_data()

# Train model
model = train_model(df)

st.sidebar.header("Enter Waste Details")

waste_type = st.sidebar.selectbox("Waste Type", ["plastic","glass","organic","metal"])
quantity = st.sidebar.slider("Quantity", 0, 100)
area_type = st.sidebar.selectbox("Area Type", ["coastal","tourist","industrial","fishing"])

# Convert input
waste_encoded = le.fit_transform([waste_type])[0]
area_encoded = le.fit_transform([area_type])[0]

# Predict
if st.sidebar.button("Predict"):
    result = model.predict([[waste_encoded, quantity, area_encoded]])
    
    levels = ["low", "medium", "high"]
    
    st.subheader("Predicted Pollution Level")
    st.success(levels[result[0]])