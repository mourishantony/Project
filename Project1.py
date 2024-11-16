import streamlit as st
import random
import time

# Page config
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎮",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
    }
    .game-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

def machine_guess(low, high, target):
    steps = 0
    while low <= high:
        steps += 1
        guess = (low + high) // 2
        if guess == target:
            return steps, guess
        elif guess < target:
            low = guess + 1
        else:
            high = guess - 1
    return steps, guess

def main():
    st.title("🎮 Ultimate Number Guessing Game")
    
    # Game mode selection
    game_mode = st.radio("Select Game Mode:", ["You Guess", "Machine Guesses"])
    
    if game_mode == "You Guess":
        st.markdown("<div class='game-container'>", unsafe_allow_html=True)
        if 'random_number' not in st.session_state:
            st.session_state.random_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.optimal_steps = len(bin(100)[2:])

        st.write("I'm thinking of a number between 1 and 100!")
        st.write(f"Can you guess it in {st.session_state.optimal_steps} steps or less? 🤔")
    
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="user_guess")
    
        if st.button("Submit Guess"):
            st.session_state.attempts += 1
        
            if guess == st.session_state.random_number:
                st.balloons()
                st.success(f"🎉 Congratulations! You found the number {st.session_state.random_number} in {st.session_state.attempts} attempts!")
                if st.session_state.attempts <= st.session_state.optimal_steps:
                    st.success("You did it optimally! 🌟")
                if st.button("Play Again"):
                    st.session_state.clear()
                    st.experimental_rerun()
            elif guess < st.session_state.random_number:
                st.warning("Your Guess is Too Low!!! ⬆️")
            elif guess > st.session_state.random_number:
                st.warning("Your Guess is Too High!!! ⬇️")
                
        st.write(f"Attempts so far: {st.session_state.attempts}")
        st.markdown("</div>", unsafe_allow_html=True)

    else:  # Machine Guesses
        st.markdown("<div class='game-container'>", unsafe_allow_html=True)
        st.write("Think of a number between 1 and 100!")
        
        if 'machine_game_started' not in st.session_state:
            st.session_state.machine_game_started = False
            st.session_state.low = 1
            st.session_state.high = 100
            st.session_state.machine_steps = 0
        
        if st.button("Start Machine Guessing"):
            st.session_state.machine_game_started = True
            
        if st.session_state.machine_game_started:
            guess = (st.session_state.low + st.session_state.high) // 2
            st.write(f"Is your number {guess}?")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("Too Low"):
                    st.session_state.low = guess + 1
                    st.session_state.machine_steps += 1
                    
            with col2:
                if st.button("Correct!"):
                    st.balloons()
                    st.success(f"Found your number in {st.session_state.machine_steps + 1} steps!")
                    if st.button("New Game"):
                        st.session_state.clear()
                        st.experimental_rerun()
                        
            with col3:
                if st.button("Too High"):
                    st.session_state.high = guess - 1
                    st.session_state.machine_steps += 1
                    
        st.write(f"Machine steps: {st.session_state.machine_steps}")
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()