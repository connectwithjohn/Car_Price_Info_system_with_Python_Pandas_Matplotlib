#!/usr/bin/env python
# coding: utf-8

# In[1]:

import interface
import csv
import pandas as pd


def searchById():
    interface.started_operation('retrieving data')
    id = input ("Enter car ID: ")
    csv_file=csv.reader(open('CarPrice.csv'))
    for row in csv_file:
        if id==row[0]:
            print(row)
    else:
        print('Invalid input')
    interface.completed_operation()
    
def searchByCylinder():
    interface.started_operation('retrieving data')
    cylinder = input("Enter Number of Cylinder: ")
    csv_file=csv.reader(open('CarPrice.csv'))
    for row in csv_file:
        if cylinder == row[13]:
            print(row)
    else:
        print('Invalid input')
    interface.completed_operation()
    
def searchByBody():
    interface.started_operation('retrieving data')
    body = input("Enter car Body type: ")
    modified_body= body.lower()
    csv_file=csv.reader(open('CarPrice.csv')) 
    for row in csv_file:
        if modified_body == row[4]:
            print (row)
    else:
        print('Invalid input')
    interface.completed_operation()
    
def specificColumn():
    interface.started_operation('retrieving data')
    carId = int(input('Enter car ID'))
    car_data = pd.read_csv ("CarPrice.csv")
    car_ID = carId
    selected_data = car_data.loc[carId,['car_ID','CarName', 'carbody', 
                                        'cylindernumber', 'price']]
    print(selected_data)
    interface.completed_operation()    
        
def alphabetically():
    interface.started_operation('loading data')
    car_data = pd.read_csv ("CarPrice.csv")
    alphabetical_data = car_data.sort_values(by="CarName", ascending=True)
    print (alphabetical_data)        
    interface.completed_operation() 
    
def salesSummary():
    interface.started_operation('retrieving data')
    body_type = input('Enter a Car Body type to get total sales: ')
    modified_body= body_type.lower()
    car_data = pd.read_csv ("CarPrice.csv")
    print(f'The summary of sales for {modified_body} is: ')
    sales=car_data.loc[car_data['carbody'] == modified_body, 'price'].sum()
    print(sales)
    interface.completed_operation()

def topSaleByBody():
    interface.started_operation('retrieving data')
    car_data = pd.read_csv ("CarPrice.csv")
    top_sale=car_data.groupby('carbody')['price'].nlargest(5)
    print(top_sale)
    interface.completed_operation()        
    
def covertibleAbove1500():
    interface.started_operation('retrieving data')
    car_data = pd.read_csv ("CarPrice.csv")
    convertible=car_data.loc[(car_data['price'] > 1500) 
                 & (car_data['carbody'] == 'convertible')]
    print(convertible)
    interface.completed_operation()
            
            

# In[ ]:




