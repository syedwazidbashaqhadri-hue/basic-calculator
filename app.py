from helpers import *
import streamlit as st

st.title("calculator of two numbers")


#n1=int(input('enter the first number:'))
n1=int(st.number_input("enter the first number:"))
#n2=int(input('enter the second number:'))
n2=int(st.number_input("enter the second number:")
       
operator=st.selectbox("operation",["multiplication","addition","subtraction","power/exponentiation","division","floor division"]))

if operator=='multiplication':
    st.write(multiply(n1,n2))
elif operator=='addition':
    st.write(add(n1,n2))
elif operator=='subtraction':
    st.write(sub(n1,n2))
elif operator=='power/exponentiation':
    st.write(power(n1,n2))
elif operator=='division':
    st.write(divide(n1,n2))
elif operator=='floor division':
    st.write(floor(n1,n2))
else:
    st.write("please select a valid option")