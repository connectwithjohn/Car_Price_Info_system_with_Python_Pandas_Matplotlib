#!/usr/bin/env python
# coding: utf-8

# In[2]:

import interface
import csv
import pandas as pd
import matplotlib.pyplot as plt


def displayCarPerFuelSystem():
    interface.started_operation('Displaying data')
    fuelsystem = dict()
    with open("CarPrice.csv") as car_data:
        csvreader = csv.reader(car_data)
        headings= next (csvreader)
        for row in csvreader:
            if row[15] not in fuelsystem:
                fuelsystem[row[15]] = 0
            fuelsystem[row[15]] += 1
            
  
    fig = plt.figure(figsize=(7,3)) 
    plt.xlabel("Fuel System")
    plt.ylabel("Number of cars")
    plt.title("Number of cars per Fuel System")
    plt.bar(fuelsystem.keys(), fuelsystem.values(), color='skyblue', label='Number of cars');
    plt.legend()
    plt.show()
    fig.savefig('number_per_fuel_sys.png')
    interface.completed_operation() 
    
def horsepowerSubplot():
    interface.started_operation('Displaying data')
    car_data = pd.read_csv ("CarPrice.csv")
    selected_sub= car_data[['CarName','price','horsepower']].nsmallest(5,"price")
    
    fig , (ax1,ax2) = plt.subplots(1,2, figsize = (22,9))
    fig.suptitle("Relationship between Car Prices and Horsepower")
    
    # First Axis
    car_name = selected_sub['CarName']
    car_price = selected_sub['price']
    ax1.scatter(car_name, car_price, label='Cars and prices')
    ax1.set(title="Cars & Prices", xlabel='Cars',ylabel='Prices')
    ax1.legend()
    ax1.grid(True)
    ax1.set_facecolor("whitesmoke")
    
    # Second Axis
    car_name = selected_sub['CarName']
    horsepower = selected_sub['horsepower']
    ax2.scatter(car_name, horsepower, label='Cars and horsepower')
    ax2.set(title="Cars and Horsepower", xlabel='Cars',ylabel='Horsepower')
    ax2.legend()
    ax2.grid(True)
    plt.show()
    interface.completed_operation()
    
def displaySalesPercent():
    interface.started_operation('Displaying data')
    fig=plt.figure(figsize=(8,7))
    car_data = pd.read_csv ("CarPrice.csv")
    car_data.groupby('carbody')['price'].sum().plot(kind='pie',y='price', 
                                                autopct='%1.0f%%',
                                                colors = ['red', 'pink', 'steelblue', 'lightgreen', 
                                                'skyblue'],
                                                title='Sales summary per carbody'), plt.legend();
    plt.show()
    interface.completed_operation()
        


        


# In[ ]:




