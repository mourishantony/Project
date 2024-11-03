import streamlit as st
import math

# Function to display game instructions
def display_rules(mode):
    if mode == "User guessing":
        st.write("""
        **Rules for User Guessing Mode:**
        1. The computer will choose a number within a certain range.
        2. Your goal is to guess the number in as few attempts as possible.
        3. After each guess, you'll be told if your guess was too high or too low.
        4. Try to achieve the optimal number of attempts!

        **Optimal attempts**: Calculated using binary search for efficiency.
        """)
    elif mode == "Machine guessing":
        st.write("""
        **Rules for Machine Guessing Mode:**
        1. You think of a number within a certain range.
        2. The machine will try to guess your number, and you will provide feedback if it's too high or too low.
        3. The machine will use binary search to find your number quickly.
        """)
    st.write("---")


# Main Game Function
def play_guessing_game():
    st.title("Guessing Game")

    # Choose game mode
    mode = st.selectbox("Choose a game mode:", ["User guessing", "Machine guessing"])

    # Display rules based on mode
    display_rules(mode)

    # Set dynamic range inputs
    min_val = st.number_input("Enter the minimum value of the range:", value=1, step=1, key="min_val")
    max_val = st.number_input("Enter the maximum value of the range:", value=100, step=1, key="max_val")

    if mode == "User guessing":
        # Optimal attempts for user reference
        optimal_attempts = math.ceil(math.log2(max_val - min_val + 1))
        st.write(f"Optimal number of attempts: {optimal_attempts}")

        # Computer randomly selects a number
        import random
        if 'target' not in st.session_state:
            st.session_state.target = random.randint(min_val, max_val)
            st.session_state.attempts = 0

        # User input guess
        guess = st.number_input("Take a guess:", min_value=min_val, max_value=max_val, step=1, key="user_guess")
        st.session_state.attempts += 1

        # Feedback based on guess
        if guess < st.session_state.target:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.target:
            st.warning("Too high! Try again.")
        else:
            st.success(f"Correct! You've guessed the number {st.session_state.target} in {st.session_state.attempts} attempts.")
            if st.session_state.attempts <= optimal_attempts:
                st.write("Congratulations! You achieved the optimal attempt count!")
            else:
                st.write("Try again to reach the optimal attempt count.")
            st.session_state.target = random.randint(min_val, max_val)  # Reset for replay

    elif mode == "Machine guessing":
        # Initialize session state variables
        if 'guess' not in st.session_state:
            st.session_state.low = min_val
            st.session_state.high = max_val
            st.session_state.guess = (min_val + max_val) // 2
            st.session_state.machine_attempts = 0

        # Display machine's current guess
        st.write(f"Machine's guess: {st.session_state.guess}")
        feedback = st.radio("Is the guess too high, too low, or correct?", ("Too high", "Too low", "Correct"))

        # Process feedback for machine's binary search adjustment
        if feedback == "Too high":
            st.session_state.high = st.session_state.guess - 1
            st.session_state.machine_attempts += 1
        elif feedback == "Too low":
            st.session_state.low = st.session_state.guess + 1
            st.session_state.machine_attempts += 1

        # Update machine's guess
        if feedback != "Correct":
            st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

        # Display success message if machine guessed correctly
        if feedback == "Correct":
            st.success(f"The machine guessed your number in {st.session_state.machine_attempts} attempts!")
            # Reset for replay
            st.session_state.low = min_val
            st.session_state.high = max_val
            st.session_state.guess = (min_val + max_val) // 2
            st.session_state.machine_attempts = 0

# Run the main game function
play_guessing_game()
