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
    
    M = len(X_series)
    # Plot the graph
    plt.figure(figsize=[18, 14])
    ax1 = plt.subplot(2,1,1)
    ax2 = plt.subplot(2,1,2)
    plt.sca(ax1)
    plt.plot(T_series,Q[:,0],label=str(T_series[0])+'s')
    plt.plot(T_series,Q[:,M/5],label=str(T_series[M/5])+'s')
    plt.plot(T_series,Q[:,2*M/5],label=str(T_series[2*M/5])+'s')
    plt.plot(T_series,Q[:,3*M/5],label=str(T_series[3*M/5])+'s')
    plt.plot(T_series,Q[:,4*M/5],label=str(T_series[4*M/5])+'s')
    plt.plot(T_series,Q[:,M-1],label=str(T_series[M-1])+'s')
    plt.xlabel('Time(s)',size=12)
    plt.ylabel('Discharge (m^3/s)',size=12)
    plt.title('Discharge as time changing',size=16)
    plt.grid()
    plt.sca(ax2)
    plt.plot(T_series,H[:,0],label=str(T_series[0])+'s')
    plt.plot(T_series,H[:,M/5],label=str(T_series[M/5])+'s')
    plt.plot(T_series,H[:,2*M/5],label=str(T_series[2*M/5])+'s')
    plt.plot(T_series,H[:,3*M/5],label=str(T_series[3*M/5])+'s')
    plt.plot(T_series,H[:,4*M/5],label=str(T_series[4*M/5])+'s')
    plt.plot(T_series,H[:,M-1],label=str(T_series[M-1])+'s')
    # set x limitation
    plt.xlabel('Discharge (m^3/s)',size=12)
    plt.ylabel('Water level (m^3/s)',size=12)
    plt.title('Height of the water level graph',size=16)
    plt.legend()
    plt.grid()
    filename = output_file('.jpg')
    plt.savefig(filename)
    plt.show()


