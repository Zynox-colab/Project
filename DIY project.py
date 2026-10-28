
import streamlit as st
import numpy as np
import pandas as pd

st.title("Gamer Reaction Test")
st.write("Test your clicking performance!")

if "scores" not in st.session_state:
    st.session_state.scores = []

score = st.number_input(
    "Enter your reaction time in milliseconds",
    min_value=1,
    value=300
)

if st.button("Record Score"):
    st.session_state.scores.append(score)
    st.success("Score recorded!")

if st.button("Show Results"):
    if st.session_state.scores:
        scores = np.array(st.session_state.scores)

        st.subheader("🏆 Your Results")
        st.write("Total Hits:", len(scores))
        st.write("Average Reaction Time:", round(np.mean(scores)), "ms")
        st.write("Best Reaction Time:", np.min(scores), "ms")

        df = pd.DataFrame({
            "Attempt": range(1, len(scores) + 1),
            "Reaction Time (ms)": scores
        })

        st.dataframe(df)
    else:
        st.warning("Record a score first!")

