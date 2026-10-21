import streamlit as st
import string

st.title("🔐 Password Strength Checker")
st.write(
    "Check your password strength"
)

st.info("Use sample passwords only. Do not enter your personal password.")

password = st.text_input(
    "Enter a sample password:",
    type="password",
    placeholder="Enter your test password"
)

if password:
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Contains an uppercase letter": any(
            char.isupper() for char in password
        ),
        "Contains a lowercase letter": any(
            char.islower() for char in password
        ),
        "Contains a number": any(
            char.isdigit() for char in password
        ),
        "Contains a special character": any(
            char in string.punctuation for char in password
        )
    }

    score = sum(checks.values())

    if score <= 2:
        strength = "Weak"
        color = "🔴"
    elif score <= 4:
        strength = "Moderate"
        color = "🟠"
    else:
        strength = "Strong"
        color = "🟢"

    st.subheader("📊 Password Strength Analysis")
    st.write(f"**Strength:** {color} {strength}")
    st.metric("Password Strength Score", f"{score}/5")

    st.write("**Strength Progress**")
    st.progress(score / 5)

    st.subheader("✅ Criteria Checklist")

    for criterion, passed in checks.items():
        if passed:
            st.write(f"✅ {criterion}")
        else:
            st.write(f"❌ {criterion}")

    st.subheader("💡 Suggestions")

    suggestions = []

    if not checks["At least 8 characters"]:
        suggestions.append(
            "Use at least 8 characters."
        )

    if not checks["Contains an uppercase letter"]:
        suggestions.append(
            "Add at least one uppercase letter (A-Z)."
        )

    if not checks["Contains a lowercase letter"]:
        suggestions.append(
            "Add at least one lowercase letter (a-z)."
        )

    if not checks["Contains a number"]:
        suggestions.append(
            "Include at least one number (0-9)."
        )

    if not checks["Contains a special character"]:
        suggestions.append(
            "Include a special character, such as @, #, or !."
        )

    if suggestions:
        for suggestion in suggestions:
            st.write(f"• {suggestion}")
    else:
        st.success(
            "Excellent! Your password meets all five criteria."
        )

else:
    st.caption(
        "Enter a sample password above to view your analysis."
    )
