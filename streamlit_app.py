# Alfredo Winston - 2702297776

import streamlit as st
import json
import requests

st.title('Machine Learning App')
st.info('This App for Checking Obesity Level')

# Input Data by User
Gender = st.selectbox('Gender', ['Male','Female'])
Age = st.slider('Age', min_value = 0, max_value = 99, value = 0)
Height = st.number_input('Height, Example: 1.73', min_value = 1.00, max_value = 2.00, value = 1.00)
Weight = st.number_input('Weight, Example: 76.84', min_value = 30.00, max_value = 150.00, value = 30.00)
family_history_with_overweight = st.selectbox('Family History with Overweight', ['yes','no'])
FAVC = st.selectbox('FAVC', ['yes','no'])
FCVC = st.number_input('FCVC, Example: 2.96', min_value = 0.00, max_value = 5.00, value = 0.00)
NCP = st.number_input('NCP, Example: 2.74', min_value = 0.00, max_value =5.00, value = 0.00)
CAEC = st.selectbox('CAEC', ['Sometimes','Frequently','Always','no'])
SMOKE = st.selectbox('SMOKE', ['yes','no'])
CH2O = st.number_input('CH2O, Example: 2.61', min_value = 0.00, max_value = 5.00, value = 0.00)
SCC = st.selectbox('SCC', ['yes','no'])
FAF = st.number_input('FAF, Example: 0.63', min_value = 0.00, max_value = 5.00, value = 0.00)
TUE = st.number_input('TUE, Example: 0.625', min_value = 0.00, max_value = 5.00, value = 0.00, step=0.001, format="%.3f")
CALC = st.selectbox('CALC', ['Sometimes','Frequently','Always','no'])
MTRANS = st.selectbox('MTRANS', ['Public_Transportation','Automobile','Walking','Motorbike','Bike'])

inputs = {
    'Gender': Gender,
    'Age': Age,
    'Height': Height,
    'Weight': Weight,
    'family_history_with_overweight': family_history_with_overweight,
    'FAVC': FAVC,
    'FCVC': FCVC,
    'NCP': NCP,
    'CAEC': CAEC,
    'SMOKE': SMOKE,
    'CH2O': CH2O,
    'SCC': SCC,
    'FAF': FAF,
    'TUE': TUE,
    'CALC': CALC,
    'MTRANS': MTRANS
}

if st.button('Predict'):
    res = requests.post(url="http://127.0.0.1:8000/predict", data=json.dumps(inputs))

    if res.status_code == 200:
        result = res.json()
        st.success(f"Prediction result: {result['prediction']}")
    else:
        st.error(f"Failed to get prediction: {res.status_code}")

    # st.subheader(f"Prediction result from API = {res.text}")