import streamlit as st
import pandas as pd
import graphviz


def functionalview():

    functionalarch = pd.read_csv("reports/FunctionalArchitecture.csv")
    
    st.write("#### Mission Architecture Diagram")

    dot = graphviz.Digraph(comment='Hierarchy', strict=True, graph_attr={"rankdir":"LR"})

    for index, row in functionalarch.iterrows():
        # colums: SOI,SystemFunction,SubFunction,SubSubFunction

        soi = row["SOI"]
        sysfunc = row["SystemFunction"]
        subfunc = row["SubFunction"]
        subsubfunc = row["SubSubFunction"]


        if pd.notna(soi):
            dot.node(soi)

        if pd.notna(sysfunc):
            if sysfunc not in dot.body:
                dot.node(sysfunc)
            if pd.notna(soi):
                dot.edge(soi, sysfunc, label="has system function")
        
        if pd.notna(subfunc):
            if subfunc not in dot.body:
                dot.node(subfunc)
            if pd.notna(sysfunc):
                dot.edge(sysfunc, subfunc, label="has sub function")
        
        if pd.notna(subsubfunc):
            if subsubfunc not in dot.body:
                dot.node(subsubfunc)
            if pd.notna(subfunc):
                dot.edge(subfunc, subsubfunc, label="has sub sub function")

    st.graphviz_chart(dot, True)