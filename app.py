import pandas as pd
import pickle
import streamlit as st
from sklearn.impute import SimpleImputer

import sklearn
print(sklearn.__version__)


st.set_page_config(page_title='From Data to Retention: An Analysis of Employee Attrition')

def load_data():
    data = pd.read_csv(
        "IBM_HR-Attrition.csv",
        encoding='ISO-8859-1'
    )
    return data


def introduction():
    data = load_data()

    st.title("From Data to Retention: An Analysis of Employee Attrition")

    st.markdown(
        """
        The IT-BPM industry has reported an average attrition rate of 30 to 40 percent in 2022, which increased by over 10 points over the previous year. 

        This presents a significant challenge to retain talented employees to ensure the constant growth and success of a company. 

        With an increased demand for services, different companies must find effective ways to mitigate attrition and keep their best employees engaged and motivated.

        """
    )

    st.subheader("Research Objectives")

    st.markdown(
        """
        1. Identify factors causing employee attrition and develop a model to prevent or mitigate it using data science techniques.
        2. Determine reasons that cause employee attrition and suggest helpful retention strategies.

        """
    )
    
    st.subheader("Methodology")

    st.markdown(
        """
        In order to achieve the research objectives, the project utilized a dataset from the IBM HR Analytics Employee Attrition & Performance case study, which had a sample size of 1,470 employees. Feature selection was performed on the dataset during exploratory data analysis to extract meaningful insights that could address the current circumstances in the company.

        """
    )
    
    with st.expander("View Data"):
        
        st.dataframe(data)
        st.caption("Source: IBM HR Analytics Employee Attrition & Performance")

    #################### END ####################



