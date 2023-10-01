import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def leaf_visualizer_body():

    st.write("## Cherry Leaf Visualiser")
    st.write('')
    st.success(
        f"Here we tackle the first business requirement which is: "
        f"\n * The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that "
        f"contains powdery mildew.")

    version = 'v1'
    if st.checkbox('Difference between Average and Variability image'):
        avg_powdery_mildew_leaf = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_healthy_leaf = plt.imread(
            f"outputs/{version}/avg_var_healthy.png")
        st.warning(
            f"Notice that the average and variability of images don't show "
            f"clear patterns that help us differentiate between healthy and "
            f"infected. If you look closely however, you will notice that "
            f"towards the center of the leaf, the infected leaf has a whitish "
            f"colour compared to the healthy leaf which is darker in the "
            f"center and towards the edges.")
        st.image(avg_powdery_mildew_leaf,
                 caption=f'Cherry Leaf infected with powdery mildew- Average '
                         f'and Variability')
        st.image(avg_healthy_leaf,
                 caption=f'Cherry Leaf healthy - Average '
                         f'and Variability')
        st.write('----')
    if st.checkbox('Difference between Average Healthy ' +
                   'and Average Powdery Mildew leaf'):
        diff_between_average = plt.imread(f'outputs/{version}/avg_diff.png')
        st.warning(
            f"Notice that it's not very clear to spot the difference but the "
            f"center of the image is darker due to the infected leaf which "
            f"are less bright due to the infection and the edges are white due"
            f" to the healthy leaves which are bright green in color."
        )
        st.image(diff_between_average,
                 caption='Difference between Average images')
        st.write('----')
