#!/usr/bin/env python
# coding: utf-8

# In[1]:


dots_size = 90

def started_operation(msg=""):
    output = f"Started: {msg}..."
    dots = "." * dots_size
    print(f"{dots}\n{output}\n")
    
def completed_operation():
    dots = "." * dots_size
    print(f"\nCompleted.\n{dots}\n")
    
def error(msg):
    print(f"Error! {msg}\n")

def menu():
    print(f"""Please select one of the following options:
    {"[i]":<8} Search by car ID
    {"[ii]":<8} Search car by Cylinder
    {"[iii]":<8} Search car by Body
    {"[iv]":<8} Retrieve vital columns
    {"[v]":<8} Sort car names alphabetically
    {"[vi]":<8} Retrieve summary of sales for each car body
    {"[vii]":<8} Retrieve the top 5 car sale by price and per car body
    {"[viii]":<8} Retrieve the detail of cars based on your own selection
    {"[ix]":<8} Display cars per fuel system using a bar chart
    {"[x]":<8} Display the horsepower car sale by price using a subplot
    {"[xi]":<8} Display sales percentage per body
    
    {"[exit]":<8} Exit programme
    """)
    selection = input("Enter your selection: ")
    return selection.strip().lower()


# In[ ]:




