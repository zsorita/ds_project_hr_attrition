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

    st.image("./assets/img/intro_img.png")

    st.caption("Source: *https://www.insureon.com/blog/what-is-an-employee*")

    st.markdown(
        """
        The IT-BPM industry has reported an average attrition rate of 30 to 40 percent in 2022, which increased by over 10 points over the previous year. 

        This presents a significant challenge to retain talented employees to ensure the constant growth and success of a company. 

        With an increased demand for services, different companies must find effective ways to mitigate attrition and keep their best employees engaged and motivated.

        """
    )


    st.subheader("Research Objectives")

    st.image("./assets/img/objectives_img.png")

    
    st.subheader("Methodology")

    st.markdown(
        """
        In order to achieve the research objectives, the project utilized a dataset from the IBM HR Analytics Employee Attrition & Performance case study, which had a sample size of 1,470 employees. Relevant features were selected from the dataset during exploratory data analysis to extract meaningful insights that could address the current circumstances in the company.

        """
    )
    
    with st.expander("View Data"):
        
        st.dataframe(data)
        st.caption("Source: IBM HR Analytics Employee Attrition & Performance")

    #################### END ####################



def viz_variables():
    st.title("Exploratory Data Analysis")

    st.info('Through exploratory data analysis, valuable insight and observations were discovered, which can aid in identifying relations among different factors that contribute to attrition. By gaining a deeper understanding of the dataset, various hypotheses were generated, leading to meaningful insights and actionable conclusions that can aid in addressing and mitigating the issue of attrition within the organization.')
    
    st.divider()


    st.subheader("Attrition Features")

    st.image("./assets/attrition-count.png")
    
    st.markdown(
        """
        To effectively identify the reasons for attrition, a set of features were carefully selected. As depicted in the figure above, maintaining a lower attrition rate that aligns with the specific circumstances of a company, such as size and culture, is crucial. Striking the right balance can help organizations achieve their goals and maximize their workforce.
        
        """
    )

    with st.container():

        tab1, tab2, tab3 = st.tabs(["**Demographic Variables**", "**Work-Related Factors**", "**Employee Satisfaction**"])

        # Demographic Variables
        with tab1:
            
            st.markdown("**▸ Gender**")

            st.image("./assets/attrition-gender.png")
            
            st.markdown(
                """
                According to the graph, there are more male employees than female employees, indicating that the workplace is  **male-dominated**. This is consistent with the current trend in the tech industry where men still hold a majority of the positions.        
                """
            )

            st.divider()

            # Attrition-Age EDA
            st.markdown("**▸ Age Profile**")

            st.image("./assets/attrition-age.png")

            st.markdown(
                """
                The graph shows that the majority of employees belong to the **Adult** group, which is considered the prime working years. The number of employees in the **Old Age** group is relatively low, as they have surpassed the peak of their careers and are approaching retirement. Notably, employees in the **Young Adult** have a high attrition rate of over 35 percent, despite their small number. 
                """
            )

            st.divider()

            # Attrition-JobLevel EDA
            st.markdown("**▸ Job Level**")
            
            st.image("./assets/attrition-job_level.png")

            st.caption("*This feature refers to the position of an employee according to the hierarchical structure of a company. It is often associated with the level of authority and responsibility that an employee has.*")

            st.markdown(
                """                    
                According to the graph, the majority of employees in the company hold **entry-level positions**, which depict the highest attrition rates. Typically, these positions are assigned to recent graduates or individuals with limited experience who possess the potential to contribute to the company's growth. Surprisingly, even **middle-level positions**, held by employees with valuable experience and expertise, experience significant attrition rates.

                """
            )

            st.divider()

            # Attrition-MonthlyIncome EDA
            st.markdown("**▸ Monthly Income**")
            
            st.image("./assets/attrition-monthly_income.png")
            
            st.markdown(
                """
                The graph shows that employees with **lower incomes** tend to have a higher attrition rate, which suggests that income could be a significant factor in their decision to leave the company. In contrast, employees with higher incomes tend to have a lower attrition rate. These findings imply that low income is a crucial driver of attrition among employees.

                """
            )
    
        # Work-Related Factors
        with tab2:

            # Attrition-BusinessTravel EDA
            st.markdown("**▸ Business Travel**")

            st.image("./assets/attrition-business_travel.png")

            st.caption("*This feature refers to the frequency of business travel that an employee undertakes for their job. This can include attending conferences, meeting clients, or collaborating with colleagues in other locations.*")

            st.markdown(
                """
                The graph shows that **employees who travel frequently for work** have the highest rate of attrition compared to those who travel rarely and those who do not travel at all.
                """
            )

            st.divider()

            # Attrition-OverTime EDA
            st.markdown("**▸ Over Time**")
            
            st.image("./assets/attrition-overtime.png")

            st.markdown(
                """
                The graph clearly indicates that **employees who work overtime** are at a higher risk of leaving the company. This suggests that working overtime can significantly impact the attrition rate among employees. Employees may choose to work overtime voluntarily or be required to do so. While those who opt for overtime may feel productive, it can have a negative impact on those who are obligated to work longer hours.
                """
            )

            st.divider()

            # Attrition-WorkLifeBalance EDA
            st.markdown("**▸ Work-Life Balance**")    

            st.image("./assets/attrition-work_life_balance.png")

            st.markdown(
                """
                The graph depicts that the majority of employees recorded having a **good to better work-life balance**, while those who had a poor work-life balance had a higher attrition rate. 

                """
            )

            st.divider()

            # Attrition-TrainingTimeLastYear EDA
            st.markdown("**▸ Training Times**")

            st.image("./assets/attrition-training_times_last_yr.png")

            st.markdown(
                """
                Insigts from the graph shows that the number of training completed by employees in the previous year, with the majority **completing 3-6 trainings**. It is also noteworthy that employees who did not receive any training have a higher attrition rate. Based on the previous graph, this could possibly indicate that those who did not receive training are entry-level employees.

                """
            )

            st.divider()

            # Attrition-YearsAtCompany EDA
            st.markdown("**▸ Tenure**")

            st.image("./assets/attrition-years_at_company.png")

            st.caption("*This feature indicates the duration of an employee's tenure with the company.*")

            st.markdown(
                """
                
                According to the graph, a significant portion of employees have worked for **less than 10 years**. Notably, employees with 0 to 5 years of service show a high attrition rate.

                """
            )
            
        # Employee Satisfaction
        with tab3:
            
            # Attrition-EnvironmentSatisfaction EDA
            st.markdown("**▸ Environment Satisfaction**")

            st.image("./assets/attrition-environment_satisfaction.png")

            st.caption("*This feature refers to the level of satisfaction among employees regarding their work environment*")

            st.markdown(
                """
                Overall, there is a high level of satisfaction among the employees with their work environment. However, upon analyzing the attrition rate across different satisfaction levels, it becomes evident that employees with lower satisfaction levels with their work environment are more likely to leave the company.
                
                Based from this representation, we can conclude that this feature is a significant factor of attrition decision among employees. This may include various factors, such as relationships with colleagues, management style and communication, job security. As well as compensation, benefits and industry trends.

                """
            )
            
            st.divider()

            # Attrition-JobSatisfaction EDA
            st.markdown("**▸ Job Satisfaction**")

            st.image("./assets/attrition-job_satisfaction.png")

            st.caption("*This feature refers to the level of employee satisfaction with their current job.*")

            st.markdown(
                """                    
                Although there is generally a high level of satisfaction among the employess, those dissatisfied with their job are more likely to leave the company. Addressing any factors that contribute to low job satisfaction is crucial for employee retention.
                """
            )

    #################### END ####################


