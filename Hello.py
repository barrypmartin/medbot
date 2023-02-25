# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 08:52:58 2023

@author: barry
"""

import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Medbot! 👋 Your window to the future")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
         **👈 Select a demo from the sidebar** to see some examples
    of what Medbot can do!
    ### Want to learn more?
    - Check out [Morgan Valley Tech](https://www.morganvalleytech.com)
    - Talk to our [Live bot Bert](https://www.morganvalleytech.com)
    - Ask a question about tech [Brother of Bert](https://www.morganvalleytech.com)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)