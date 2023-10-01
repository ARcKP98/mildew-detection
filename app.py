import streamlit as st
from app_pages.multipage import MultiPage

# Page scripts
from app_pages.summary_page import summary_page_body
from app_pages.hypothesis_page import hypothesis_page_body
from app_pages.leaf_visualizer_page import leaf_visualizer_body
from app_pages.powdery_mildew_detection_page import mildew_detector_body


app = MultiPage(app_name='Mildew Detector')

# Add app pages
app.add_page('Project Summary', summary_page_body)
app.add_page('Project Hypothesis', hypothesis_page_body)
app.add_page('Cherry Leaf visualizer', leaf_visualizer_body)
app.add_page('Mildew Detector for Cherry Leaves', mildew_detector_body)


app.run()
