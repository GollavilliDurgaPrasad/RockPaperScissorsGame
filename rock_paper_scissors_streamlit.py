import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮")

st.title("✊ Rock 🧻 Paper ✂️ Scissors")

# Initialize scores in session state if not already present
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0

choices = ["Rock", "Paper", "Scissors"]
user_choice = st.radio("Choose your move:", choices, horizontal=True)

if st.button("Play"):
    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        st.session_state.user_score += 1
    else:
        result = "Computer wins!"
        st.session_state.computer_score += 1

    st.success(f"You chose **{user_choice}**, computer chose **{computer_choice}**.")
    st.markdown(f"### {result}")

st.markdown("---")
st.subheader("Game Score")
col1, col2 = st.columns(2)
col1.metric("👤 Your Score", st.session_state.user_score)
col2.metric("💻 Computer Score", st.session_state.computer_score)

# Reset button
if st.button("Reset Scores"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.success("Scores have been reset.")
