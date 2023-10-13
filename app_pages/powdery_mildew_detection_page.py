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
    st.write('')
    st.write('You can upload image(s) of cherry leaves below')
    st.write(
        f'To access images of cherry leaves, you can use [this]'
        f'(https://www.kaggle.com/datasets/codeinstitute/cherry-leaves/data)'
        f' Kaggle folder to download images.')

    images_buffer = st.file_uploader(
        'Upload your cherry leaves here:', accept_multiple_files=True,
        type=['png', 'jpeg'])

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:
            img_pil = (Image.open(image))
            st.info(f'Cherry leaf sample: **{image.name}**')
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x"
                f"{img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append(
                {'Name': image.name, 'Result': pred_class}, ignore_index=True)

        if not df_report.empty:
            st.success('Analysis report')
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)
