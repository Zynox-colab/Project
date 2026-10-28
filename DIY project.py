import streamlit as st
import numpy as np
import pandas as pd

st.title(" Gamer Reaction Test")
st.write("Click the circle as many times as you can!")

if "scores" not in st.session_state:
    st.session_state.scores = []

if "position" not in st.session_state:
    st.session_state.position = 50

if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.markdown(
    f"""
    <div style="text-align:center; padding:20px;">
        <a href="?hit={st.session_state.position}"
           style="display:inline-block; width:65px; height:65px;
           line-height:65px; border-radius:50%; background:#22c55e;
           color:white; text-decoration:none; font-size:25px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("Hit Circle"):
    st.session_state.scores.append(300)
    st.session_state.position = int(
        np.random.randint(1, 100)
    )
    st.rerun()

if st.button("Show Results"):
    st.session_state.game_over = True

if st.session_state.game_over:
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
        st.warning("Play the game first!")
