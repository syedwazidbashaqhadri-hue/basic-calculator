from helpers import *
import streamlit as st

st.title("calculator of two numbers")


#n1=int(input('enter the first number:'))
n1=int(st.number_input("enter the first number:"))
#n2=int(input('enter the second number:'))
n2=int(st.number_input("enter the second number:"))

st.write("select the operation to do in the two numbers ")
st.write("type 1- multiplication")
st.write("type 2- addition")
st.write("type 3- subtraction")
st.write("type 4- power/exponentiation ")
st.write("type 5- division")
st.write("type 6- floor division")


#operator=int(input("enter the option of the above:")) 
operator=int(st.number_input("enter the option of the above:")) 

if operator==1:
    st.write(multiply(n1,n2))
elif operator==2:
    st.write(add(n1,n2))
elif operator==3:
    st.write(sub(n1,n2))
elif operator==4:
    st.write(power(n1,n2))
elif operator==5:
    st.write(divide(n1,n2))
elif operator==6:
    st.write(floor(n1,n2))
else:
    st.write("please select a valid option")