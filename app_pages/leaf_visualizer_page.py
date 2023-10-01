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
    if st.checkbox('Image Montage'):
        st.info("To refresh the montage click on **Create Montage**")
        my_data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0)
        if st.button('Create Montage'):
            image_montage(
                dir_path=my_data_dir + '/validation',
                label_to_display=label_to_display,  nrows=8,
                ncols=3, figsize=(10, 25)
                )
        st.write('----')


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):

    labels = os.listdir(dir_path)
    if label_to_display in labels:
        images_list = os.listdir(dir_path+'/'+label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(f'Decrease nrow or ncols to create your montage.')
            print(f'There are {len(images_list)} in your subset.')
            print(f'You requested a montage with {nrows * ncols} spaces.')
            return

        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path+'/'+label_to_display+'/'+img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f'Width {img_shape[1]}px x Height {img_shape[0]}px')
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
