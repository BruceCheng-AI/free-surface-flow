# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:43:38 2020

@author: szh002
"""
import numpy as np
import sys
sys.path.append('..')
import fsf.fsf_engine as engine_module
import fsf.fsf_input as input_module

'''
The user has two ways to call this program
In the main.py, call it and obtain the current txtfile data 
Directly run this module and get the data
file_num -- argument represents one of the case that you run the code
flag_method -- Choosing between matrix inversion and doubel sweep

E.g.
test_h0([5,1]) -- test the fifth dataset and apply matrix inversion
The result will save in the report folder
'''



# =============================================================================
# Read the data in the required txtfile
# =============================================================================
def data(*information):
    if information == ():
        [file_num,filename] = input_module.input_file()       
        flag_method = input_module.flag_method()
    else:
        [file_num,flag_method] = information[0]
        filename = '../inputs/'+ str(file_num)+'.txt'
    read_data = input_module.read(filename) 
    read_data.append(flag_method)
    data = engine_module.calculation(read_data)
    data.append(file_num)
    return data



# =============================================================================
# Main code imported in the main.py
# =============================================================================
# Water level in upstream boundary
def test_h0(*information):
    result = data(*information)
    test_h0 = result[1][0]
    txtname = '..\\report\\test_h0_'+ str(result[-1]) +'.txt'
    np.savetxt(txtname,test_h0, fmt='%.02f')
    return test_h0
    
# Discharge in upstream boundary  
def test_q0(*information):
    result = data(*information)
    test_q0 = result[0][0]
    txtname = '..\\report\\test_q0_'+ str(result[-1]) +'.txt'
    np.savetxt(txtname,test_q0, fmt='%.02f')
    return test_q0

# Water level in downstream boundary
def test_h_end(*information):
    result = data(*information)
    test_h_end = result[1][-1]
    txtname = '..\\report\\test_h_end_'+ str(result[-1]) +'.txt'
    np.savetxt(txtname,test_h_end, fmt='%.02f')
    return test_h_end

# Water level in downstream boundary
def test_q_end(*information):
    result = data(*information)
    test_q_end = result[0][-1]
    txtname = '..\\report\\test_q_end_'+ str(result[-1]) +'.txt'
    np.savetxt(txtname,test_q_end, fmt='%.02f')
    return test_q_end