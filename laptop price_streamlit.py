#!/usr/bin/env python
# coding: utf-8

# In[2]:


# In[3]:


import streamlit as st
import pickle
import numpy as np
import pandas as pd

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide"
)

# -------------------------------
# Load model and dataframe
# -------------------------------
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# -------------------------------
# Custom styling
# -------------------------------
st.markdown("""
    <style>
        .main {
            padding-top: 1rem;
        }
        .title-text {
            font-size: 38px;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 0.2rem;
        }
        .subtitle-text {
            font-size: 16px;
            color: #6b7280;
            margin-bottom: 2rem;
        }
        .prediction-box {
            background-color: #f8fafc;
            padding: 22px;
            border-radius: 14px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-top: 20px;
        }
        .prediction-label {
            font-size: 18px;
            color: #6b7280;
            margin-bottom: 8px;
        }
        .prediction-value {
            font-size: 34px;
            font-weight: 700;
            color: #111827;
        }
        .section-header {
            font-size: 22px;
            font-weight: 600;
            margin-top: 10px;
            margin-bottom: 12px;
            color: #111827;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown('<div class="title-text">💻 Laptop Price Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-text">Estimate the price of a laptop based on its configuration and hardware specifications.</div>',
    unsafe_allow_html=True
)

# -------------------------------
# Layout
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)

    company = st.selectbox('Brand', sorted(df['Company'].unique()))
    laptop_type = st.selectbox('Laptop Type', sorted(df['TypeName'].unique()))
    ram = st.selectbox('RAM (GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=1.5, step=0.1)

    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    ips = st.selectbox('IPS Display', ['No', 'Yes'])
    os = st.selectbox('Operating System', sorted(df['os'].unique()))

with col2:
    st.markdown('<div class="section-header">Display & Hardware</div>', unsafe_allow_html=True)

    screen_size = st.slider('Screen Size (inches)', 10.0, 18.0, 13.3, step=0.1)

    resolution = st.selectbox(
        'Screen Resolution',
        [
            '1920x1080',
            '1366x768',
            '1600x900',
            '3840x2160',
            '3200x1800',
            '2880x1800',
            '2560x1600',
            '2560x1440',
            '2304x1440'
        ]
    )

    cpu = st.selectbox('CPU Brand', sorted(df['Cpu brand'].unique()))
    gpu = st.selectbox('GPU Brand', sorted(df['Gpu brand'].unique()))
    hdd = st.selectbox('HDD Capacity (GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox('SSD Capacity (GB)', [0, 8, 128, 256, 512, 1024])

# -------------------------------
# Predict button
# -------------------------------
st.markdown("")
predict_btn = st.button('🔍 Predict Laptop Price', use_container_width=True)

if predict_btn:
    # Convert categorical yes/no to binary
    touchscreen_val = 1 if touchscreen == 'Yes' else 0
    ips_val = 1 if ips == 'Yes' else 0

    # Compute PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size

    # Final query must match training feature order exactly
    query = pd.DataFrame({
    'Company': [company],
    'TypeName': [laptop_type],
    'RAM': [ram],
    'Weight': [weight],
    'Touchscreen': [touchscreen_val],
    'Ips': [ips_val],
    'ppi': [ppi],
    'Cpu brand': [cpu],
    'HDD': [hdd],
    'SSD': [ssd],
    'Gpu brand': [gpu],
    'os': [os]
})

    # Prediction
    predicted_price = int(pipe.predict(query)[0])

    # Output card
    st.markdown(
        f"""
        <div class="prediction-box">
            <div class="prediction-label">Estimated Laptop Price</div>
            <div class="prediction-value">₹ {predicted_price:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Optional details
    with st.expander("View configuration summary"):
        st.write("### Selected Configuration")
        st.write(f"**Brand:** {company}")
        st.write(f"**Type:** {laptop_type}")
        st.write(f"**RAM:** {ram} GB")
        st.write(f"**Weight:** {weight} kg")
        st.write(f"**Touchscreen:** {touchscreen}")
        st.write(f"**IPS Display:** {ips}")
        st.write(f"**Screen Size:** {screen_size} inches")
        st.write(f"**Resolution:** {resolution}")
        st.write(f"**Computed PPI:** {round(ppi, 2)}")
        st.write(f"**CPU Brand:** {cpu}")
        st.write(f"**GPU Brand:** {gpu}")
        st.write(f"**HDD:** {hdd} GB")
        st.write(f"**SSD:** {ssd} GB")
        st.write(f"**Operating System:** {os}")


# In[ ]:




