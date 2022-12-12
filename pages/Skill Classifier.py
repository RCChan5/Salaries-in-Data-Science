
# Pandas is used for data manipulation
import pandas as pd
import numpy as np
import streamlit as st

# Read in data and display first 5 rows
features = pd.read_csv("data/Cleaned_Salaries.csv")
features=features[["Job Title","Python","spark","aws","excel","sql","sas","keras","pytorch","scikit","tensor","hadoop","tableau","bi","flink","mongo","google_an"]]

# One-hot encode the data using pandas get_dummies
# features = pd.get_dummies(features,columns=["Job Title"])

features.loc[features["Job Title"] == "Data Scientist", "Job Title"] = 1
features.loc[features["Job Title"] == "Data Analyst", "Job Title"] = 2
features.loc[features["Job Title"] == "Data Engineer", "Job Title"] = 3
features.loc[features["Job Title"] == "Data Science Consultant", "Job Title"] = 4
features.loc[features["Job Title"] == "Data Science Director", "Job Title"] = 5
features.loc[features["Job Title"] == "Other", "Job Title"] = 6
features.loc[features["Job Title"] == "Data Science Manager", "Job Title"] = 7
features.loc[features["Job Title"] == "Data Architect", "Job Title"] = 8



# Labels are the values we want to predict
labels = np.array(features['Job Title'])
#['Job Title Analyst','Job Title_Architect','Job Title_Data Engineer','Job Title_Data Science Consultant','Job Title_Data Science Director','Job Title_Data Science Manager','Job Title_Data Scientist','Job Title_Other']
# Remove the labels from the features
# axis 1 refers to the columns
features= features.drop('Job Title', axis = 1)
# Saving feature names for later use
feature_list = list(features.columns)
# Convert to numpy array
features = np.array(features)

# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)




# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(train_features, train_labels);

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)




# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)



st.header("What Job best fits your skill set")
st.write("#### Using Random Forest to try and classify what type of Job best fits your skillset.")


st.image("data/tree.png")
with open("data/tree.png", "rb") as file:
    btn = st.download_button(
            label="Download Tree image",
            data=file,
            file_name="data/tree.png",
            mime="image/png"
          )

#user_Input=[["Python","spark","aws","excel","excel","sql","sas","keras","pytorch","scikit","tensor","tableau","bi","flink","mongo","google_an"]]






############################SIDE BAR################################################
options = st.sidebar.multiselect(
    'What Skills do you know? Select all that may apply.',
    ("Python","spark","aws","excel","sql","sas","keras","pytorch","scikit","tensor","hadoop","tableau","bi","flink","mongo","google_an"),("Python"))
#st.write('You selected:', options)
############################MAIN PAGE################################################

x=[]
if "Python" in options:
    x.append(1)
else:
    x.append(0)
if "spark" in options:
    x.append(1)
else:
    x.append(0)
if "aws" in options:
    x.append(1)
else:
    x.append(0)
if "excel" in options:
    x.append(1)
else:
    x.append(0)    
if "sql" in options:
    x.append(1)
else:
    x.append(0)
if "sas" in options:
    x.append(1)
else:
    x.append(0)
if "keras" in options:
    x.append(1)
else:
    x.append(0)
if "pytorch" in options:
    x.append(1)
else:
    x.append(0)
if "scikit" in options:
    x.append(1)
else:
    x.append(0)
if "tensor" in options:
    x.append(1)
else:
    x.append(0)
if "hadoop" in options:
    x.append(1)
else:
    x.append(0)
if "tableau" in options:
    x.append(1)
else:
    x.append(0)
if "bi" in options:
    x.append(1)
else:
    x.append(0)
if "flink" in options:
    x.append(1)
else:
    x.append(0)
if "mongo" in options:
    x.append(1)
else:
    x.append(0)
if "google_an" in options:
    x.append(1)
else:
    x.append(0)


tab1, tab2 = st.tabs(["Job Classification", "Model Performance"])

with tab1:
    
    st.write("### Fill out the multi-select box on the left and see that classification below:")
    try:
        x11=[x]
        results=rf.predict(x11)
        results1=round(results[0])
        

    except:
        print("critical error1")
    st.write("## With these skills: "+str(options))
    if results1 == 1:
        st.write("## Your skillset belongs to a: Data Scientist")
    if results1 == 2:
        st.write("## Your skillset belongs to a: Data Analyst")
    if results1 == 3:
        st.write("## Your skillset belongs to a: Data Engineer")
    if results1 == 4:
        st.write("## Your skillset belongs to a:  Data Science Consultant")
    if results1 == 5:
        st.write("## Your skillset belongs to a:  Data Science Director")
    if results1 == 6:
        st.write("## Your skillset belongs to a:  Other specialty field")
    if results1 == 7:
        st.write("## Your skillset belongs to a:  Data Science Manager")
    if results1 == 8:
        st.write("## Your skillset belongs to a:  Data Architect")
        



with tab2:
    st.header("Model Performance")
    st.write('Training Features Shape:', train_features.shape)
    st.write('Training Labels Shape:', train_labels.shape)
    st.write('Testing Features Shape:', test_features.shape)
    st.write('Testing Labels Shape:', test_labels.shape)
    st.write('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
    st.write('Accuracy:', round(accuracy, 2), '%.')
    st.write("With a model accuracy rate of 40% I would suggest further tunning of the random forest model. This could be achieved with more data, Feature processing, or Model parameter tuning.")