def discussion():
    st.title("Findings and Conclusion")

    st.info('According to the EDA results, potential issues and reasons that may lead to employee attrition in Avyan were identified and must be addressed to prevent the loss of valuable talents and assets in the company.')

    st.divider()

    # Male dominance in the Tech Industry
    st.subheader("**▸ Male dominance in the Tech Industry**")
    
    st.markdown(
        """
        As the Tech industry is still primarily male-dominated, there can be instances of gender bias and discrimination, leading to females feeling undermined and discouraged in the field. With this being said, it is crucial to address these issues to promote an inclusive workplace. 
        
        However, there has been progress, with an increasing number of females joining the industry, as evident in Avyan, where more females are holding programming and coding roles.

        """
    )

    # Younger employees are more likely to leave for career growth opportunities
    st.subheader("**▸ Younger employees are more likely to leave for career growth opportunities**")
    
    st.markdown(
        """
        Avyan has a significant number of young employees (18-25 years old) who are more likely to leave their jobs for career growth opportunities. Dissatisfaction with current roles, demands for higher compensation, and managerial concerns can also contribute to their attrition. 
        
        To retain these young talents, Avyan must create an environment that fosters personal and professional growth, offering career growth opportunities and support. By doing so, Avyan can cultivate a positive workplace culture and prevent the loss of its talented young employees.

        """
    )

    # Anticipate attrition in all levels of the organizational hierarchy
    st.subheader("**▸ Anticipate attrition in all levels of the organizational hierarchy**")
    
    st.markdown(
        """
        While entry-level positions are often seen as a source of future talent for the company, retaining these employees can be a challenge due to competition among companies for the most skilled and talented individuals. To address this, companies can provide clear career paths, mentoring, and training programs to support the professional growth of their employees. It is also important for companies to recognize the potential costs of high turnover rates in entry-level positions and improve their hiring qualifications to reduce such losses.
        
        In addition, the attrition rate among middle-level employees should not be overlooked. These employees have gained valuable experience and expertise in their field, making them a valuable asset to the company. However, they may feel stagnant in their positions and seek better opportunities elsewhere. To retain middle-level employees, offering growth opportunities, increased compensation, and recognition for their contributions can be effective strategies.
        
        In conclusion, addressing attrition at all levels of the organizational hierarchy is essential for maintaining a stable and productive workforce. Companies must recognize the value of their employees and implement measures to retain them, such as providing growth opportunities and improving hiring qualifications.

        """
    )


    # Low income as a primary factor for attrition
    st.subheader("**▸ Low income as a primary factor for attrition**")
    
    st.markdown(
        """
        While it's true that every employee aspires for a higher income, fair and reasonable compensation is a more practical approach to address this concern. In other words, employees should be paid for their work and contributions to the company. It’s worth considering that each company has its own methods of determining wages, taking into account determinants such as job type, position, and tenure, as well as the financial capacity of the company.
        
        Beyond providing a practical source of income, the company can also offer additional incentives as a form of compensation, such as health benefits, assistance programs, meals and snacks, events and outings. Although higher pay or compensation often leads to greater job satisfaction, it's not always the case. Regardless, it's the company's responsibility to ensure that employees are compensated fairly for their work, and it's up to the employees to fulfill their responsibilities and take their work seriously in return.

        """
    )

    # Possible impact of frequent business travel on employee engagement and satisfaction
    st.subheader("**▸Possible impact of frequent business travel**")
    
    st.markdown(
        """
        Business travel can provide employees with professional growth and a change of environment. However, based on the data set, it appears that employees who travel frequently have a higher rate of attrition. In light of the pandemic and the past two years of online settings, many companies have adapted to virtual work environments, which eventually became the norm. 
        
        Avyan's current hybrid work setup suggests that travel may not be necessary for its employees. However, enhancing travel policy could increase employee engagement. Without travel opportunities, employees may feel disconnected and burnt out. Providing support for business travel, like adequate resources and communication channels, can reduce stress and promote a sense of connection with colleagues and reach a wider network. Alternatives for growth can also keep non-traveling employees motivated and engaged in their work.

        """
    )

    # Importance of work-life balance
    st.subheader("**▸ Importance of work-life balance**")
    
    st.markdown(
        """
        Work-life balance is highly emphasized in the current "millennial" era, and research indicates that it significantly affects job satisfaction and employee retention. To achieve this balance, it is crucial to establish clear boundaries between work and personal life and provide adequate breaks. Fortunately, Avyan's culture prioritizes employees' lives and rest outside of work and does not generally promote an overtime culture. The company employs an efficient and flexible workflow that allows employees to be productive during work hours and prioritize their rest and personal life outside of work.
        
        To improve attendance and manage time effectively, the attendance bot is a valuable tool that enables employers to track attendance and ensure employees are meeting their schedules and deadlines.

        """
    )

    # Conduct training programs for development
    st.subheader("**▸ Conduct training programs for development**")
    
    st.markdown(
        """
        Training programs provide employees with opportunities for growth and resources to improve their skills, which can help them succeed in their careers. Thus, investing in employee training and development programs is essential for improving employee retention and overall company success.
        
        When employees are encouraged to participate in training courses, they are likely to experience a positive impact on their job satisfaction. Such training opportunities can improve their skills and performance in their current roles. Furthermore, when employees are given opportunities to learn and develop, they become more engaged and committed to their work, leading to higher job satisfaction and lower attrition rates. Encouraging and investing in employee training can be a valuable tool for companies to retain talented individuals and improve overall productivity.

        """
    )

    # Maintaining an effective and conducive workplace
    st.subheader("**▸ Maintaining an effective and conducive workplace**")
    
    st.markdown(
        """
        When employees feel satisfied with their work environment, they tend to perform better, resulting in increased productivity and better business outcomes. Encouraging open communication and creating a culture of respect and inclusivity can help employees feel valued and supported, leading to a positive work culture. It is also essential to address conflicts in a timely and effective manner to prevent them from damaging the work environment. Prioritizing a positive work environment can help organizations improve employee satisfaction, reduce attrition rates, and achieve better business results.
        """
    )

    # Prioritize work environment and employee satisfaction
    st.subheader("**▸ Prioritize work environment and employee satisfaction**")
    
    st.markdown(
        """
        Creating a positive work environment is crucial in enhancing job satisfaction and motivating employees. When employees feel valued and supported through open communication, respect, inclusivity, and conflict resolution, they tend to perform better, resulting in increased productivity and better business outcomes. 
        
        Additionally, providing opportunities for learning and growth and recognizing employees' hard work can further enhance their job satisfaction, making them more engaged and committed to their job. By prioritizing a positive work environment and employee satisfaction, organizations can reduce attrition rates and ultimately achieve better business results.
        """
    )

    st.divider()

    st.header("Conclusion")

    st.info('From what I have observed during my short time as an intern, Avyan has already implemented great retention strategies and addressed some concerns, it is still crucial to take note of some potential reasons that may affect employee retention. By analyzing the data, some hypotheses were drawn, and intervention measures were suggested to nurture Avyan’s culture. The management has done a great job in establishing effective management techniques to maintain a positive workplace for employees, as long as their dignity is not compromised. \n\nHowever, as the industry becomes more competitive and dynamic, Avyan needs to continuously improve its strategies to remain relevant and competitive. Monitoring employee performance and ensuring job security are vital in keeping the employees engaged and motivated. \n\nIn conclusion, it is important for Avyan to stay consistent with its management techniques while continuously adapting to the changing industry landscape.')


    st.divider()

    # REFERENCES
    st.caption("References:")

    st.image("./assets/img/references_img.png")

    
    #################### END ####################


