
"""
Created on Tue Feb 28 14:01:18 2023

@author: gsinha
"""

import pandas as pd
import os



path = input("Enter the path to 50vs50 folder: ")
# Example path: "C:/Users/gsinha/Downloads/ASD Biolog Project - Raw Data/ASD Biolog Project - Raw Data/50 ASD vs 50 Controls/"

    
    
# %%% Acquire File Paths
files = []

if os.path.isdir(path) == True:
    temp = os.listdir(path)
    for i in temp:
        if 'PM-' in i:
            files.append(path + i)

print(files) #checking if it picked all the files
