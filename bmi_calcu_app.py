import streamlit as st
st.set_page_config(page_title = "BMI CALCULATOR BY PIAIC255664", layout = "centered")

st.title(" BMI CALCULATOR BY PIAIC255664")
st.write("Enter your height and weight to calculate your Body Mass Index (BMI).")

user_name = st.text_input("Enter your Name:")

height = st.number_input("Enter your Hight in cm:", min_value=50.0, max_value=250.0, step=0.1)
weight = st.number_input("Enter your Weight in kg:", min_value=10.0, max_value=300.0, step=0.1)

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi,2)
def interpret_bmi(bmi):
    if bmi <18.5:
        return " your are falling under the category of Underweight 😟" 
    elif 18.5 <= bmi < 24.9:
        return " your are falling under the category of Normal weight 😊" 
    elif 25 <= bmi < 29.9:
        return " your are falling under the category of Overweight 😐" 
    else:
        return " your are falling under the category of Obesity 😟"
# ✅ Step 5: BMI Calculation Function
    
#def calculate_bmi(height_cm, weight_kg):
 #   height_m = height_cm / 100  # Convert cm to meters
  #  bmi = weight_kg / (height_m ** 2)
   # return round(bmi, 2)

# ✅# Step 6: Interpret the BMI
#def interpret_bmi(bmi):
#    if bmi < 18.5:
#        return "Underweight 😟"
#    elif 18.5 <= bmi < 24.9:
#        return "Normal weight 😊"
#    elif 25 <= bmi < 29.9:
#       return "Overweight 😐"
#    else:
 #       return "Obesity 😟"
if st.button("calculate BMI"):
    if height == 0 or weight == 0:
        st.error("please emter valid height and weight."    )
    
    else:
        bmi_result = calculate_bmi(height, weight)
        bmi_category = interpret_bmi(bmi_result)
        st.success(f" Mr. {user_name}, your BMI is: {bmi_result}")
        st.info(f"Mr. {user_name}, {bmi_category}")