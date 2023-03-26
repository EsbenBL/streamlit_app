from plot_europe import plot_europe
from plot_dk import plot_dk
import streamlit as st 

## Page Configs 
st.set_page_config(initial_sidebar_state="collapsed", page_title = "Unresolved Crime in San Francisco")

# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         </style>
#         """

# st.markdown(hide_menu_style, unsafe_allow_html=True)

## HTML Plot 
st.header("Map of Unresolved Crime Distributed by San Francisco Neighborhoods")

HtmlFile = open("Plot/SF_unresolved_crime.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
st.components.v1.html(source_code, height = 650, width = 1050)

# st.header("Kort over Europa og Danmark")

# st.write("Hvad vil du gerne se?")

# dk_button = st.button("Se Danmark tættere på?") 
# eu_button = st.button("Se Europa?") 

# if dk_button:
#     fig = plot_dk()
#     st.pyplot(fig)
#     st.button("Se Europa igen?")
#     st.write("Ovenfor ses et utroligt flot kort over Danmark!")
# elif eu_button:
#     fig = plot_europe()
#     st.pyplot(fig)
#     st.write("Ovenfor ses et utroligt flot kort over Europa, hvor Holland, Danmark og Sverige er fremhævet (GO ADC!)")