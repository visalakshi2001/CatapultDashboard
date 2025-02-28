import streamlit as st
import pandas as pd
import graphviz


def missionview():

    missionarch = pd.read_csv("reports/MissionArchitecture.csv")
    
    st.write("#### Mission Architecture Diagram")

    dot = graphviz.Digraph(comment='Hierarchy', strict=True)

    for index, row in missionarch.iterrows():
        mission = row["Mission"]
        env = row["Env"]
        ent = row["MissionEntities"]

        if pd.notna(mission):
            dot.node(mission)

        if pd.notna(env):
            if env not in dot.body:
                dot.node(env)
            if pd.notna(mission):
                dot.edge(mission, env, label="has environment")
        
        if pd.notna(ent):
            if ent not in dot.body:
                dot.node(ent)
            if pd.notna(env):
                dot.edge(env, ent, label="has mission entity")  
    st.graphviz_chart(dot, True)