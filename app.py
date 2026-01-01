import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="CardioVision AI",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS STYLING (FINAL POLISHED THEME)
# ==========================================
st.markdown("""
    <style>
    /* --- COLOR VARIABLES --- */
    :root {
        --bg-color: #000000;
        --card-bg: #121212;
        --text-color: #ffffff;
        --accent-green: #00ff88;
        --accent-cyan: #00c6ff;
    }

    /* --- GLOBAL BACKGROUND --- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: var(--bg-color); 
        color: var(--text-color);
    }
    
    .stApp {
        background-color: var(--bg-color);
    }

    /* --- TABS STYLING (FIXED ALIGNMENT) --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
        padding: 0;
        margin-bottom: 20px;
        border-bottom: 1px solid #333;
    }

    .stTabs [data-baseweb="tab"] {
        height: auto;
        padding: 12px 24px;
        background-color: #0a0a0a;
        color: #888;
        border-radius: 8px 8px 0 0;
        border: 1px solid transparent;
        font-weight: 600;
        font-size: 14px;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: #121212;
        color: #fff;
    }

    /* Active Tab: Green Highlight */
    .stTabs [aria-selected="true"] {
        background-color: #121212 !important;
        color: #00ff88 !important;
        border: 1px solid #00ff88;
        border-bottom: 1px solid #121212; /* seamless blend */
        font-weight: 800;
        box-shadow: 0 -4px 15px rgba(0, 255, 136, 0.1);
    }
    
    /* Remove default underline */
    .stTabs [data-baseweb="tab-highlight"] {
        display: none;
    }

    /* --- HEART LOGO ANIMATION (FIXED WIDTH) --- */
    .heart-logo {
        font-size: 80px;
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
        filter: drop-shadow(0 0 10px rgba(255, 65, 108, 0.5));
        animation: lubDub 1.5s infinite ease-in-out;
        line-height: 1; /* Fix vertical spacing */
    }
    
    @keyframes lubDub {
        0% { transform: scale(1); }
        10% { transform: scale(1.15); }
        20% { transform: scale(1); }
        30% { transform: scale(1.15); }
        40% { transform: scale(1); }
        100% { transform: scale(1); }
    }

    /* --- ECG MONITOR --- */
    .monitor-wrapper {
        background: #0a0a0a;
        padding: 5px;
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(0, 255, 136, 0.15); 
        border: 1px solid #222;
        margin-top: 10px;
    }

    .monitor-screen {
        width: 100%;
        background-color: #000000;
        border-radius: 8px;
        position: relative;
        overflow: hidden;
        height: 70px;
    }
    
    .ecg-path {
        fill: none;
        stroke: #00ff88;
        stroke-width: 2.5;
        stroke-linecap: round;
        stroke-linejoin: round;
        filter: drop-shadow(0 0 6px #00ff88);
        stroke-dasharray: 1000;
        stroke-dashoffset: 1000;
        animation: drawECG 2.5s linear infinite;
    }
    
    @keyframes drawECG {
        to { stroke-dashoffset: 0; }
    }

    /* --- FORM HEADERS --- */
    .section-header {
        font-size: 20px;
        font-weight: 700;
        color: #00ff88;
        margin-bottom: 20px;
        padding-bottom: 8px;
        border-bottom: 2px solid #00ff88;
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
    }

    /* --- INPUT STYLING --- */
    .stNumberInput label, .stSelectbox label, .stRadio label, .stToggle label, .stFileUploader label, .stSlider label {
        color: white !important;
        font-weight: 600;
    }
    .stNumberInput input, .stSelectbox div[data-baseweb="select"] > div {
        background-color: var(--card-bg); 
        color: white;
        border: 1px solid #333;
    }
    div[data-baseweb="popover"], div[data-baseweb="menu"] {
        background-color: var(--card-bg);
    }

    /* --- BUTTON STYLING (UPDATED TO GREEN) --- */
    .stButton>button {
        background: linear-gradient(90deg, #00ff88 0%, #00cc6a 100%); 
        color: #000000; /* Black Text for Contrast */
        border: none;
        padding: 18px;
        font-size: 18px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 12px;
        width: 100%;
        margin-top: 25px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0, 255, 136, 0.3); 
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 25px rgba(0, 255, 136, 0.7);
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HEADER: LOGO & ANIMATION (ALIGNED)
# ==========================================
col_h1, col_h2 = st.columns([1.5, 4]) 

with col_h1:
    # Flexbox for perfect vertical alignment
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 20px; padding-top: 15px;">
            <div style="width: 80px; text-align: center;">
                <div class="heart-logo">♥</div>
            </div>
            <div>
                <h1 style="margin:0; font-weight:800; color: #00ff88; font-size: 36px; letter-spacing:-1px; text-shadow: 0 0 10px rgba(0,255,136,0.3); line-height: 1;">CardioVision</h1>
                <p style="margin:5px 0 0 0; color:#00c6ff; font-size:14px; font-weight:700; letter-spacing: 1px;">AI DIAGNOSTICS</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_h2:
    st.markdown("""
        <div class="monitor-wrapper">
            <div class="monitor-screen">
                <svg width="100%" height="100%" viewBox="0 0 500 100" preserveAspectRatio="none">
                    <defs>
                        <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
                            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#222" stroke-width="1"/>
                        </pattern>
                    </defs>
                    <rect width="100%" height="100%" fill="url(#grid)" />
                    <path class="ecg-path" d="M0,50 L50,50 L60,20 L70,80 L80,50 L150,50 L160,20 L170,80 L180,50 L250,50 L260,20 L270,80 L280,50 L350,50 L360,20 L370,80 L380,50 L450,50 L460,20 L470,80 L480,50 L500,50" />
                </svg>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# 4. LOAD RESOURCES & HELPER FUNCTIONS
# ==========================================
@st.cache_resource
def load_resources():
    try:
        model = joblib.load('best_cardio_model.pkl')
        scaler = joblib.load('scaler.pkl')
        return model, scaler
    except Exception as e:
        st.error(f"System Error: {e}")
        return None, None

model, scaler = load_resources()

def preprocess_input(row):
    """Helper to convert raw input dict into model-ready dataframe"""
    height_m = row['height'] / 100
    bmi = row['weight'] / (height_m ** 2)
    
    if bmi < 18.5: bmi_cat = 0
    elif 18.5 <= bmi < 25: bmi_cat = 1
    elif 25 <= bmi < 30: bmi_cat = 2
    else: bmi_cat = 3
    
    cols = ['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'BMI', 
            'gender_2', 'cholesterol_2', 'cholesterol_3', 
            'gluc_2', 'gluc_3', 'smoke_1', 'alco_1', 'active_1', 
            'BMI_category_1', 'BMI_category_2', 'BMI_category_3']
    
    data = {col: 0 for col in cols}
    
    data['age'] = row['age']
    data['height'] = row['height']
    data['weight'] = row['weight']
    data['ap_hi'] = row['ap_hi']
    data['ap_lo'] = row['ap_lo']
    data['BMI'] = bmi
    
    # One-Hot Encoding Logic
    if row['gender'] == 2 or row['gender'] == 'Male': data['gender_2'] = 1
    if row['cholesterol'] == 2: data['cholesterol_2'] = 1
    elif row['cholesterol'] == 3: data['cholesterol_3'] = 1
    if row['gluc'] == 2: data['gluc_2'] = 1
    elif row['gluc'] == 3: data['gluc_3'] = 1
    if row['smoke'] == 1: data['smoke_1'] = 1
    if row['alco'] == 1: data['alco_1'] = 1
    if row['active'] == 1: data['active_1'] = 1
    if bmi_cat == 1: data['BMI_category_1'] = 1
    if bmi_cat == 2: data['BMI_category_2'] = 1
    if bmi_cat == 3: data['BMI_category_3'] = 1
    
    return pd.DataFrame([data], columns=cols), bmi

# ==========================================
# 5. GLOBAL CONFIGURATION (DECIMAL THRESHOLD)
# ==========================================
with st.expander("⚙️ Model Configuration (Decision Threshold)"):
    st.write("Adjust the decimal probability threshold for classifying High Risk vs Low Risk.")
    # UPDATED: Slider uses floats 0.0 to 1.0 (Default 0.5)
    DECISION_THRESHOLD = st.slider(
        "Decision Threshold (0.0 - 1.0)", 
        min_value=0.0, max_value=1.0, value=0.5, step=0.01,
        help="If the model probability (0-1) is higher than this value, the patient is classified as High Risk."
    )

# ==========================================
# 6. MAIN NAVIGATION (TABS)
# ==========================================
tab1, tab2 = st.tabs([" SINGLE PREDICTION", " BATCH PREDICTION"])

# ==========================================
# TAB 1: SINGLE PREDICTION
# ==========================================
with tab1:
    st.write("") 
    with st.form("medical_intake_form"):
        c1, c2, c3 = st.columns(3)
        
        # --- COLUMN 1 ---
        with c1:
            st.markdown('<div class="section-header"> Patient Demographics</div>', unsafe_allow_html=True)
            gender = st.radio("Gender", ["Female", "Male"], horizontal=True)
            age = st.number_input("Age (Years)", 20, 100, 50)
            height = st.number_input("Height (cm)", 100, 250, 165)
            weight = st.number_input("Weight (kg)", 30, 200, 70)

        # --- COLUMN 2 ---
        with c2:
            st.markdown('<div class="section-header"> Clinical Vitals</div>', unsafe_allow_html=True)
            ap_hi = st.number_input("Systolic BP (High)", 50, 250, 120)
            ap_lo = st.number_input("Diastolic BP (Low)", 30, 150, 80)
            
            chol_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
            chol = st.selectbox("Cholesterol Level", options=list(chol_map.keys()))
            
            gluc_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
            gluc = st.selectbox("Glucose Level", options=list(gluc_map.keys()))

        # --- COLUMN 3 ---
        with c3:
            st.markdown('<div class="section-header"> Lifestyle Factors</div>', unsafe_allow_html=True)
            st.write("") 
            smoke = st.toggle("Smoker")
            st.write("") 
            alco = st.toggle("Alcohol Intake")
            st.write("") 
            active = st.toggle("Physically Active", value=True)
            
            st.write("")
            st.info(f"ℹ️ Current Threshold: > {DECISION_THRESHOLD} indicates High Risk.")

        # Button is now GREEN via CSS
        submit_btn = st.form_submit_button("ANALYZE HEART HEALTH")

    if submit_btn:
        if model and scaler:
            with st.spinner("Processing Bio-markers..."):
                time.sleep(1.5) 

            # Prepare Data
            raw_input = {
                'gender': gender, 'age': age, 'height': height, 'weight': weight,
                'ap_hi': ap_hi, 'ap_lo': ap_lo,
                'cholesterol': chol_map[chol], 'gluc': gluc_map[gluc],
                'smoke': 1 if smoke else 0, 'alco': 1 if alco else 0, 'active': 1 if active else 0
            }
            
            df_processed, bmi_val = preprocess_input(raw_input)
            
            # BMI Status
            if bmi_val < 18.5: bmi_status = "Underweight"
            elif 18.5 <= bmi_val < 25: bmi_status = "Normal Weight"
            elif 25 <= bmi_val < 30: bmi_status = "Overweight"
            else: bmi_status = "Obese"

            try:
                # Predict
                input_scaled = scaler.transform(df_processed)
                probability = model.predict_proba(input_scaled)[0][1] # Float 0.0-1.0
                risk_pct = probability * 100 
                
                # --- DISPLAY SINGLE RESULTS ---
                st.write("")
                st.markdown("---")
                
                # --- UPDATED HEADER COLOR TO BLUE ---
                st.markdown("""
                    <h2 style="text-align: center; color: #00c6ff; margin-bottom: 30px; text-shadow: 0 0 10px rgba(0, 198, 255, 0.3); letter-spacing: 1px;">
                        📊 Diagnostic Analysis Results
                    </h2>
                """, unsafe_allow_html=True)
                
                r1, r2 = st.columns([1, 2])
                
                with r1:
                    st.markdown(f"""
                    <div style="background: #121212; border-radius: 15px; padding: 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); text-align: center; border: 1px solid #333; height: 100%; display: flex; flex-direction: column; justify-content: center;">
                        <div style="font-size: 40px; margin-bottom: 10px;">⚖️</div>
                        <p style="color:#00c6ff; font-size:16px; margin:0; font-weight:700; letter-spacing: 1px;">BODY MASS INDEX (BMI)</p>
                        <h1 style="color:#ffffff; font-size:54px; margin: 15px 0; font-weight: 800;">{bmi_val:.1f}</h1>
                        <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px; margin-top: 10px;">
                            <p style="color:#aaa; font-size:13px; margin:0;">Normal Range: 18.5 - 24.9</p>
                            <p style="color:#00c6ff; font-size:14px; margin:5px 0 0 0; font-weight: 600;">Status: {bmi_status}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with r2:
                    # THRESHOLD LOGIC (Decimal Comparison)
                    if probability > DECISION_THRESHOLD:
                        color = "#ff4b4b" # Red
                        status = "HIGH RISK DETECTED"
                        msg = f"Model probability ({probability:.3f}) exceeds the threshold of {DECISION_THRESHOLD}."
                        bg_col = "rgba(255, 75, 75, 0.1)"
                        gauge_bg = "#0a1128"
                    else:
                        color = "#00ff88" # Green
                        status = "LOW RISK PROFILE"
                        msg = f"Model probability ({probability:.3f}) is within the safe range (< {DECISION_THRESHOLD})."
                        bg_col = "rgba(0, 255, 136, 0.1)"
                        gauge_bg = "#0a1128"

                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = risk_pct,
                        # --- UPDATED TITLE COLOR TO BLUE #00c6ff ---
                        title = {'text': "Cardio Risk Probability", 'font': {'size': 22, 'color': '#00c6ff', 'weight': 700}},
                        number = {'font': {'color': 'white', 'size': 40}, 'suffix': "%"},
                        gauge = {
                            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
                            'bar': {'color': color},
                            'bgcolor': gauge_bg,
                            'borderwidth': 2,
                            'bordercolor': "#333",
                            'steps': [
                                {'range': [0, DECISION_THRESHOLD * 100], 'color': "rgba(0, 255, 136, 0.05)"},
                                {'range': [DECISION_THRESHOLD * 100, 100], 'color': "rgba(255, 75, 75, 0.05)"}
                            ],
                            # Threshold Line Logic
                            'threshold': {'line': {'color': "white", 'width': 4}, 'thickness': 0.75, 'value': DECISION_THRESHOLD * 100}
                        }
                    ))
                    fig.update_layout(height=260, margin=dict(l=20, r=20, t=60, b=20), paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"})
                    st.plotly_chart(fig, use_container_width=True)
                    
                    st.markdown(f"""
                    <div style="background-color: {bg_col}; border-left: 6px solid {color}; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                        <h3 style="color: {color}; margin:0; font-weight:700; letter-spacing: 0.5px;">{status}</h3>
                        <p style="margin: 8px 0 0 0; color: #ddd; font-size: 15px; line-height: 1.4;">{msg}</p>
                    </div>
                    """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Prediction Error: {e}")

# ==========================================
# TAB 2: BATCH PREDICTION
# ==========================================
with tab2:
    st.write("")
    st.markdown('<div class="section-header">📂 Batch Patient Processing</div>', unsafe_allow_html=True)
    st.info(f"Upload a CSV file. The system will use the current Decision Threshold of **{DECISION_THRESHOLD}**.")
    
    uploaded_file = st.file_uploader("Upload Patient Data (CSV)", type="csv")
    
    if uploaded_file is not None:
        try:
            df_batch = pd.read_csv(uploaded_file)
            st.write("Preview of Uploaded Data:")
            st.dataframe(df_batch.head())
            
            # Button is now GREEN via CSS
            if st.button("PROCESS BATCH DIAGNOSIS"):
                results = []
                with st.spinner("Analyzing Batch Data..."):
                    progress_bar = st.progress(0)
                    
                    for index, row in df_batch.iterrows():
                        processed_row_df, bmi_val = preprocess_input(row)
                        
                        input_scaled = scaler.transform(processed_row_df)
                        prob = model.predict_proba(input_scaled)[0][1]
                        
                        # Apply DYNAMIC THRESHOLD
                        risk_label = "HIGH RISK" if prob > DECISION_THRESHOLD else "LOW RISK"
                        
                        results.append({
                            'Patient_ID': index + 1,
                            'BMI': round(bmi_val, 1),
                            'Probability_Score': round(prob, 3),
                            'Diagnosis': risk_label
                        })
                        progress_bar.progress((index + 1) / len(df_batch))
                        
                result_df = pd.DataFrame(results)
                st.success("Batch Processing Complete!")
                
                def color_high_risk(val):
                    color = '#ff4b4b' if val == 'HIGH RISK' else '#00ff88'
                    return f'color: {color}; font-weight: bold'

                st.dataframe(result_df.style.map(color_high_risk, subset=['Diagnosis']))
                
                csv = result_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Diagnosis Report",
                    data=csv,
                    file_name='cardiovision_batch_results.csv',
                    mime='text/csv',
                )
                
        except Exception as e:
            st.error(f"Error processing batch file: {e}")