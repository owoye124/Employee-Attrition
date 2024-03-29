# Employee Attrition Prediction Project

This project aims to predict employee attrition within an organization using machine learning techniques. The goal is to develop a model that accurately identifies employees who are likely to leave the company, allowing proactive measures to be taken to mitigate attrition.

## Project Overview

The project utilizes a dataset containing various features related to employee performance, satisfaction, and tenure within the organization. The columns used for prediction are:

- Average Monthly Hours
- Satisfaction Level
- Last Evaluation
- Number of Projects
- Time Spent in Company
- Department
- Salary
- Left (Target Variable)

## Steps Taken

1. **Data Collection:** Obtained a dataset containing relevant features for predicting employee attrition.

2. **Data Preprocessing:** Conducted data preprocessing steps such as handling missing values, encoding categorical variables, and scaling numerical features.

3. **Exploratory Data Analysis (EDA):** Performed EDA to gain insights into the distribution of features, identify correlations, and understand patterns within the data.

4. **Feature Engineering:** Created new features or modified existing ones to improve model performance.

5. **Model Selection:** Evaluated several machine learning algorithms suitable for binary classification tasks and selected the most promising ones based on performance metrics.

6. **Model Training:** Trained the selected models on the dataset, fine-tuning hyperparameters where necessary.

7. **Model Evaluation:** Assessed the performance of trained models using appropriate evaluation metrics such as accuracy, precision, recall, and F1-score.

8. **Deployment:** Deployed the trained model using Streamlit, allowing users to input employee data and receive predictions on attrition likelihood.

## Achieving Optimal Solution

To achieve a high level of accuracy (95%) in predicting employee attrition, the following steps were crucial:

- **Feature Selection:** Identified the most relevant features contributing to attrition prediction through feature importance analysis or domain knowledge.

- **Model Tuning:** Fine-tuned hyperparameters of the chosen algorithms using techniques such as grid search or random search to optimize model performance.

- **Ensemble Methods:** Employed ensemble learning techniques like Random Forest or Gradient Boosting to combine predictions from multiple models, often resulting in improved accuracy.

- **Cross-Validation:** Utilized cross-validation techniques to ensure the model's generalization capability and mitigate overfitting.

## Deployment

The trained model is deployed using Streamlit, a platform for building interactive web applications. Users can access the deployed application [here](https://employeeattrition.streamlit.app/), where they can input employee data and receive predictions on attrition likelihood.

## Future Work

- Continuous Monitoring: Implement mechanisms for monitoring and updating the model with new data to maintain its accuracy over time.
- Incorporating External Data: Explore the integration of external data sources such as employee demographics or economic indicators to enhance prediction accuracy.
- Refinement of Features: Continuously refine feature engineering techniques to extract more meaningful information from the data.



