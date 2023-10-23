# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:50:35 2020

@author: szh002
"""
import numpy as np


# =============================================================================
# Choose the test dataset
# =============================================================================
def input_file():
    try:
        file_num = int(input('Please type the test number you want. (1~11):\t'))
    except ValueError :
        file_num = int(input('It is wrong. Please type the test number again. (1~11):\t'))
    while file_num < 1 or file_num > 12:
        try:
            file_num = int(input("It is wrong. Please type the test number again. (1~11):\t"))
        except ValueError:
            file_num = int(input("It is wrong. Please type the test number again. (1~11):\t"))            
    filename = '../inputs/'+ str(file_num)+'.txt'
    return [file_num,filename]
    

# =============================================================================
# Choose the calculating method (matrix inversion or double sweep)    
# =============================================================================
def flag_method():
    try:
        print('\nNow you should choose which method you apply, whether matrix inversion or double sweep.')
        flag_method = int(input('For matrix inversion, type 1; for double sweep, type 2.Please type the number:\t'))
    except ValueError :
        flag_method = input('It is wrong. Please type the right number again. (1,2):\t')
    while flag_method not in [1,2]:
        try:
            flag_method = int(input("It is wrong. Please type the right number again. (1,2):\t"))
        except ValueError:
            flag_method = int(input("It is wrong. Please type the right number again. (1,2):\t"))
    return flag_method



# =============================================================================
# Main code imported in the main.py
# =============================================================================
def read(filename):
    global data_all,data
    # Intercept the table part (note: all the element is string)
    def table(string):
        value = []
        position = data.find(string)
        if position == 0:
            del data_all[0:3]
            while data_all:
                series_temp = data_all.pop(0).split()
                temp = []
                for i in series_temp:
                    try:
                        i_float = float(i)
                        temp.append(i_float)
                    except:
                        pass
                if series_temp[0][0] == '*':
                    break
                value.append(temp)
        return value
    
    # Obtain each table value
    def obtain(dataset,string):
        if dataset == []:
            dataset = table(string)
        return dataset
    
    # Get the variable name (Each table name)
    def Variable_name(name, locals):    
        # print(locals)
        for key in locals:
            if locals[key] == name:
                return key
    
    # Check the validity of each element of data and pop up error
    def check_valid(dataset,table_name,row_num):
        length = len(dataset)
        for i in range(length):
            try:
                dataset[i][row_num -1]
            except IndexError:
                raise IndexError('Table '+table_name+' has invalid data or space, please check in')

    strings= ['\tTable.1','\tTable.2','\tTable.3','\tTable.4','\tTable.5']
    # The data in Upstream  boundary table
    upstream = []
    # The data in Downstream boundary table
    downstream = []
    # The data in Initial boundary table
    initial = []
    # The data in cancel table
    geometry = []
    # The data in numerical parameters
    parameters = []
    with open(filename,'r') as fname:
        data_all = fname.readlines()
        # flag = 0 -- h
        # flag = -1 -- Q
        flag_up = -1
        flag_down = -1
        while data_all:
            data = data_all.pop(0)
            if flag_up == -1:
                flag_up = data.find('# Upstream boundary: h')
            if flag_down == -1:
                flag_down = data.find('# Downstream boundary: h')
            # Obtain the table part
            upstream = obtain(upstream,strings[0])           
            downstream = obtain(downstream,strings[1])
            initial = obtain(initial,strings[2])
            geometry = obtain(geometry,strings[3])
            parameters = obtain(parameters,strings[4])
    
    # Check validity       
    check_valid(upstream,Variable_name(upstream,locals()),2)
    check_valid(downstream,Variable_name(downstream,locals()),2) 
    check_valid(initial,Variable_name(initial,locals()),3) 
    check_valid(geometry,Variable_name(geometry,locals()),1)
    check_valid(parameters,Variable_name(parameters,locals()),1)         
    
    # Assign variable names to data
    # Upstream boundary
    H_up = []; Q_up = []
    if flag_up == 0:
        # Water level
        H_up = np.array(upstream)
    else:
        # Discharge
        Q_up = np.array(upstream)
    
    # Downstream boundary
    H_down = []; Q_down = []
    if flag_down == 0:
        # Water level
        H_down = np.array(downstream)
    else:
        # Discharge
        Q_down = np.array(downstream)
    
    # Initial boundary
    H_ini = np.array(initial)[:,[0,1]]
    Q_ini = np.array(initial)[:,[0,2]]
    
    # The data of the cancel
    # Channel length
    L = geometry[0][0]
    # Contant channel width
    b = geometry[1][0]
    # Bed slope
    S0 = geometry[2][0]
    # Chezy resistance coefficient
    C = geometry[3][0]
    
    # The numerical parameters
    # Computational time step
    t = parameters[0][0]
    # Total time
    T = parameters[1][0]
    # Cell size
    x = parameters[2][0]
    # Time weighting parameter
    theta = parameters[3][0]
    # Space weighting parameter
    psi = parameters[4][0]
    # Coefficient
    beta = parameters[5][0]
    # Max No. of iteration 
    Iter = parameters[6][0]
    # Convergence criteria
    Err = parameters[7][0]
    # Gravity
    g = parameters[8][0]
    
    result = [flag_up,flag_down,H_up,Q_up,H_down,Q_down,H_ini,Q_ini,L,b,S0,C,t,T,x,theta,psi,beta,Iter,Err,g]
    return result