def viz_variables():
    st.title("Exploratory Data Analysis")

    st.markdown(
        """
        Through exploratory data analysis, valuable insight and observations were discovered, which can aid in identifying relations among different factors that contribute to attrition. By gaining a deeper understanding of the dataset, various hypotheses were generated, leading to meaningful insights and actionable conclusions that can aid in addressing and mitigating the issue of attrition within the organization.
        """
    )
    
    st.divider()


    st.subheader("Attrition Features")

    st.image("./assets/attrition-count.png")
    
    st.markdown(
        """
        To effectively identify the reasons for attrition, a set of features were carefully selected. As depicted in the figure above, maintaining a lower attrition rate that aligns with the specific circumstances of a company, such as size and culture, is crucial. Striking the right balance can help organizations achieve their goals and maximize their workforce.
        
        """
    )

    
    st.subheader("Demographic Variables")

    # Attrition-Gender EDA
    st.markdown("**▸ Gender**")
    
    st.image("./assets/attrition-gender.png")

    st.markdown(
        """
        The graph shows that there are more males employed than females, suggesting a male-dominated workplace. Female employees may feel undermined and discouraged when there’s a depiction of gender bias and discrimination, which may lead them to leave the company. Hence, it is essential to evaluate and address possible gender issues from time to time to promote a more inclusive workplace.
        """
    )

    # Attrition-Age EDA
    st.markdown("**▸ Age Profile**")
    
    st.image("./assets/attrition-age.png")

    st.markdown(
        """
        The graph shows that the majority of employees belongs to the Adult age range of 26-44, which is considered the prime working years. On the other hand, the number of employees in the Old Age group is relatively low, as they have surpassed the peak of their careers and are approaching retirement.

        Additionally, a general observation is that younger employees have a higher tendency to leave than older employees, as they are more inclined to seek career growth opportunities. Meanwhile, older employees tend to be more content with their current job and are only waiting for their retirement.

        """
    )

    # Attrition-JobLevel EDA
    st.markdown("**▸ Job Level**")
    
    st.image("./assets/attrition-job_level.png")

    st.markdown(
        """
        According to the graph, the majority of employees in the company hold entry-level positions, which exhibit the highest attrition rates. Typically, these positions are assigned to recent graduates or individuals with limited experience who possess the potential to contribute to the company's growth. Surprisingly, even middle-level positions, occupied by employees with valuable experience and expertise, experience significant attrition rates.
        """
    )

    # Attrition-MonthlyIncome EDA
    st.markdown("**▸ Monthly Income**")
    
    st.image("./assets/attrition-monthly_income.png")

    st.markdown(
        """
        The graph shows that employees with lower incomes tend to have a higher attrition rate, which suggests that income could be a significant factor in their decision to leave the company. In contrast, employees with higher incomes tend to have a lower attrition rate. These findings imply that low income must be a crucial driver of attrition among employees, as fair compensation is an essential component of job satisfaction.

        However, it's important to note that every company has its own criteria for determining employees' wages, which may depend on factors such as job type, position, or tenure, as well as the company's financial capacity. While higher pay often leads to greater job satisfaction, this isn't always the case. Nevertheless, it's the company’s responsibility to ensure that employees receive reasonable compensation for their work, and it's up to employees to perform and take their work seriously in return.
        
        """
    )

    st.subheader("Work-Related Factors")


    # Attrition-BusinessTravel EDA
    st.markdown("**▸ Business Travel**")
    
    st.image("./assets/attrition-business_travel.png")

    st.markdown(
        """
        This feature refers to the frequency of business travel that an employee undertakes for their job. This can include attending conferences, meeting clients, or collaborating with colleagues in other locations. 
        
        The graph analyzing this feature reveals that employees who rarely travel for work have the highest rate of attrition compared to those who travel more frequently. Surprisingly, employees who do not travel at all have relatively low rates of attrition.

        """
    )

    # Attrition-OverTime EDA
    st.markdown("**▸ Over Time**")
    
    st.image("./assets/attrition-overtime.png")

    st.markdown(
        """
        The graph clearly indicates that employees who work overtime are at a higher risk of leaving the company. This suggests that working overtime can significantly impact the attrition rate among employees. 
        
        The impact of overtime on employee satisfaction and productivity depends on whether it is voluntary or mandatory. Employees who choose to work overtime are likely to be motivated and productive, while those who are required to work overtime may experience negative effects such as stress and burnout.

        Therefore, it is important for employers to carefully consider the necessity of overtime and ensure that it is fairly compensated and balanced among employees. Additionally, employers should provide support and resources to help employees manage the potential negative effects of overtime, such as offering stress management programs or flexible work arrangements. This can help promote a positive work environment and reduce the likelihood of employee turnover due to overtime-related issues.
        """
    )

    # Attrition-WorkLifeBalance EDA
    st.markdown("**▸ Work-Life Balance**")
    
    st.image("./assets/attrition-work_life_balance.png")

    st.markdown(
        """
        The graph depicts that the majority of employees recorded having a good to better work-life balance, while those who had a poor work-life balance had a higher attrition rate. This suggests that work-life balance plays a crucial role in retaining employees.
        
        In connection to overtime, employees highly value their time inside and outside of work, especially in today's "millennial" era where work-life balance is highly emphasized. Studies show that work-life balance has a significant impact on job satisfaction and overall employee retention. Thus, it is essential to prioritize and maintain a healthy work-life balance by providing adequate breaks and setting clear boundaries between work and personal life. Additionally, implementing an efficient workflow can also help in achieving a better work-life balance for employees.

        """
    )
    
    st.info("*Attendance bot could be a useful tool for flexible time management, providing valuable information for employers to monitor attendance and promote transparency.*", icon='ℹ️')

    # Attrition-TrainingTimeLastYear EDA
    st.markdown("**▸ Training Times**")
    
    st.image("./assets/attrition-training_times_last_yr.png")

    st.markdown(
        """
        The graph provides insights on the number of trainings completed by employees in the previous year, with the majority completing 3-6 trainings. It is also noteworthy that employees who did not receive any training have a higher attrition rate. Based on the previous graph, this could possibly indicate that those who did not receive training are entry-level employees.
        
        Employee training and development programs are critical in human resource management and can significantly impact attrition rates in a company. These programs provide growth opportunities and resources for employees to enhance their skills and succeed in their careers. Therefore, it is essential to invest in employee training and development programs to improve employee retention and overall company success.

        """
    )

    st.info("*Employees who are encouraged to take training courses not only experience a positive impact on their job satisfaction, but also when they are properly compensated with a reasonable monthly income, they are more likely to stay committed and engaged in their work. Training opportunities can improve employees' skills and performance, while competitive compensation can help them feel valued and appreciated. Investing in employee training and paying a reasonable wage can work together to create a positive work environment, leading to higher job satisfaction and lower attrition rates.*")

    # Attrition-YearsAtCompany EDA
    st.markdown("**▸ Tenure**")
    
    st.image("./assets/attrition-years_at_company.png")

    st.markdown(
        """
        This feature indicates the duration of an employee's tenure with the company. According to the graph, a big portion of employees have worked for less than 10 years. Notably, employees with 0 to 5 years of service show a high attrition rate. 
        
        In 2022, an increase in short-term employees has been observed, particularly among younger workers who are seeking their desired career path. The reasons for such high attrition rates among short-tenured employees include dissatisfaction with their current roles, demands for higher compensation, and managerial issues. Therefore, it is crucial for the company to provide proper guidance and support to these employees to help them progress in their careers.

        """
    )

    st.subheader("Employee Satisfaction")

    # Attrition-EnvironmentSatisfaction EDA
    st.markdown("**▸ Environment Satisfaction**")
    
    st.image("./assets/attrition-environment_satisfaction.png")

    st.markdown(
        """
        This feature reflects the level of satisfaction among employees regarding their work environment. 
        
        Overall, there is a high level of satisfaction among the employees with their work environment. However, upon analyzing the attrition rate across different satisfaction levels, it becomes evident that employees with lower satisfaction levels with their work environment are more likely to leave the company. This finding highlights the importance of providing a positive and fulfilling work environment to reduce the possibility of attrition among employees. 
        
        Having a positive work environment is crucial for employee retention. When employees feel satisfied with their work environment, they tend to perform better, which can lead to increased productivity and better business outcomes. 
        
        To maintain a healthy workplace environment and positive work culture, it is essential to establish effective communication and conflict resolution strategies. Encouraging open communication and creating a culture of respect and inclusivity can help employees feel valued and supported. Additionally, addressing conflicts in a timely and effective manner can prevent them from escalating and damaging the work environment. By prioritizing a positive work environment, organizations can improve employee satisfaction, reduce attrition rates, and ultimately achieve better business results.

        """
    )

    # Attrition-JobSatisfaction EDA
    st.markdown("**▸ Job Satisfaction**")
    
    st.image("./assets/attrition-job_satisfaction.png")

    st.markdown(
        """
        This feature measures the level of employee satisfaction with their current job, and although there is generally a high level of satisfaction, those who are dissatisfied with their job are more likely to leave the company. Addressing any factors that contribute to low job satisfaction is crucial for employee retention.
        
        To further motivate employees and enhance job satisfaction, it is important to provide them with opportunities for learning and growth, recognize their hard work, make them feel valued and show that their contributions are significant to the company's success. By creating a positive and supportive work environment, employees are more likely to feel engaged and committed to their job, which in turn can lead to increased productivity and better business outcomes.
        """
    )

    #################### END ####################


