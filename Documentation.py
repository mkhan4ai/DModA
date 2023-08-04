import streamlit as st

def home_page():
    # Add the slide image at the top of the page
    st.image("Slide1.PNG", use_column_width=True)

    # Add the title of the app
    st.title("Welcome to My Streamlit App")
    st.write("This is the home page of the app.")

    # Add links to datasets
    st.header("Datasets")
    st.write("Here are some useful datasets:")
    st.markdown("[Dataset 1](https://example.com/dataset1)")
    st.markdown("[Dataset 2](https://example.com/dataset2)")
    
def about_page():
    st.title("About")
    st.write("This is the about page of the app.")
    
def insights_page():
    st.image("Slide3.PNG", use_column_width=True)
    st.title("Insights")
    st.write("This is the insights page of the app.")
    
def documentation_page():
    st.title("Documentation")
    st.write("This is the documentation page of the app.")
    
def code_page():
    st.title("Code")
    st.write("This is the code page of the app.")
    
# Create a function to switch pages based on user input
def main():
    st.sidebar.title("Navigation")
    pages = ["Home", "About", "Insights", "Documentation", "Code"]
    choice = st.sidebar.radio("Go to", pages)

    if choice == "Home":
        home_page()
    elif choice == "About":
        about_page()
    elif choice == "Insights":
        insights_page()
    elif choice == "Documentation":
        documentation_page()
    elif choice == "Code":
        code_page()

if __name__ == "__main__":
    main()

