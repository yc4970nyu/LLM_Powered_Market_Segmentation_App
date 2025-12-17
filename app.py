import streamlit as st
from chain import generate_segmentation

st.title("Market Segmentation Generator")

business_name = st.text_input("Business Name")
description = st.text_area("Description")
competitors = st.text_area("Competitors")
segmentation_type = st.selectbox(
    "Segmentation Type",
    ("Geographic", "Demographic", "Psychographic", "Behavioral")
)

if st.button("Generate Segmentation"):
    if business_name and description and competitors and segmentation_type:
        with st.spinner("Generating segmentation..."):
            segmentation_result = generate_segmentation(
                business_name, description, competitors, segmentation_type
            )
            st.success("Segmentation generated successfully!")
            st.write(segmentation_result)
    else:
        st.error("Please fill in all fields.")


