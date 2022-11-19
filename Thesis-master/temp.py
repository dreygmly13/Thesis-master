import pickle
import streamlit as st
from streamlit_option_menu import option_menu

something_model = pickle.load(open('heart123.sav', 'rb'))

with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System', 
                           ['Run'],
                           icons = ['heart'],
                           default_index = 0)

if (selected == 'Run'):
    
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
        
    with col1:
        
        age = st.number_input('Age')
        
    with col1:
        
        cp = st.number_input('Chest pain level (0 - 3)')
        
    with col2:
        
        exang = st.number_input('Induced Angina (YES = 1, NO = 0)')
        
    with col2:
        
        thal = st.number_input('Thalassemia (3 - 0)')
        
    heart_diagnosis = 'IF THIS TEXT IS SHOWING PLEASE RE-INPUT YOUR DATA'
    
    if st.button('See Results'):
       A = something_model.predict([[age, cp, exang, thal]])
       if (A[0]==0):
            heart_diagnosis = ('I THINK YOU ARE FINE FOR NOW')
       else:
        heart_diagnosis = ('YOU SHOULD SEE A DOCTOR')
    st.success(heart_diagnosis)
    
        
    
   
   

