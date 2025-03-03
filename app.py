import streamlit as st

from mission import missionview
from functional import functionalview
from system import systemview
from requirements import dashreqs

st.set_page_config(page_title="Catapult Dashboard", page_icon="🪂", layout="wide")

def main():

    st.header("☄️ Catapult Project Dashboard", divider="violet")

    TABS = ["Mission", "Functional Architecture", "System Logical Architecture", "Requirements"]
    tabs = st.tabs(TABS)

    with tabs[0]:
        missionview()
    with tabs[1]:
        functionalview()
    with tabs[2]:
        systemview()
    with tabs[3]:
        dashreqs()

if __name__ == "__main__":
    main()