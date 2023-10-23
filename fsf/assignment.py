# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:31:21 2020

@author: szh002
"""


import fsf_input
import fsf_engine


from matplotlib import pyplot as plt

'''
The argument represents one of the case that you run the code for
1 -- static_test_1
2 -- static_test_2
3 -- static_test_3
4 -- steady_state_test
5 -- transient_test_1_a
6 -- transient_test_1_b
7 -- transient_test_2_a
8 -- transient_test_2_b
9 -- transient_test_3_a
10 -- transient_test_3_b
11 -- seiche test
'''






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
    
    N = len(T_series)
    # Plot the graph
    plt.figure(figsize=[18, 14])
    ax1 = plt.subplot(2,1,1)
    ax2 = plt.subplot(2,1,2)
    plt.sca(ax1)
    plt.plot(X_series,Q[0,:],label=str(T_series[0])+'s')
    plt.plot(X_series,Q[int(N/200),:],label=str(T_series[int(N/200)])+'s')   
    plt.plot(X_series,Q[int(N/100),:],label=str(T_series[int(N/100)])+'s')    
    plt.plot(X_series,Q[int(N/50),:],label=str(T_series[int(N/50)])+'s')
    plt.plot(X_series,Q[int(N/20),:],label=str(T_series[int(N/20)])+'s')
    plt.plot(X_series,Q[int(N/10),:],label=str(T_series[int(N/10)])+'s')
    plt.plot(X_series,Q[int(N/5),:],label=str(T_series[int(N/5)])+'s')
    plt.plot(X_series,Q[int(2*N/5),:],label=str(T_series[int(2*N/5)])+'s')
    plt.plot(X_series,Q[int(3*N/5),:],label=str(T_series[int(3*N/5)])+'s')
    plt.plot(X_series,Q[int(4*N/5),:],label=str(T_series[int(4*N/5)])+'s')
    plt.plot(X_series,Q[N-1,:],label=str(T_series[N-1])+'s')
    plt.xlabel('Distance (m)',size=12)
    plt.ylabel('Discharge (m^3/s)',size=12)
    plt.title('Discharge as time changing',size=16)
    plt.legend()
    plt.grid()
    plt.sca(ax2)
    plt.plot(X_series,H[0,:],label=str(T_series[0])+'s')
    plt.plot(X_series,H[int(N/200),:],label=str(T_series[int(N/200)])+'s')      
    plt.plot(X_series,H[int(N/100),:],label=str(T_series[int(N/100)])+'s')    
    plt.plot(X_series,H[int(N/50),:],label=str(T_series[int(N/50)])+'s')
    plt.plot(X_series,H[int(N/20),:],label=str(T_series[int(N/20)])+'s')
    plt.plot(X_series,H[int(N/10),:],label=str(T_series[int(N/10)])+'s')
    plt.plot(X_series,H[int(N/5),:],label=str(T_series[int(N/5)])+'s')
    plt.plot(X_series,H[int(2*N/5),:],label=str(T_series[int(2*N/5)])+'s')
    plt.plot(X_series,H[int(3*N/5),:],label=str(T_series[int(3*N/5)])+'s')
    plt.plot(X_series,H[int(4*N/5),:],label=str(T_series[int(4*N/5)])+'s')
    plt.plot(X_series,H[N-1,:],label=str(T_series[N-1])+'s')
    # set x limitation
    plt.xlabel('Distance (m)',size=12)
    plt.ylabel('Water level (m)',size=12)
    plt.title('Water level as time changing',size=16)
    plt.legend()
    plt.grid()
    filename = output_file('.jpg')
    plt.savefig(filename)
    plt.show()



# =============================================================================
# Input the dataset
# =============================================================================
# Choose the test dataset
[file_num,filename] = fsf_input.input_file()
# Read the dataset
read_data = fsf_input.read(filename)        



# =============================================================================
# Calculation
# =============================================================================
# Choose the calculating method (matrix inversion or double sweep)
flag_method = fsf_input.flag_method()
read_data.append(flag_method)
# Calculation module
[Q,H,X_series,T_series] = fsf_engine.calculation(read_data)

graph(Q,H,X_series,T_series)








