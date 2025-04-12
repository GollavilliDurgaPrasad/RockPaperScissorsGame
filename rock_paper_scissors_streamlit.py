import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮")
st.title("✊ Rock 🧻 Paper ✂️ Scissors")

# Initialize session state
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'result' not in st.session_state:
    st.session_state.result = ""
if 'computer_choice' not in st.session_state:
    st.session_state.computer_choice = ""
if 'play_clicked' not in st.session_state:
    st.session_state.play_clicked = False

choices = ["Rock", "Paper", "Scissors"]

def clear_result():
    st.session_state.result = ""
    st.session_state.computer_choice = ""
    st.session_state.play_clicked = False

# Radio with on_change to clear previous result
user_choice = st.radio("Choose your move:", choices, horizontal=True, key="user_choice", on_change=clear_result)

# Game logic
def play_game():
    computer_choice = random.choice(choices)
    user_choice = st.session_state.user_choice
    st.session_state.computer_choice = computer_choice
    st.session_state.play_clicked = True

    if user_choice == computer_choice:
        st.session_state.result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.session_state.result = "You win!"
        st.session_state.user_score += 1
    else:
        st.session_state.result = "Computer wins!"
        st.session_state.computer_score += 1

# Play Button
if st.button("Play"):
    play_game()

# Show result only after Play is clicked
if st.session_state.play_clicked:
    st.success(f"You chose **{st.session_state.user_choice}**, computer chose **{st.session_state.computer_choice}**.")
    st.markdown(f"### {st.session_state.result}")

st.markdown("---")
st.subheader("Game Score")
col1, col2 = st.columns(2)
col1.metric("👤 Your Score", st.session_state.user_score)
col2.metric("💻 Computer Score", st.session_state.computer_score)

# Reset button
if st.button("Reset Scores"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    clear_result()
    st.success("Scores have been reset.")
