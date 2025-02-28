import streamlit as st

# from dashboard import  dashschedule, dashresults
# from requirements import dashreqs
# from architecture import sysarcfunc
# from teststrategy import teststrat
# from testfacility import testfacility

st.set_page_config(page_title="Catapult Dashboard", page_icon="🪂", layout="wide")

def main():

    st.header("☄️ Catapult Project Dashboard", divider="violet")

    TABS = ["Mission", "Functional Architecture", "System Architecture"]
    tabs = st.tabs(TABS)

    with tabs[0]:
        st.write("Mission")
    with tabs[1]:
        st.write("Functional Architecture")
    with tabs[2]:
        st.write("System Architecture")


if __name__ == "__main__":
    main()