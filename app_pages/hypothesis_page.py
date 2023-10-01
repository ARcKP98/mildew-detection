import streamlit as st


def hypothesis_page_body():
    st.write('## Hypothesis')
    st.write('')
    st.info(
        f"Cherry leaves that have been affected by mildew will "
        f"have white or gray powdery spots on the surface of the leaf with "
        f"some discoloration.")
    st.write('')
    st.write('## Validation')
    st.success(
        f"The image montage that was generated supports this hypothesis as it "
        f"shows that leaves affected with powdery mildew do have white/gray "
        f"spots with discoloration when compared to healthy leaves."
    )
