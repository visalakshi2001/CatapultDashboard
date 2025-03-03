import streamlit as st
import pandas as pd


# ########## REQUIREMENTS VIEW FUNCTION
def dashreqs():
    st.subheader("Requirements Table", divider="orange")
    breakdown = pd.read_csv("reports/Requirements.csv")
    st.dataframe(breakdown, hide_index=True, use_container_width=True)