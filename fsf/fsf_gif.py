# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:07:08 2020

@author: szh002
"""
from matplotlib import pyplot as plt
import matplotlib.animation as animation



# =============================================================================
# Input fuction, let the user choose
# =============================================================================
# Fill in filename
def output_file(string,file_type):
    filename = input(string)        
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


# Produce dynamic graph 
def process(N,label,title,Y,X_series,string):
    fig = plt.figure(figsize=[18, 14])
    plt.xlabel('Distance (m)',size=12)
    plt.ylabel(label,size=12)
    plt.title(title,size=14)
    ims = []
    for n in range(N):
        im = plt.plot(X_series,Y[10*n])
        ims.append(im)
    ani = animation.ArtistAnimation(fig, ims, interval=200, repeat_delay=1000)
    filename = output_file(string,'.gif')
    ani.save(filename,writer=animation.PillowWriter(fps=10))
    plt.close()



# =============================================================================
# Main code imported in the main.py
# =============================================================================
def gif(Q,H,X_series,T_series):
    print('Now determine whether plot the dynamic graph. \n1--Yes\n2--No')
    flag_judge = flag()
    if flag_judge == 1:      
        N = int(len(T_series)/10)
        # Discharge graph
        process(N,'Discharge (m^3/s)','Discharge changing with distance',Q,X_series,'Discharge dynamic graph.Please fill in the filename:\t')
        # Water level graph
        process(N,'Water level (m)','Water level changing with distance',H,X_series,'Water level dynamic graph.Please fill in the filename:\t')
