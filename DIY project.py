import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="AIM MASTER", page_icon="🎯")

# CSS DESIGN
st.markdown("""
<style>
.stApp {
    background-color: #101827;
    color: white;
}
h1 {
    color: #38BDF8;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# SESSION VARIABLES
if "score" not in st.session_state:
    st.session_state.score = 0

if "playing" not in st.session_state:
    st.session_state.playing = False

if "target" not in st.session_state:
    st.session_state.target = 0

if "start" not in st.session_state:
    st.session_state.start = 0

if "reaction" not in st.session_state:
    st.session_state.reaction = []

if "history" not in st.session_state:
    st.session_state.history = []

if "duration" not in st.session_state:
    st.session_state.duration = 30

# TITLE
st.title("🎯 AIM MASTER")
st.write("### Test your aiming skills and reaction speed!")
st.write("---")

# GAME SETTINGS
if not st.session_state.playing:

    st.subheader("Game Settings")

    duration = st.selectbox(
        "Choose game duration",
        [15, 30, 60],
        index=1
    )

    if st.button("🚀 START GAME"):

        st.session_state.score = 0
        st.session_state.reaction = []
        st.session_state.duration = duration
        st.session_state.start = time.time()
        st.session_state.target = np.random.randint(0, 15)
        st.session_state.playing = True

        st.rerun()


# GAME FUNCTION
@st.fragment(run_every="200ms")
def play_game():

    if st.session_state.playing:

        elapsed = time.time() - st.session_state.start
        remaining = st.session_state.duration - elapsed

        # CHECK TIMER
        if remaining <= 0:

            st.session_state.playing = False

            st.session_state.history.append({
                "Score": st.session_state.score,
                "Speed": round(
                    st.session_state.score / st.session_state.duration, 2
                ),
                "Reaction Time": round(
                    np.mean(st.session_state.reaction) * 1000, 2
                ) if st.session_state.reaction else 0
            })

            st.rerun()

        # SHOW SCORE AND TIMER
        a, b, c = st.columns(3)

        a.metric("Time Left", f"{remaining:.1f} sec")
        b.metric("Score", st.session_state.score)
        c.metric(
            "Speed",
            f"{st.session_state.score / max(elapsed, 0.01):.2f} CPS"
        )

        st.progress(max(0.0, remaining / st.session_state.duration))

        st.subheader("Click the target!")

        # CREATE 15 BUTTONS
        for i in range(15):

            if i % 5 == 0:
                cols = st.columns(5)

            with cols[i % 5]:

                if i == st.session_state.target:

                    if st.button("🎯", key=f"target{i}",
                                 use_container_width=True):

                        current = time.time()

                        if current - st.session_state.start < st.session_state.duration:

                            reaction_time = (
                                current - st.session_state.start
                                if st.session_state.score == 0
                                else current - st.session_state.last_click
                            )

                            st.session_state.reaction.append(reaction_time)
                            st.session_state.score += 1
                            st.session_state.last_click = current

                            st.session_state.target = np.random.randint(0, 15)

                            st.rerun()

                else:
                    st.button(
                        " ",
                        key=f"empty{i}",
                        disabled=True,
                        use_container_width=True
                    )


play_game()


# RESULTS
if not st.session_state.playing and st.session_state.history:

    st.write("---")
    st.header("🏆 GAME RESULTS")

    result = st.session_state.history[-1]

    st.metric("Total Score", result["Score"])
    st.metric("Clicks Per Second", result["Speed"])
    st.metric("Average Reaction Time", str(result["Reaction Time"]) + " ms")

    # PERFORMANCE GRADE
    if result["Speed"] < 0.5:
        st.error("BAD - Keep Practising!")

    elif result["Speed"] < 1:
        st.warning("GOOD - You can improve!")

    elif result["Speed"] < 1.5:
        st.success("VERY GOOD!")

    else:
        st.success("EXCELLENT! 🏆")

    # GAME HISTORY
    st.subheader("📊 Game History")

    df = pd.DataFrame(st.session_state.history)

    st.dataframe(df, use_container_width=True)

    st.subheader("Performance Graph")
    st.line_chart(df["Score"])

    if st.button("🔄 PLAY AGAIN"):
        st.session_state.playing = False
        st.rerun()


# FOOTER
st.write("---")
st.caption("AIM MASTER | Made with Python, Streamlit, Pandas and NumPy")