def predictive_model():
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
        Building the attrition prediction model involved training the model with an imbalanced dataset, which means one class is more dominant than the other. To overcome potential bias in predictions, the **Random Undersampling** technique was employed to balance the dataset. This involved randomly selecting and removing samples from the majority class until the distribution between classes became even. To further enhance the model's accuracy, the **Gradient Boosting** algorithm was utilized.

        The **SHAP (SHapley Additive exPlanations)** technique was utilized to calculate and represent feature importances for the Gradient Boosting Classifier model that was trained on the dataset. It was observed that the most contributing features were Tenure, Monthly Income, and whether or not the employee works overtime.
                
        """
    )

    st.warning("*This predictive model is designed specifically for the context of Avyan and is not intended for generic use across different organizations or industries. It is important to keep in mind the limitations of the model's generalizability and to exercise caution when attempting to apply its predictions or insights outside of the Avyan context.*", icon='⚠️')

    st.markdown(
        """   
        To determine whether an employee is likely to leave, please provide the required information in the following feature fields:
        """
    )


    st.subheader("Demographics")
    Gender = st.radio("▸   ***Gender***", ["Male", "Female"])
    Age_Profile = st.radio("▸   ***Age***", ["Young Adult (18-25)", "Adult (26-44)", "Middle-age (45-59)", "Old age (60+)"])
    JobLevel = st.radio("▸   ***Current Position in the Company***", ["Entry-Level", "Junior", "Middle", "Senior", "Executive"])
    MonthlyIncome = st.number_input(label="▸   ***Monthly Income***", min_value=1009, max_value=19999, value=1009, step=1)


    st.subheader("Work-Related Factors")
    BusinessTravel = st.radio("▸   ***How frequent does the employee travel for business?***", ["Rarely", "Frequently", "Non-Travel"])
    OverTime = st.radio("▸   ***Does the employee work overtime?***", ["No", "Yes"])
    WorkLifeBalance = st.radio("▸   ***Work-Life balance rating***", ["Bad", "Good", "Better", "Best"])
    TrainingTimesLastYear = st.radio("▸   ***Number of training completed last year***", ["None", "1-2", "3-4", "5-6", "7-8", "9-10", "More than 10"])
    YearsAtCompany = st.number_input(label="▸   ***Tenure of service***", min_value=0, max_value=40, value=0, step=1)


    st.subheader("Employee Satisfaction")
    JobSatisfaction = st.radio("▸   ***Level of satisfaction with current job.***", ["Low", "Medium", "High", "Very High"])
    EnvironmentSatisfaction = st.radio("▸   ***Level of satisfaction with current work environment.***", ["Low", "Medium", "High", "Very High"])


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
                st.success("Great news! The employee is likely to stay with the company.", icon="👍")
                st.markdown(
                    """
                        This is an opportunity to provide the employee with growth opportunities that can help them feel more engaged and committed to the company. 
                        
                        Consider offering training programs, mentorship, and other development opportunities to help the employee advance in their career.
                    """
                )


            else:
                st.error("Uh-oh, it looks like the employee may be at risk of leaving the company.", icon="⚠️")
                st.markdown(
                    """
                        There could be several factors that contribute to an employee's desire to leave the company. 
                        
                        One possible reason could be a lack of career growth opportunities. Consider providing the employee with a clear career path, mentorship, and training programs to help them see a future with the company. It is also important to assess their compensation and workload to ensure they are fair and reasonable. 
                        
                        Additionally, offering work-life balance and other incentives such as travel opportunities can help retain the employee.    
                    """
                )

    col1, col2, col3 = st.columns(3)

    with col1:
        pass
    with col3:
        pass
    with col2 :
        center_button = st.button('**Predict Employee Attrition**')
    
    st.divider()

    if center_button:
        predict_attrition()

    
    #################### END ####################


# def clustering():
#     st.title("Clustering")


list_of_pages = [
    "Introduction",
    "Exploratory Data Analysis",
    # "Clustering",
    "Discussion",  
    "Predictive Model",
]

st.sidebar.title('💼 Main Menu')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Exploratory Data Analysis":
    viz_variables()

# elif selection == "Clustering":
#     clustering()

elif selection == "Discussion":
    discussion()

elif selection == "Predictive Model":
    predictive_model()
