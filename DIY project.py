import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as components

st.title("🎮 Gamer Aim Trainer")
st.write("Click as many circles as you can!")

duration = st.selectbox("Game duration", [30, 60, 120])

game = """
<div style="background:#111827;color:white;padding:12px;border-radius:12px;text-align:center">
    <h3>Time: <span id="timer">30</span>s</h3>
    <h3>Score: <span id="score">0</span></h3>
    <div id="arena" style="height:400px;position:relative;background:#1f2937;overflow:hidden;border-radius:10px">
        <button id="target" style="position:absolute;width:45px;height:45px;border-radius:50%;background:#22c55e;border:0;left:40%;top:40%;cursor:pointer"></button>
    </div>
    <button id="start" style="margin:12px;padding:10px">Start Game</button>
    <h3 id="result"></h3>
</div>

<script>
let score = 0;
let seconds = __DURATION__;
let playing = false;
let timerID;

const arena = document.getElementById("arena");
const target = document.getElementById("target");

document.getElementById("start").onclick = function() {
    score = 0;
    seconds = __DURATION__;
    playing = true;
    this.disabled = true;
    document.getElementById("score").textContent = score;
    document.getElementById("result").textContent = "";
    target.style.display = "block";

    timerID = setInterval(function() {
        seconds--;
        document.getElementById("timer").textContent = seconds;

        if (seconds <= 0) {
            clearInterval(timerID);
            playing = false;
            target.style.display = "none";
            document.getElementById("start").disabled = false;
            document.getElementById("result").textContent =
                "Final Score: " + score;
        }
    }, 1000);
};

target.onclick = function() {
    if (!playing) return;

    score++;
    document.getElementById("score").textContent = score;

    const maxX = arena.clientWidth - target.offsetWidth;
    const maxY = arena.clientHeight - target.offsetHeight;

    target.style.left = Math.floor(Math.random() * maxX) + "px";
    target.style.top = Math.floor(Math.random() * maxY) + "px";
};
</script>
</div>
"""

components.html(
    game.replace("__DURATION__", str(duration)),
    height=510
)

st.subheader("📊 Performance Analysis")

score_input = st.number_input(
    "Enter your final score shown in the game",
    min_value=0,
    step=1
)

if st.button("Analyze Performance"):
    scores = np.array([score_input])

    df = pd.DataFrame({
        "Metric": ["Final Score"],
        "Value": [int(np.sum(scores))]
    })

    st.dataframe(df, hide_index=True)

    if score_input >= duration * 1.5:
        st.success("Excellent performance! ⚡")
    elif score_input >= duration:
        st.info("Good job! Keep practising. 🎯")
    else:
        st.warning("Keep training to improve your aim! 💪")
