import streamlit as st

# Function to display the about me section with image upload
def about_me():
    st.header("About Me")
    st.image("profile.jpg", width=150)  # Placeholder for profile image
    st.write("""
    Hello! I'm **Mourish Antony.C**, a **Student**. I have a passion for **Coding**.
    I love to work on projects that involve **Fullstrack Development**.
    Feel free to connect with me!
    """)

# Function to display the projects section with expandable cards
def projects():
    st.header("Projects")
    project_data = [
        {"title": "Guessing Game","description": "User Guessing And Machine Guesiing", "link": "https://github.com/mourishantony/Project/blob/master/Project1.py"},
        
    ]

    for project in project_data:
        with st.expander(project["title"], expanded=False):
            st.write(project["description"])
            st.markdown(f"[View Project]({project['link']})")

# Function to display the skills section with progress bars
def skills():
    st.header("Skills")
    skills_data = {
        "Python": 90,
        "Data Analysis": 80,
        "Machine Learning": 70,
        "Web Development": 75,
        "Streamlit": 85
    }

    for skill, percentage in skills_data.items():
        st.write(f"{skill}: {percentage}%")
        st.progress(percentage / 100)

# Function to display the contact section
def contact():
    st.header("Contact Me")
    st.write("""
    You can reach me via:
    - Email: mourishantonyc@gmail.com
    - LinkedIn: https://www.linkedin.com/in/mourish-a-6b51b0301/
    - GitHub: https://github.com/mourishantony
    """)

# Main app function
def main():
    st.set_page_config(page_title="My Portfolio", layout="wide", initial_sidebar_state="expanded")
    st.title("Welcome to My Portfolio")

    # Sidebar navigation
    menu = ["About Me", "Projects", "Skills", "Contact"]
    choice = st.sidebar.selectbox("Select a section", menu)

    if choice == "About Me":
        about_me()
    elif choice == "Projects":
        projects()
    elif choice == "Skills":
        skills()
    elif choice == "Contact":
        contact()

# Run the app
if __name__ == '__main__':
    main()
