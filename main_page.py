from plot_europe import plot_europe
from plot_dk import plot_dk
import streamlit as st 

st.set_page_config(initial_sidebar_state="collapsed", page_title = "Hej")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)

st.header("Kort over Europa og Danmark")

st.write("Hvad vil du gerne se?")

dk_button = st.button("Se Danmark tættere på?") 
eu_button = st.button("Se Europa?") 

if dk_button:
    fig = plot_dk()
    st.pyplot(fig)
    st.button("Se Europa igen?")
    st.write("Ovenfor ses et utroligt flot kort over Danmark!")
elif eu_button:
    fig = plot_europe()
    st.pyplot(fig)
    st.write("Ovenfor ses et utroligt flot kort over Europa, hvor Holland, Danmark og Sverige er fremhævet (GO ADC!)")

st.header("Ocean Tech i Danmark")

with open("Plot/network_test.html", "r") as file:
    html_file = file.read()

st.components.v1.html(html_file, height = 600)