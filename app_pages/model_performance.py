import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.ml.evaluate_clf import load_test_evaluation


def model_performance_metrics():
    '''
    Display the model performance
    '''

    version = 'v1'
    st.write('## Train, Test, and Validation Set: Labels Frequencies')
    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels on Train, Test, and Validation sets')
    st.write(f"The graph above shows that all sets are balanced as they all "
             f"contain the same amount of healthy and infected leaves. ")
    st.write('---')

    st.write('## Model history')
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(
            f"outputs/{version}/model_training_accuracy.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(
            f"outputs/{version}/model_training_accuracy.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write(f'The above graphs shows that the model has learned normally '
             f'(no overfitting or underfitting) because both loss and '
             f'accuracy plots follow a '
             f'similar path and are close to each other.')
    st.write('---')
    st.write('## Generalised Performance on Test set')
    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))
    st.info(f'This model has an accuracy of 99.53% on average which meets the '
            f'business performance criteria of 97% accuracy on predictions. ')
    st.success(f'A high accuracy value and a low loss value show that the '
               f'model is performing well and can be implemented to predict '
               f'the condition of a given cherry leaf.')
