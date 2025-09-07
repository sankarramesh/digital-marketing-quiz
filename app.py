import streamlit as st
import re

# -----------------------
# Page setup
# -----------------------
st.set_page_config(page_title="Digital Marketing Quiz", page_icon="🧠")
st.title("🧠 Digital Marketing Quiz")
st.write("Answer the 5 questions below and hit **Submit** to see your score.")

# -----------------------
# Question bank
# -----------------------
mcqs = [
    (
        "q1",
        "What does SEO stand for?",
        [
            "Search Engine Optimization",
            "Social Engagement Optimization",
            "Search Engine Operation",
            "Site Experience Optimization",
        ],
        "Search Engine Optimization",
    ),
    (
        "q2",
        "Which metric is clicks divided by impressions?",
        [
            "Conversion Rate (CVR)",
            "Click-Through Rate (CTR)",
            "Cost Per Click (CPC)",
            "Bounce Rate",
        ],
        "Click-Through Rate (CTR)",
    ),
    (
        "q3",
        "In Google Analytics 4, which measurement model is used by default?",
        ["Session-based", "Event-based", "Pageview-based", "User-based"],
        "Event-based",
    ),
    (
        "q4",
        "Which of these is typically an example of owned media?",
        ["TV Commercial", "Influencer Post", "Display Ads", "Email Newsletter"],
        "Email Newsletter",
    ),
]

# Fill-in-the-blank question
text_q_id = "q5"
text_q_prompt = (
    "Fill in the blank: Testing two variants of a landing page to see which performs better is called ______."
)

# Acceptable answers for the fill-in (normalized)
ACCEPTED_TEXT_ANSWERS = {"abtesting", "abtest", "splittesting", "splittest"}

def normalize(s: str) -> str:
    """Lowercase and remove non-alphanumerics to make matching flexible."""
    return re.sub(r"[^a-z0-9]", "", s.strip().lower())

# -----------------------
# Quiz form (single submit)
# -----------------------
with st.form("quiz_form"):
    for qid, question, options, _ in mcqs:
        st.radio(question, options, key=qid)

    st.text_input(text_q_prompt, key=text_q_id, placeholder="Your answer")

    submitted = st.form_submit_button("Submit")

# -----------------------
# Evaluation + result
# -----------------------
if submitted:
    score = 0

    # Check MCQs
    for qid, _, _, correct_answer in mcqs:
        user_answer = st.session_state.get(qid)
        if user_answer == correct_answer:
            score += 1

    # Check fill-in
    text_ans = st.session_state.get(text_q_id, "")
    if normalize(text_ans) in ACCEPTED_TEXT_ANSWERS:
        score += 1

    # Show result
    st.subheader("Your Result")
    st.metric("Score", f"{score} / 5")

    # Celebration + congrats message at the bottom
    st.balloons()
    st.success(f"🎉 Congratulations! You scored **{score} / 5**.")
