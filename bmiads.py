
import streamlit as st

st.title("BMI Calculator with Bonus Offer")

name = st.text_input("Enter your name:")
height = st.number_input("Enter height (cm):", min_value=50.0, max_value=250.0)
weight = st.number_input("Enter weight (kg):", min_value=10.0, max_value=300.0)

def calculate_bmi(h, w):
    h_m = h / 100
    return round(w / (h_m ** 2), 2)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = calculate_bmi(height, weight)
        st.success(f"Hello {name}, your BMI is {bmi}!")
        
        # Adsterra Direct Link Offer
        adsterra_link = "https://www.effectiveratecpm.com/wt8ijqj84?key=9a748c4acdd52dc0a1dd7616e72d388c"
        st.markdown(f'''
            <a href="{adsterra_link}" target="_blank">
                <button style="background-color: #FF4B4B; color: white; padding: 10px 20px; border-radius: 10px;">
                    🔥 Special Health Offer - Click Here!
                </button>
            </a>
        ''', unsafe_allow_html=True)
