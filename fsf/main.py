# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:31:21 2020

@author: szh002
"""


import fsf_input
import fsf_engine
import fsf_report
import fsf_gif
import sys
sys.path.append('..')
import tests_module.test_module as test_module

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



# =============================================================================
# Plot the graph
# =============================================================================
# plot the graph for the chosen grid point
#fsf_report.graph(Q,H,X_series,T_series)
# plot the dynamic graph with the time changing
fsf_gif.gif(Q,H,X_series,T_series)



# =============================================================================
# Return a vector for all time steps in both boundaries
# =============================================================================
# Choose whether output the boundary dataset
print('\n Do you need to obtain the current boundary data,h0,q0,h_end,q_end?\nYes--1\nNo--2')
flag_boundary =fsf_report.flag()
if flag_boundary == 1:
    # Print the current test's boundary dataset: h0,q0,h_end,q_end
    # Then save in the report file
    h0 = test_module.test_h0([file_num,flag_method])
    q0 = test_module.test_q0([file_num,flag_method])
    h_end = test_module.test_h_end([file_num,flag_method])
    q_end = test_module.test_q_end([file_num,flag_method])