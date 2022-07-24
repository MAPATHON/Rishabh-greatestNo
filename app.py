import streamlit as st

st.write("""
# largest among 3 given numbers App

This app predicts the credit card approval probablity
""")

a=st.number_input('Number_A')
b=st.number_input('Number_B')
c=st.number_input('Number_C')
if (a>b && a>c):
    greatest=st.write('A')
elif(b>c && b>a):
    greatest=st.write('B')
else(c>a && c>b):
    greatest=st.write('B')

print(greatest)
