import streamlit as st

st.header("Netværk over Ocean Technology Industries")

with open("Plot/network_test.html", "r") as file:
    html_file = file.read()

st.components.v1.html(html_file, height = 600)
