import streamlit as st
import requests

# 1. The Title and Description
st.set_page_config(page_title="Wine Sommelier AI", page_icon="🍷")
st.title("🍷 AI Wine Quality Sommelier")
st.write("Enter the chemical properties of the wine, and the AI will predict its quality score (0-10).")

# 2. The Input Form (Sidebar)
st.sidebar.header("Input Wine Details")

def user_input_features():
    # We use sliders for easy input
    alcohol = st.sidebar.slider('Alcohol %', 8.0, 15.0, 10.5)
    volatile_acidity = st.sidebar.slider('Volatile Acidity', 0.1, 1.6, 0.28)
    sulphates = st.sidebar.slider('Sulphates', 0.3, 2.0, 0.75)
    citric_acid = st.sidebar.slider('Citric Acid', 0.0, 1.0, 0.56)
    total_sulfur_dioxide = st.sidebar.slider('Total Sulfur Dioxide', 6.0, 300.0, 103.0)
    
    # These are less important features, so we can set defaults or let user type
    fixed_acidity = st.sidebar.number_input('Fixed Acidity', value=8.5)
    residual_sugar = st.sidebar.number_input('Residual Sugar', value=1.8)
    chlorides = st.sidebar.number_input('Chlorides', value=0.092)
    free_sulfur_dioxide = st.sidebar.number_input('Free Sulfur Dioxide', value=35.0)
    density = st.sidebar.number_input('Density', value=0.9969)
    pH = st.sidebar.number_input('pH', value=3.30)

    # Return the data as a dictionary (JSON format)
    data = {
        "fixed_acidity": fixed_acidity,
        "volatile_acidity": volatile_acidity,
        "citric_acid": citric_acid,
        "residual_sugar": residual_sugar,
        "chlorides": chlorides,
        "free_sulfur_dioxide": free_sulfur_dioxide,
        "total_sulfur_dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol
    }
    return data

# Get the input from the user
wine_data = user_input_features()

# 3. Display the User's Input (Summary)
st.subheader("Current Wine Profile")
st.json(wine_data)

# 4. The "Predict" Button
if st.button("🔍 Predict Quality"):
    
    # REPLACE THIS URL WITH YOUR ACTUAL AWS IP
    api_url = "http://ec2-100-26-141-71.compute-1.amazonaws.com/predict" 
    
    try:
        with st.spinner('Asking the AI Sommelier...'):
            # Send the data to your AWS Server
            response = requests.post(api_url, json=wine_data)
            
            # Read the result
            prediction = response.json()['predicted_quality']
            
            # 5. Show the Result with Style
            st.success(f"Predicted Quality Score: {prediction}")
            
            # Add some logic for fun
            if prediction > 6.5:
                st.balloons()
                st.write("🌟 **This is a Premium Wine!**")
            elif prediction < 5.0:
                st.write("🤢 **Probably Vinegar...**")
            else:
                st.write("😐 **Average Table Wine.**")
                
    except Exception as e:
        st.error(f"Error connecting to API: {e}")