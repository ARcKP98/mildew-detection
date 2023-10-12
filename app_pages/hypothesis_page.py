import streamlit as st


def hypothesis_page_body():
    st.write('## Hypotheses')
    st.write('')
    st.info(
        f"* Cherry leaves that have been affected by mildew will "
        f"have white or gray powdery spots on the surface of the leaf with "
        f"some discoloration. \n"
        f"* Cherry leaves that have been affected by powdery mildew will also "
        f"have some discoloration on parts of the leaf(the stem, the edges, "
        f"the center, etc.) with deformity of the edges.")
    st.write('')
    st.write('## Validation')
    st.success(
        f"The image montage and the average image differences that were "
        f"generated supports the hypotheses as it shows that leaves "
        f"affected with powdery mildew do have white/gray regions/spots "
        f"with discoloration and deformity of the edges when compared "
        f"to healthy leaves."
    )
