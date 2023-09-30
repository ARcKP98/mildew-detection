import streamlit as st
from app_pages.multipage import MultiPage

# Page scripts
from app_pages.page_summary import summary_page_body

app = MultiPage(app_name='Mildew Detector')

# Add app pages
app.add_page('Project Summary', summary_page_body)

app.run()
