import streamlit as st
import pandas as pd
import graphviz


def systemview():

    st.write("#### System Architecture Diagram")
    # systemarch = pd.read_csv("reports/SystemArchitecture.csv")
    # st.write("SOI: catapultSystem")


    # subsystem = st.selectbox("Select Subsystem to view the architecture", systemarch["Subsystem"].unique())

    # subsetsystem = systemarch[systemarch["Subsystem"] == subsystem]

    subsystemdf = pd.read_csv("reports/Subsystems.csv")
    assembliesdf = pd.read_csv("reports/Assemblies.csv")
    componentsdf = pd.read_csv("reports/Components.csv")

    dot = graphviz.Digraph(
                comment='Hierarchy',  
                graph_attr={"height":"1000", "width":"1000", "rankdir":"LR"},
                strict=True
            )


    for index, row in subsystemdf.iterrows():
        soi = row["SOI"]
        subsystem = row["Subsystem"]

        if pd.notna(soi) and soi not in dot.body:
            dot.node(soi)

        if pd.notna(subsystem):
            if subsystem not in dot.body:
                dot.node(subsystem)
            if pd.notna(soi):
                dot.edge(soi, subsystem, label="has subsystem") 

        
    for index, row in assembliesdf.iterrows():
        soi = row["SOI"]
        subsystem = row["Subsystem"]
        assembly = row["Assembly"]

        if pd.notna(soi) and soi not in dot.body:
            dot.node(soi)

        if pd.notna(subsystem):
            if subsystem not in dot.body:
                dot.node(subsystem)
            if pd.notna(soi):
                dot.edge(soi, subsystem, label="has subsystem") 

        if pd.notna(assembly):
            if assembly not in dot.body:
                dot.node(assembly)
            if pd.notna(subsystem):
                dot.edge(subsystem, assembly, label="has assembly")

    for index, row in componentsdf.iterrows():
        soi = row["SOI"]
        subsystem = row["Subsystem"]
        assembly = row["Assembly"]
        component = row["Component"]

        if pd.notna(soi) and soi not in dot.body:
            dot.node(soi)

        if pd.notna(subsystem):
            if subsystem not in dot.body:
                dot.node(subsystem)
            if pd.notna(soi):
                dot.edge(soi, subsystem, label="has subsystem") 

        if pd.notna(assembly):
            if assembly not in dot.body:
                dot.node(assembly)
            if pd.notna(subsystem):
                dot.edge(subsystem, assembly, label="has assembly")

        if pd.notna(component):
            if component not in dot.body:
                dot.node(component)
            if pd.notna(assembly):
                dot.edge(assembly, component, label="has component")

    st.graphviz_chart(dot)


        

