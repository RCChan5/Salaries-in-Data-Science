import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st


################################Data stuff##########################################
df = pd.read_csv("data/Cleaned_Salaries.csv")
location_option = df["Job Location"].unique()
state_option = df["Job Title"].unique()
industry_option =df["Industry"].unique()


############################SIDE BAR################################################
# st.sidebar.success("Select a demo above.")

#list of job titles to use in new df  ##should i keep this as a single value or multi
option1 = st.sidebar.multiselect(
    'Job Location by state:',
    location_option)

### add a choice to ask how many rows they would ike to see

values = st.sidebar.slider(
    'Salary Range(K):',
    0, 300, (30,150 ))



#list of job titles to use in new df  ##should i keep this as a single value or multi
industry_option = st.sidebar.multiselect(
    'Industry:',
    industry_option)




degree_option = st.sidebar.multiselect(
    'Degree:',
    ["Masters","Bachelors","PHD"])

st.header("Data Science Jobs based on your filters:")

##############Filtering#############

if option1 != []:
    df=df.loc[df['Job Location'].isin(option1)]

if industry_option != []:
    df=df.loc[df['Industry'].isin(industry_option)]


df = df[df['Avg Salary(K)'].between(values[0], values[1])]

if degree_option != []:
    df=df.loc[df['Degree'].isin(degree_option)]





df2=df[["Job Title","Job Location","Avg Salary(K)","Industry","Degree","company_txt"]]
df2=df2.rename(columns={"company_txt":"Company Name"})


st.dataframe(df2, height=1000,use_container_width=True)

