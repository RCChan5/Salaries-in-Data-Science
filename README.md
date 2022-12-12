# Salaries in Data Science
 
[Tableau Dashboard](https://public.tableau.com/app/profile/rosh3601/viz/SalariesinDataScience_16694182554330/Story1)
 
[Streamlit](https://rcchan5-salaries-in-data-scienc-salaries-in-data-science-4bdicp.streamlit.app/)
## About
This is a dataset found on [Kaggle](https://www.kaggle.com/datasets/nikhilbhathi/data-scientist-salary-us-glassdoor). This dataset was made by scrapping the job postings related to the position of 'Data Scientist' from www.glassdoor.com in USA, Selenium was used to scrap the data.
### Objective:
1. Find the salary distribution for each type of job in the field of Data Science.
2. Create a way to visualize filtered jobs on streamlit easily.
3. Using this data set implements a multiclass classification machine learning model.
 
 
## Data processing:
## [Link to notebook used for Cleaning and EDA](https://github.com/RCChan5/Salaries-in-Data-Science/blob/main/DS%20Salary%20EDA%20and%20potential%20Data%20Cleaning.ipynb)
### Steps taken when cleaning this data set and learning about it:
* Looked at the data types of each field.
* Checked for missing values.
* Checked for Nulls.
* Checked the cardinality of each point.
* Cleaned the Job Title Column.
* Cleaned the Degree Column.
* Cleaned the seniority_by_title Column.
* Converted the Multiple Skills from binary 1 or 0 to boolean true or false.
* Correlation matrix
* Quick chart of avg salary to the job title.
* One hot encoding was done for the data frame to convert categorical data for its use in random forest
### Key findings
* The balance of the skills data is very imbalanced
* The balance for degree level required is highly imbalanced: job listing for bachelor degrees is very few.
 
 
## Classifier using Random Forest
![](data/tree.png?raw=true)
The goal of this section is to try and classify the different types of jobs in data science based of their skills.

## Future Work
