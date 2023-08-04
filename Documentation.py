import streamlit as st

def home_page():
    # Add the slide image at the top of the page
    st.image("Slide1.PNG", use_column_width=True)

    # Add the title of the app
    st.title("Welcome to My Streamlit App")
    st.write("This is the home page of the app.")

    # Add links to datasets
    #st.header("Dataset")
    st.markdown("""
       The Global Findex is the world’s most comprehensive database on financial inclusion. 
       It is also the only global demand-side data source allowing for global and 
       regional cross-country analysis to provide a rigorous and multidimensional picture of how adults save, 
       borrow, make payments, and manage financial risks.
    """)
    st.markdown("[Dataset](https://microdata.worldbank.org/index.php/catalog/4607/study-description)")
    st.markdown("[MetaData](https://microdata.worldbank.org/index.php/catalog/4607/data-dictionary)")
    
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
    st.image("Slide2.PNG", use_column_width=True)
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

