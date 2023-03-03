# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:14:46 2023

@author: gsinha
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file = "C:/Users/gsinha/Downloads/ASD Biolog Project - Raw Data/ASD Biolog Project - Raw Data/50 ASD vs 50 Controls/50_vs_50_p_values.xlsx"


for i in range(8):
    temp = pd.read_excel(file,sheet_name="PM"+str(i+1))
    #print(temp.head)
    temp = temp.rename({"P value ": "p_value"},axis=1)
    #print(temp.columns)
    temp = temp[temp.p_value>0.5]
    temp=temp.nlargest(10,'p_value')
    temp = temp.drop(temp.columns[[0,4,5]], axis=1)
    temp = temp[temp.substrate != 'NegativeControl']
    #print(temp.columns)
    ax = temp.plot.bar(x='substrate',rot=90)
    ax.set_xlabel("Biomarkers")
    ax.set_ylabel("Absorption Rate")
    