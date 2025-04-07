import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# SESSION STATE: SIMULATED DATABASE
# ------------------------------
if "responses" not in st.session_state:
    st.session_state.responses = []

# ------------------------------
# SIMULATED RECOMMENDATION ENGINE
# ------------------------------
def get_recommendation(score):
    if score >= 4:
        return "You are performing excellently. Keep leveraging current practices."
    elif score >= 3:
        return "You are on the right track. Consider refining some strategies."
    elif score >= 2:
        return "Improvement needed. Explore templates or guided tools."
    else:
        return "Urgent attention required. Begin with foundational training."

# ------------------------------
# SELF-ASSESSMENT FORM (FRONT-END)
# ------------------------------
st.title("🧠 Self Assessment Survey")
st.markdown("Answer the following questions to assess your maturity in key areas.")

name = st.text_input("Your Name")

q1 = st.slider("1. I understand my role and responsibilities clearly.", 1, 5)
q2 = st.slider("2. My team collaborates effectively.", 1, 5)
q3 = st.slider("3. We consistently meet our deadlines.", 1, 5)
q4 = st.slider("4. I feel confident using our internal tools and systems.", 1, 5)
q5 = st.slider("5. We regularly reflect and improve our processes.", 1, 5)

if st.button("Submit Assessment"):
    if not name:
        st.warning("Please enter your name before submitting.")
    else:
        avg_score = round((q1 + q2 + q3 + q4 + q5) / 5, 2)
        recommendation = get_recommendation(avg_score)

        # Save to simulated DB (session)
        st.session_state.responses.append({
            "name": name,
            "q1": q1,
            "q2": q2,
            "q3": q3,
            "q4": q4,
            "q5": q5,
            "score": avg_score,
            "recommendation": recommendation
        })

        st.success("✅ Assessment Submitted!")
        st.write(f"**Average Score:** {avg_score}")
        st.info(f"**Recommendation:** {recommendation}")

# ------------------------------
# BACK-END: SHOW RESPONSES TABLE + CHART
# ------------------------------
st.markdown("---")
st.subheader("📊 Assessment Results Overview")

if st.session_state.responses:
    df = pd.DataFrame(st.session_state.responses)
    st.dataframe(df)

    # Score Distribution Chart
    fig, ax = plt.subplots()
    ax.hist(df['score'], bins=range(1, 7), edgecolor='black')
    ax.set_title("Assessment Score Distribution")
    ax.set_xlabel("Score")
    ax.set_ylabel("Number of Respondents")
    st.pyplot(fig)
else:
    st.info("No assessments submitted yet.")

