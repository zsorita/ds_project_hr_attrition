import pandas as pd
import streamlit as st

st.set_page_config(page_title='HR Attrition')

def load_data():
    data = pd.read_csv(
        "IBM_HR-Attrition.csv",
        encoding='ISO-8859-1'
    )
    return data


def introduction():
    data = load_data()
    st.header("Dataset")
    
    with st.expander("View Data"):
        
        st.dataframe(data)
        st.caption("*Source: IBM")

    st.subheader("Attrition Rate")
    st.image("./assets/attrition-count.png")
    st.markdown(
        """
        
        """
    )

def viz_variables():
    st.title("Exploratory Data Analysis")
    
    st.header("Attrition Rates")
    st.markdown(
        """
        Desc
        """
    )


    # Attrition-Age EDA
    st.subheader("Age")
    
    st.image("./assets/attrition-age.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-Gender EDA
    st.subheader("Gender")
    
    st.image("./assets/attrition-gender.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-MaritalStatus EDA
    st.subheader("Marital Status")
    
    st.image("./assets/attrition-marital_status.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-Department EDA
    st.subheader("Department")
    
    st.image("./assets/attrition-department.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    st.subheader("Research & Development Department")
    
    st.image("./assets/attrition-department-job_role.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-EnvironmentSatisfaction EDA
    st.subheader("Environment Satisfaction")
    
    st.image("./assets/attrition-environment_satisfaction.png")

    st.markdown(
        """
        Lorem impsum
        """
    )
    
    # Attrition-JobSatisfaction EDA
    st.subheader("Job Satisfaction")
    
    st.image("./assets/attrition-job_satisfaction.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-BusinessTravel EDA
    st.subheader("Business Travel")
    
    st.image("./assets/attrition-business_travel.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-OverTime EDA
    st.subheader("Over Time")
    
    st.image("./assets/attrition-overtime.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-TotalWorkingYears EDA
    st.subheader("Total Working Years")
    
    st.image("./assets/attrition-total_working_years.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-YearsAtCompany EDA
    st.subheader("Years At Company")
    
    st.image("./assets/attrition-years_at_company.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-YearsInCurrentRole EDA
    st.subheader("Years in Current Role")
    
    st.image("./assets/attrition-years_current.png")

    st.markdown(
        """
        Lorem impsum
        """
    )

    # Attrition-MonthlyIncome EDA
    st.subheader("Monthly Income")
    
    st.image("./assets/attrition-monthly_income.png")

    st.markdown(
        """
        Lorem impsum
        """
    )


def clustering():
    st.title("Clustering")

def conclusion():
    st.title("Conclusion")


list_of_pages = [
    "Introduction",
    "Exploratory Data Analysis",
    "Clustering",
    "Conclusion"
]

st.sidebar.title(':scroll: Main Menu')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Exploratory Data Analysis":
    viz_variables()

elif selection == "Clustering":
    clustering()

elif selection == "Conclusion":
    conclusion()