# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:34:18 2022

The Nigerian Electricity Supply Market consists of 11 Distribution companies. 
I am analysing their 
revenue collection for the first half of the year 2022


@author: Omoregbe Olotu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing revenue collection data for all distribution companies from excel

input_file = r'C:\Users\matah\Downloads\ELECTRICIY DATA 2015-Q2 2022.xlsx'

data = pd.read_excel(input_file, 0, skiprows = 50, skipfooter = 16,
                        usecols = [0, 92, 93, 94, 95, 96, 97])
data.columns = ['DISCO', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']

#rounding off numbers to 2 significant figures
pd.options.display.float_format = '{:,.2f}'.format
print('\n Original data:\n',data)

# Transposing the data frame
data.set_index('DISCO', inplace = True)
df = data.transpose()

# renaming columns and distribution company name for readability convenience
for header_name in df.columns:
    df.rename({header_name: header_name.split()[0]}, axis = 1, inplace = True)
    
print('\n Transposed Data:\n',df)


#plotting line chartheader_name
def plot_A(data):
    
    """This will plot the Months on x-axis and 
    the Revenue in Naira Million on the X-axis"""
    
    plt.figure(figsize = (6, 4))
    for header_name in data.columns:
        plt.plot(data[header_name], label = header_name)
    plt.xlabel('Month', fontweight = 'bold')
    plt.ylabel('Naira(Million)', fontweight = 'bold')
    plt.legend(bbox_to_anchor = (1.02,1), title = 'Distribution Company')
    plt.title(('NIGERIA ELECTRICITY DISTRIBUTION COMPANIES')+
            (' REVENUE COLLECTION FOR THE HALF YEAR 2022'),
            fontweight = 'bold')
    plt.savefig("electricitydata.jpg", bbox_inches = 'tight', dpi = 140)
    plt.show()


#plotting grouped bar chart for more insight
def plot_B(data):
    
    """This will plot the Months on x-axis and 
    the Revenue in Naira Million on the X-axis"""
    
    plt.figure(figsize = (6, 4))
    width = 0.07
    counter = 0
    data_length = len(data.index)
    
    for header_name in data.columns:
        mySeries = data[header_name].squeeze()
    
        #positioning the Bar elements
        if counter == 0:
            position = np.arange(len(data.index))
        else:
            position = [x + width for x in position]
        
        plt.bar(position, mySeries, width = width, label = header_name)
        counter += 1
    plt.xlabel('Month', fontweight = 'bold')
    plt.ylabel('Naira(Million)', fontweight = 'bold')
    plt.legend(bbox_to_anchor = (1.05,1), title = 'Distribution Company')
    plt.title(('NIGERIA ELECTRICITY DISTRIBUTION COMPANIES')+
            (' REVENUE COLLECTION FOR THE HALF YEAR 2022'),
            fontweight = 'bold')
    plt.xticks([r + width*(data_length-1) for r in range(data_length)],
        list(df.index.values))
    plt.savefig("electricitydata2.jpg", bbox_inches = 'tight', dpi = 140)
    plt.show()

    
#plotting piechart to get insights on each DISCO revenue percentage share
def plot_C(data):
    
    """This will plot a pie chart showing the total contribution of each
    distribution company"""
         
    plt.figure(figsize = (10, 8))
    df = data.transpose()
    df['Total'] = df.sum(axis = 1)
    plt.pie(df['Total'], labels = list(df.index.values),
                                  autopct = '%1.1f%%')

    plt.legend(bbox_to_anchor = (1.05,1), title = 'Distribution Company')
    plt.title(('NIGERIA ELECTRICITY DISTRIBUTION COMPANIES')+
            (' REVENUE COLLECTION FOR THE HALF YEAR 2022'),
            fontweight = 'bold')
    plt.savefig("electricitydata3.jpg", bbox_inches = 'tight', dpi = 140)
    plt.show()


def main(): 
    
    """ This will check for errors in code blocks"""
    try:
        print(f"\nPlotting Data from : {input_file}")
        plot_A(df)
        plot_B(df)
        plot_C(df)
        
    except Exception as Err:
        print(f"System Encountered an Error\n{Err}")


if __name__ == "__main__":
    main()
