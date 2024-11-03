
import numpy as np
import streamlit as st
import pickle

loaded_model = pickle.load(open('logistic_model.sav', 'rb'))
def Feyti_predicta(information):
    information= np.asarray(information)
    #reshape the array to predict one row
    information_reshaped = information.reshape(1,-1)

    prediction = loaded_model.predict(information_reshaped)
    if (prediction[0] == 0):
        return "You have a 90% chance of not having a heart disease"
    else:
        return "You are 90% likely to have a heart disease"


def main():
    st.title("WELCOME TO FEYTICARE.")
    age = st.number_input("Age", min_value=0)
    sex = st.number_input("Sex", min_value=0, max_value=1)
    cp = st.number_input("CP", min_value=0)
    trestbps = st.number_input("Trestbps", min_value=0)
    chol = st.number_input("Chol", min_value=0)
    fbs = st.number_input("fbs", min_value=0)
    restecg = st.number_input("Restecg", min_value=0)
    thalach = st.number_input("Thalach", min_value=0)
    exang = st.number_input("exang", min_value=0)
    oldpeak = st.number_input("oldpeak", step=0.1)
    slope = st.number_input("slope", min_value=0)
    ca = st.number_input("CA", min_value=0)
    thal = st.number_input("Thal", min_value=0)
    
    data= ''
    if st.button('Send'):
        data = Feyti_predicta([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
        
    st.success(data)
       
if __name__ == '__main__':
    main()