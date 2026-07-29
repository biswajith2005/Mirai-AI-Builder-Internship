import streamlit as st

import pandas as pd

import numpy as np

 

st.title("SPORTS ANALYTICS")

 

with st.sidebar:

    st.header("DASHBOARD CONTROLS")

    player=st.selectbox("SELECT PLAYER",["Virat Kohli","MS DHONI"])

    match_phase=st.slider("OVERS PLAYED",1,5,10)

 

st.subheader(f"LIVE STATS: {player}")

 

col1,col2= st.columns(2)

with col1:

    # METRICS

    runs=match_phase*7

    st.metric(label="TOTAL RUNS GIVEN BY BOWLERS",value=runs,delta="+7",delta_color="normal")

with col2:

    strike_rate=130+(match_phase*2)

    st.metric(label="STR",value=strike_rate, delta="+2",delta_color="inverse")

st.divider()
st.subheader("Run Rate")

char_data=pd.DataFrame(np.random.randn(5, 1),columns=["Runs per over"])

st.line_chart(char_data)