def findings():
    st.title("Findings")


    #################### END ####################


def predictive_modeling():
    # Load the trained model
    model = pickle.load(open('model/model_gbm.pkl', 'rb'))

    # Load the column names used for training
    columns = pd.read_csv('model/training_cols.csv')['0'].tolist()

    def one_hot_encode_input(data, col_ohe):
        # One-hot encode the categorical features
        encoded_data = pd.get_dummies(data, columns=col_ohe)
        
        # Add any missing columns
        missing_cols = set(columns) - set(encoded_data.columns)
        for col in missing_cols:
            encoded_data[col] = 0

        
        # Reorder columns to match training data
        encoded_data = encoded_data[columns]
        
        return encoded_data


    st.title('Employee Attrition Prediction')
    st.markdown(
        """
        The attrition prediction model utilizes the Gradient Boosting algorithm and considers several factors to predict the likelihood of an employee's attrition. 
        
        To determine whether an employee is likely to leave, please provide the required information in the following feature fields:
        """
    )

    st.subheader("Demographics")
    Gender = st.radio("▸   ***Gender***", ["Male", "Female"])
    Age_Profile = st.radio("▸   ***Age***", ["Young Adult (18-25)", "Adult (26-44)", "Middle-age (45-59)", "Old age (60+)"])
    JobLevel = st.radio("▸   ***Current Position in the Company***", ["Entry-Level", "Junior", "Middle", "Senior", "Executive"])
    MonthlyIncome  = st.slider("▸   ***Monthly Income***", 1000, 19999, 1009)

    st.subheader("Work-Related Factors")
    BusinessTravel = st.radio("▸   ***How frequent does the employee travel for business?***", ["Rarely", "Frequently", "Non-Travel"])
    OverTime = st.radio("▸   ***Does the employee work overtime?***", ["No", "Yes"])
    WorkLifeBalance = st.radio("▸   ***Work-Life balance rating***", ["Bad", "Good", "Better", "Best"])
    TrainingTimesLastYear = st.radio("▸   ***Trainings sessions completed last year?***", ["None", "1-2", "3-4", "5-6", "7-8", "9-10", "More than 10"])
    YearsAtCompany  = st.slider("▸   ***Tenure of service***", 0, 40, 0)

    st.subheader("Employee Satisfaction")
    JobSatisfaction = st.radio("▸   ***Level of satisfaction with current job.***", ["Low", "Medium", "High", "Very High"])
    EnvironmentSatisfaction = st.radio("▸   ***Level of satisfaction with current work environment.***", ["Low", "Medium", "High", "Very High"])

    st.divider()


    Gender = 1 if Gender == "Male" else 0

    if Age_Profile == "Young Adult (18-25)":
        Age_Profile= 1
    elif Age_Profile == "Adult (26-44)":
        Age_Profile = 2
    elif Age_Profile == "Middle-age (45-59)":
        Age_Profile = 3
    else:
        Age_Profile = 4

    if JobLevel == "Entry-Level":
        JobLevel = 1
    elif JobLevel == "Junior":
        JobLevel = 2
    elif JobLevel == "Middle":
        JobLevel = 3
    elif JobLevel == "Senior":
        JobLevel = 4
    else:
        JobLevel = 5

    if BusinessTravel == "Rarely":
        BusinessTravel = 1
    elif BusinessTravel == "Frequently":
        BusinessTravel = 2
    else:
        BusinessTravel = 3

    OverTime = 1 if OverTime == "Yes" else 0

    if WorkLifeBalance == "Bad":
        WorkLifeBalance = 1
    elif WorkLifeBalance == "Good":
        WorkLifeBalance = 2
    elif WorkLifeBalance == "Better":
        WorkLifeBalance = 3
    else:
        WorkLifeBalance = 4

    if JobSatisfaction == "Low":
        JobSatisfaction = 1
    elif JobSatisfaction == "Medium":
        JobSatisfaction = 2
    elif JobSatisfaction == "High":
        JobSatisfaction = 3
    else:
        JobSatisfaction = 4

    if EnvironmentSatisfaction == "Low":
        EnvironmentSatisfaction = 1
    elif EnvironmentSatisfaction == "Medium":
        EnvironmentSatisfaction = 2
    elif EnvironmentSatisfaction == "High":
        EnvironmentSatisfaction = 3
    else:
        EnvironmentSatisfaction = 4


    if TrainingTimesLastYear == "None":
        TrainingTimesLastYear = 0
    elif TrainingTimesLastYear == "1-2":
        TrainingTimesLastYear = 1
    elif TrainingTimesLastYear == "3-4":
        TrainingTimesLastYear = 2
    elif TrainingTimesLastYear == "5-6":
        TrainingTimesLastYear = 3
    elif TrainingTimesLastYear == "7-8":
        TrainingTimesLastYear = 4
    elif TrainingTimesLastYear == "9-10":
        TrainingTimesLastYear = 5
    else:
        TrainingTimesLastYear = 6


    def predict_attrition():
        # Create a dictionary to store the user input
        user_input = {
        'Gender': Gender,
        'Age_Profile': Age_Profile,
        'JobLevel': JobLevel,
        'MonthlyIncome': MonthlyIncome,
        'BusinessTravel': BusinessTravel,
        'OverTime': OverTime,
        'WorkLifeBalance': WorkLifeBalance,
        'JobSatisfaction': JobSatisfaction,
        'EnvironmentSatisfaction': EnvironmentSatisfaction,
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'YearsAtCompany': YearsAtCompany
        }

        # Convert the user input into a Pandas DataFrame
        user_input_df = pd.DataFrame(user_input, index=[0])

        cols_to_encode = ['Age_Profile', 'BusinessTravel']

        # Check for missing values
        if user_input_df.isnull().values.any():
            st.write('Please fill in all the input fields.')
        else:
            # One-hot encode the categorical features in the user input
            encoded_user_input = one_hot_encode_input(user_input_df, cols_to_encode)

            #Impute any missing values
            imputer = SimpleImputer(strategy='median')
            user_input_imputed = imputer.fit_transform(encoded_user_input)

            # Make a prediction using the trained model
            prediction = model.predict(user_input_imputed)

            # Display the prediction
            if prediction[0]==0:
                st.success('Attrition: No')

                st.markdown(
                    """
                    No
                    """
                )
            else:
                st.error('Attrition: Yes')

                st.markdown(
                    """
                    Yes
                    """
                )

    st.subheader("Predict")
    if st.button('Predict'):
        predict_attrition()

    #################### END ####################


# def clustering():
#     st.title("Clustering")


list_of_pages = [
    "Introduction",
    "Exploratory Data Analysis",
    # "Clustering",
    "Findings",  
    "Predictive Modeling",
]

st.sidebar.title('💼 Main Menu')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Exploratory Data Analysis":
    viz_variables()

# elif selection == "Clustering":
#     clustering()

elif selection == "Findings":
    findings()

elif selection == "Predictive Modeling":
    predictive_modeling()