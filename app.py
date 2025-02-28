import streamlit as st

from mission import missionview
from functional import functionalview

st.set_page_config(page_title="Catapult Dashboard", page_icon="🪂", layout="wide")

def main():

    st.header("☄️ Catapult Project Dashboard", divider="violet")

    TABS = ["Mission", "Functional Architecture", "System Architecture"]
    tabs = st.tabs(TABS)

    with tabs[0]:
        missionview()
    with tabs[1]:
        functionalview()
    with tabs[2]:
        st.write("System Architecture")


if __name__ == "__main__":
    main()