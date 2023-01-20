# Project name : Google Playstore Apps Analysis & Visualization

## **About the project**
In this project, you will be working on a real-world dataset of the google play store, one of the most used applications for downloading android apps. This project aims on cleaning the dataset, analyze the given dataset, and mining informational quality insights. This project also involves visualizing the data to better and easily understand trends and different categories.

# **Project Description**
This project will help you understand how a real-world database is analyzed using SQL, how to get maximum available insights from the dataset, pre-process the data using python for a better upcoming performance, how a structured query language helps us retrieve useful information from the database, and visualize the data with the power bi tool.

# **Module 1: Pre-processing, Analyzing data using Python and SQL.**
In this module, you will query the dataset using structured query language to gain insights from the database. The problem statements to be solved will be provided to you and you need to provide the solution for the same using your logic. Different concepts of SQL will be used in this process such as aggregating the data, grouping the data, ordering the data, etc. Module 1 consists of subtasks which are as follows

# **Cleaning** **playstore_apps**
"""

#importing libraries

import numpy as np
import pandas as pd
from numpy import nan

# import playstore_app data set

app=pd.read_csv("playstore_apps.csv",index_col='App')

app.shape

# drop duplicate values

app.drop_duplicates(keep=False,inplace=True)

app.head()

app.info()

# checking for null values
app.isnull().sum()

# find Category is equal to 1.9 and drop that row
print(app[app['Category'] == '1.9'])

app.drop("Life Made WI-Fi Touchscreen Photo Frame",inplace=True)

print(app['Category'].unique())

# Add 0 in place of NAN value in Ratings
app["Rating"] = app["Rating"].replace(np.nan,0 )

# drop NAN values
app.dropna(inplace=True)

# rename Columns 
app=app.rename(columns={"Current Ver": "current_Ver","Android Ver":"Android_Ver","Last Updated":"Last_Updated","Content Rating":"Content_Rating"})

app.info()

app.shape

# exporting the cleaned data
app.to_csv("cleaned_apps_data.csv")

"""# **Cleaning playstore_reviews**"""

# read Playstore_reviews data
reviews=pd.read_csv("playstore_reviews.csv",index_col='App')

reviews.head()

reviews.shape

reviews.info()

# checking for null values
reviews.isnull().sum()

# drop NAN values
reviews.dropna(axis=0,inplace=True)

reviews.info()

# getting all columns
reviews.columns

# checking for null values again
reviews.isnull().sum()

# checking for unique values
print(reviews['Sentiment'].unique())

# checking for unique values 
print(reviews['Sentiment_Polarity'].unique())

# checking for unique values
print(reviews['Sentiment_Subjectivity'].unique())

# getting dimensions of dataset after performing data cleaning
reviews.shape

# exporting the cleaned data
reviews.to_csv("cleaned_reviews_data.csv")
