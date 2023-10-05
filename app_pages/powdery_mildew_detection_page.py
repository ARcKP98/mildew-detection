import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.ml.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def mildew_detector_body():
    st.write('## Powdery Mildew Detector')
    st.write('')
    st.success(
        f"Here we tackle the second business requirement which is: "
        f"\n * The client is interested in predicting if a cherry leaf is "
        f"healthy or contains powdery mildew.")
