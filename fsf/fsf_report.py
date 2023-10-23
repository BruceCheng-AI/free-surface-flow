# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:55:43 2020

@author: szh002
"""

from matplotlib import pyplot as plt


# =============================================================================
# Input fuction, let the user choose
# =============================================================================
# Fill in filename
def output_file(file_type):
    filename = input('Please fill in the filename:\t ')        
    filename = '../report/'+ filename + file_type
    return filename

# Flag means choosing answer
def flag():
    try:
        flag = int(input('Please type the number:\t'))
    except ValueError:
        flag = input('It is wrong. Please type the right number again. (1,2):\t')
    while flag not in [1,2]:
        try:
            flag = int(input("It is wrong. Please type the right number again. (1,2):\t"))
        except ValueError:
            flag = int(input("It is wrong. Please type the right number again. (1,2):\t"))
    return flag

# Let the user fill in the number
def number(string):
    try:
        num = int(input(string))
    except ValueError :
        num = int(input('It is wrong. Please type again:\t'))
    while num<0:
        try:
            num = int(input("It is wrong. Please type again:\t"))
        except ValueError:
            num = int(input("It is wrong. Please type again:\t"))            
    return num


    
# =============================================================================
# Main code imported in the main.py
# =============================================================================
def graph(Q,H,X_series,T_series):
    # Choose between discharge and water level
    print('\nNow you should determine which type of graph you want to produce.\nDischarge--1\nWater level--2')
    flag_qh = flag()
    
    # Choose between grid point and time point 
    print('\nNow you should determine which type of graph you want to produce.\nChosen Grid point--1\nChosen time point--2')
    flag_xt = flag()

    # Determine the time and space step
    x_step = X_series[1] - X_series[0]
    t_step = T_series[1] - T_series[0]
    
    if flag_xt == 1: 
        num = int(number('\nPlease type the distance(m):\t')/x_step)
    else: 
        num = int(number('\nPlease type the time(s):\t')/t_step)          
    
    if flag_qh == 1: # Dischage 
        Title = 'Discharge changing with '
        Ylabel = 'Discharge (m^3/s)'
        if flag_xt == 1: # grid point 
            Title += 'time'
            Xlabel = 'Time (s)'
            Y = Q[:,num]
            X = T_series
        else: # time point
            Title += 'space'
            Xlabel = 'Distance (m)'
            Y = Q[num,:]
            X = X_series
    else: # Water level
        Title = 'Depth changing with '
        Ylabel = 'Depth (m)'
        if flag_xt == 1: # grid point 
            Title += 'time'
            Xlabel = 'Time (s)'
            Y = H[:,num]
            X = T_series
        else: # time point
            Title += 'space'
            Xlabel = 'Distance (m)'
            Y = H[num,:]
            X = X_series
    
    # Plot the graph
    plt.figure(figsize=[18, 14])
    plt.plot(X,Y)
    plt.xlabel(Xlabel)
    plt.ylabel(Ylabel)
    plt.title(Title)
    filename = output_file('.jpg')
    plt.savefig(filename)
    plt.show()
    


