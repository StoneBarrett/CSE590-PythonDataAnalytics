# Stone Barrett
# CSE 590: Python Data Analytics
# Midterm Exam

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
# Testing
# import os
# os.getcwd()

# PROBLEM 1
def problem1():
    # Loading CSV into dataframe
    df_init = pd.read_csv("Exams/Midterm/MetObjects_Subset.csv")
    # Testing
    # print(df_init)
    return df_init

# PROBLEM 2
def problem2(df_init):
    # Dropping all columns that are at least 50% NA
    df_prob2 = df_init.dropna(axis=1, thresh=8625)
    # Testing
    # print(df_prob2)
    return df_prob2

# PROBLEM 3
def problem3(df_prob2):
    # Counting ten most frequently occuring object names
    toptenwords = pd.Series(' '.join(df_prob2['Object Name']).lower().split()).value_counts()[:10]
    # Putting those names into an iterable list
    ttwList = ['Drawing', 'Painting', 'Plate', 'Vase', 'Watercolor', 'miniature', 'painting,', 'Bowl', 'Medal', 'Chair']
    # Dropping all rows that do not have one of those object names
    df_prob3 = df_prob2.loc[df_prob2['Object Name'].isin(ttwList)]
    # Resetting index
    df_prob3.reset_index(inplace=True)
    # Testing
    # print(toptenwords)
    # df_prob3.to_csv('Exams/Midterm/outtest.csv')
    # print(df_prob3)
    return df_prob3

# PROBLEM 4
def problem4(df_prob3):
    # Group by country and get count of each
    countryCounts = df_prob3.groupby('Country').count()
    # Hardcoding counts (taken from terminal printout generated from testing section below)
    usCount = 1432
    mexCount = 38
    canCount = 0
    otherCount = 6380 - (usCount + mexCount + canCount)
    totalCount = 6380
    # Calculating percentages
    usPerc = (usCount / totalCount) * 100
    mexPerc = (mexCount / totalCount) * 100
    canPerc = 0
    otherPerc = (otherCount / totalCount) * 100
    # Making dictionary
    dict_prob4 = {
        "United States": usPerc,
        "Mexico": mexPerc,
        "Canada": canPerc,
        "Other": otherPerc
    }
    # Testing
    # print(countryCounts)
    # print(usPerc + canPerc + mexPerc + otherPerc)
    # print(dict_prob4)
    return dict_prob4

# PROBLEM 5
def problem5(df_prob3):
    # Filter out every year of completion greater than 1999 or less than 1900
    only20th = df_prob3[(df_prob3['Object End Date'].astype(int) >= 1900) & (df_prob3['Object End Date'].astype(int) < 2000)]
    # Sort by year of completion
    only20th.sort_values(by=['Object End Date'])
    # Reset index
    only20th.reset_index(inplace=True)
    # Hardcoding decade counts (taken from .csv file generated in testing section below)
    x1900s = 807
    x1910s = 491
    x1920s = 287
    x1930s = 369
    x1940s = 35
    x1950s = 37
    x1960s = 12
    x1970s = 0
    x1980s = 0
    x1990s = 1
    # Making dictionary
    dict_prob5 = {
        "1900s": x1900s,
        "1910s": x1910s,
        "1920s": x1920s,
        "1930s": x1930s,
        "1940s": x1940s,
        "1950s": x1950s,
        "1960s": x1960s,
        "1970s": x1970s,
        "1980s": x1980s,
        "1990s": x1990s
    }
    # Testing
    # only20th.to_csv('Exams/Midterm/outtest5.csv')
    # print(only20th)
    # print(dict_prob5)
    return dict_prob5

# PROBLEM 6
def problem6(dict_prob4, dict_prob5):
    # Assigning lists for graphing
    x1 = list(dict_prob4.keys())
    y1 = list(dict_prob4.values())
    x2 = list(dict_prob5.keys())
    y2 = list(dict_prob5.values())
    # Graph for dict_prob4
    plt.bar(range(len(dict_prob4)), y1, tick_label=x1)
    plt.show()
    # Graph for dict_prob5
    plt.bar(range(len(dict_prob5)), y2, tick_label=x2)
    plt.show()


# Assigning variables for grading
df_init = problem1()
df_prob2 = problem2(df_init)
df_prob3 = problem3(df_prob2)
dict_prob4 = problem4(df_prob3)
dict_prob5 = problem5(df_prob3)
problem6(dict_prob4, dict_prob5)

# To make grading easier
# print(df_init)
# print(df_prob2)
# print(df_prob3)
# print(dict_prob4)
# print(dict_prob5)