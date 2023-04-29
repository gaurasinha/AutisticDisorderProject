# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:30:11 2023

@author: gsinha
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# temp = pd.read_csv("C:/Users/gsinha/Documents/test_5050.csv")
# datasets=[]

# for column in temp:
#     df=temp.copy()
#     if("Trp" in column):
        
#         df = df[['Patient',column]]
#         df1=df[df['Patient']==1]
#         df1 = df1.rename(columns={column:str(column+"-Patient")})
#         df1=df1.drop(columns=df1.columns[0],axis=1)
#         df2 =df[df['Patient']==0]
#         df2 = df2.rename(columns={'Patient': 'Control',column:str(column+"-Control")})
#         df2=df2.drop(columns=df2.columns[0],axis=1)
#         df2.reset_index(inplace = True)
#         datasets.append(df1)
#         datasets.append(df2)

# new_df = pd.concat(datasets, axis=1)
# new_df=new_df.drop

# # plt.rcParams["figure.figsize"] = [15, 7]
# # plt.rcParams["figure.autolayout"] = True
# sns.set_style('white')
# sns.boxplot(data=new_df, palette='flare')
# sns.despine()
# plt.show()
# Load data from CSV file
file_path = 'C:/Users/gsinha/Downloads/50v50_collated_data - Sheet3.csv'
temp = pd.read_csv(file_path)
for column in temp:
    df=temp.copy()
    if("Trp" in column):
        x= df[column]
        group = df['Patient']
        # Create color-coded box plot
        plt.boxplot([x[group==0].values, x[group==1].values], labels=['Control', 'Patient'], showfliers=False)
        plt.xlabel('Groups')
        plt.ylabel('Value')
        plt.title("Box Plot of "+ column+" (Patient vs Control)")
        plt.grid()
        plt.show()




# # Set the figure size
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True


# plt.boxplot(datasets)

# # # Plot the dataframe
# # for data in datasets:
# #     data=data.drop(columns=data.columns[0], axis=1)
# #     ax = data.plot(kind='box', title='boxplot')

# # Display the plot
# plt.show()