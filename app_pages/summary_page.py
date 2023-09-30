import streamlit as st


def summary_page_body():

    st.write('## Project Summary')
    st.write('')
    st.write(
        f"Mildew(also known as Powdery Mildew) is a form of fungus that"
        f"has a whitish appearance which"
        f"affect a wide range of plants where the leaves, stems, and flowers"
        f"as a result get white coating all over them. This is bad for the"
        f"plants as this can weaken the plant and lead to no fruit production."
    )
    st.write(
        f"This is an issue at Farmy & Foods where some of their cherry leaves"
        f"have been identified as having powdery mildew. To identify infected"
        f"leaves, an employee examines all the leaves and treats them if they"
        f"are infected which is very time consuming and unscalable.")

    st.write(
        f"Based on this, the IT department has proposed an Machine Learning"
        f"system(ML) to instantly identify whether a leaf is infected or not."
    )

    st.info(f"The dataset used for this project was provided by the company"
            f"which contained images(4208 total) of healthy leaves and"
            f"infected leaves which were used to create the ML system.")

    st.success(f"The Business requirements for this project are:\n"
               f"* The client is interested in conducting a study to visually "
               f"differentiate a cherry leaf that is healthy from one that "
               f"contains powdery mildew. \n"
               f"* The client is interested in predicting if a cherry leaf is "
               f"healthy or contains powdery mildew.")

    st.write(f"For more information, please visit and read the "
             f"[Project README file]("
             f"https://github.com/ARcKP98/"
             f"mildew-detection/blob/main/README.md)")
