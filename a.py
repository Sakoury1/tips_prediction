import streamlit as st
from p import *
st.title("Tips Predict App 👋")

with st.sidebar:
    st.title("Hello Friends 👋")
    image_path ="img.jpg"
    st.image(image_path, caption="This is an example image")
    st.info("This Model Predict Tips of Employee Using Liner Regression")

c1,c2=st.columns(2)

with c1:
    total_bill=st.number_input("Enter total_bill",0,90,step=2)
    size=st.number_input("Enter size",0,5,step=1)
    sex = st.selectbox("👩‍💼(Enter Your Sex)", ["Male", "Female"])
    
    
with c2:
    smoker = st.selectbox("🚬(Are you Smoker)", ["Yes", "No"])
    day = st.selectbox("📅(Day)", ["Thur", "Fri", "Sat", "Sun"])
    time = st.selectbox("🌙 (Time of meal)", ["Lunch", "Dinner"])

input_data = pd.DataFrame([[total_bill, size, sex, smoker, day, time]], 
                          columns=["total_bill", "size", "sex", "smoker", "day", "time"])
input_data = pd.get_dummies(input_data, drop_first=True)

for col in saved_columns:
    if col not in input_data.columns:
        input_data[col] = 0  

input_data = input_data[saved_columns]

btn=st.button("Predict")

if btn:
    prediction = model.predict(input_data)
    st.success(f"💰 Tips = {prediction[0]:.2f} ")

