# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:20:55 2020

@author: szh002
"""

import numpy as np
from scipy import linalg



# =============================================================================
# The value for the coefficients
# =============================================================================
def cal_A1(x,theta):
    A1 = - theta /x
    return A1

def cal_B1(b,t,psi):
    B1 = b * (1-psi)/t
    return B1

def cal_C1(x,theta):
    C1 = theta / x
    return C1

def cal_D1(b,t,psi):
    D1 = b * psi  / t
    return D1

def cal_E1(b,t,x,theta,psi,q_j,h_j,q_j1,h_j1):
    E1 = -(1-theta) * (q_j1 - q_j) / x + b * ((1-psi) * h_j/t + psi * h_j1/t)
    return E1

def cal_A2(b,C,t,x,psi,beta,g,q_j,h_j,h1_j):
    A2 = (1-psi)/t - beta * q_j/ x / (b * (h_j+h1_j)/2) + g * (b * (h_j+h1_j)/2) * (1-psi) * abs(q_j)/(C*b*((h_j+h1_j)/2)**1.5)**2
    return A2

def cal_B2(b,x,theta,g,h_j,h_j1,h1_j,h1_j1):
    B2 = -g *theta * (b *(h_j + h_j1+h1_j+h1_j1)/4)/x
    return B2

def cal_C2(b,C,t,x,psi,beta,g,q_j1,h_j1,h1_j1):
    C2 = psi/t + beta * q_j1/x / ((h_j1+h1_j1)/2 * b) + g *(b*(h_j1+h1_j1)/2)* psi * abs(q_j1)/(C*b*((h_j1+h1_j1)/2)**1.5)**2
    return C2

def cal_D2(b,x,theta,g,h_j,h_j1,h1_j,h1_j1):
    D2 = g *theta * (b *(h_j + h_j1+h1_j+h1_j1)/4)/x
    return D2

def cal_E2(b,S0,t,x,theta,psi,g,q_j,h_j,q_j1,h_j1,h1_j,h1_j1):
    E2 = (1-psi)/t * q_j + psi / t * q_j1 + g*(b *(h_j+h_j1+h1_j+h1_j1)/4)*(1-theta)/x*(h_j1-h_j) +g*S0*(b *(h_j+h_j1+h1_j+h1_j1)/4)
    return E2



# =============================================================================
# Matrix inversion
# =============================================================================
# Algorithm for each row 
def calculation_mi(n,qh):       
    for m in range(1,M):
        # Assign four points
        q_j = QH[2*m-2,n-1]
        h_j = QH[2*m-1,n-1]
        q_j1= QH[2*m,n-1]
        h_j1 = QH[2*m+1,n-1]
        h1_j = qh[2*m-1]
        h1_j1 = qh[2*m+1]
        # Calculate the coefficients
        Coef[n,2*m-1,2*m-2] = A1
        Coef[n,2*m-1,2*m-1] = B1
        Coef[n,2*m-1,2*m] = C1
        Coef[n,2*m-1,2*m+1] = D1
        En[2*m-1,n] = cal_E1(b,t,x,theta,psi,q_j,h_j,q_j1,h_j1)
        Coef[n,2*m,2*m-2] = cal_A2(b,C,t,x,psi,beta,g,q_j,h_j,h1_j)
        Coef[n,2*m,2*m-1] = cal_B2(b,x,theta,g,h_j,h_j1,h1_j,h1_j1)
        Coef[n,2*m,2*m] = cal_C2(b,C,t,x,psi,beta,g,q_j1,h_j1,h1_j1)
        Coef[n,2*m,2*m+1] = cal_D2(b,x,theta,g,h_j,h_j1,h1_j,h1_j1)
        En[2*m,n] = cal_E2(b,S0,t,x,theta,psi,g,q_j,h_j,q_j1,h_j1,h1_j,h1_j1)
    # Matrix calculation 
    QH_test = linalg.solve(Coef[n,:,:], En[:,n])
    return QH_test

# Root Mean Square Error
def RMSE_mi(qh_1,qh,Iteration):
    Error = 0
    for i in range(2*M):
        Error += (qh_1[i] - qh[i])**2
    Error = np.sqrt(Error/(2*M))
    Iteration += 1
    return [Error,Iteration]

# Main code for matrix inversion
def matrix_inversion():
    global Coef,En,QH
    # Initial the value
    Coef = np.zeros((N,2*M,2*M))
    En = np.zeros((2*M,N))
    QH = np.zeros((2*M,N))
    
    # Coefficient in both boundaries
    for n in range(1,N):
        #Upstream boundary
        if flag_up == 0:
            Coef[n,0,1] = 1
        else:
            Coef[n,0,0] = 1
        # Downstream boundary
        if flag_down == 0:
            Coef[n,2*M-1,2*M-1] = 1
        else:    
            Coef[n,2*M-1,2*M-2] = 1  
    
    # En value in both boundaries
    for n in range(1,N):
        if flag_up == 0:
            En[0,n] = np.interp(T_series[n],H_up[:,0],H_up[:,1])
        else:
            En[0,n] = np.interp(T_series[n],Q_up[:,0],Q_up[:,1])
        if flag_down == 0:
            En[2*M-1,n] = np.interp(T_series[n],H_down[:,0],H_down[:,1])
        else:
            En[2*M-1,n] = np.interp(T_series[n],Q_down[:,0],Q_down[:,1])
    
    # Initial condition
    for m in range(M):
        QH[2*m,0] = np.interp(X_series[m],Q_ini[:,0],Q_ini[:,1])
        QH[2*m+1,0] = np.interp(X_series[m],H_ini[:,0],H_ini[:,1])
    
    # Iterative solution of nonlinear equations
    for n in range(1,N):
        qh = QH[:,n-1]
        Error = 1
        Iteration = 0
        while Error > Err and Iteration <= Iter:
            qh_1 = calculation_mi(n,qh)
            [Error,Iteration] = RMSE_mi(qh_1,qh,Iteration)
            qh = qh_1
        QH[:,n] = qh
    
    # Transpose the matrix
    QH = np.transpose(QH)
    for i in range(M):
        Q[:,i] = QH[:,2*i]
        H[:,i] = QH[:,2*i+1]
        
    return [Q,H,X_series,T_series]



# =============================================================================
# Double sweep algorithm 
# =============================================================================
# Algorithm for each row
def calculation_ds(n,q,h):
    # Initial the value
    q_1 = np.zeros(M)
    h_1 = np.zeros(M)
    E1 = np.zeros((M-1))
    A2 = np.zeros((M-1))
    B2 = np.zeros((M-1))
    C2 = np.zeros((M-1))
    D2 = np.zeros((M-1))
    E2 = np.zeros((M-1))
    R = np.zeros((M-1))
    I = np.zeros((M-1))
    J = np.zeros((M-1))
    F = np.zeros((M))
    G = np.zeros((M))

    # Forward sweep
    # Upstream boundary condition
    if flag_up == 0: # Water level
        F[0] = 10**6
        G[0] = -F[0] * np.interp(T_series[n+1],H_up[:,0],H_up[:,1])
    else: # discharge
        F[0] = 0
        G[0] = np.interp(T_series[n+1],Q_up[:,0],Q_up[:,1])
    for m in range(M-1):
        # Assign four points
        q_j = Q[n,m]
        h_j = H[n,m]
        q_j1 = Q[n,m+1]
        h_j1 = H[n,m+1]
        h1_j = h[m]
        h1_j1 = h[m+1]
        # Calculate the coefficient 
        E1[m] = cal_E1(b,t,x,theta,psi,q_j,h_j,q_j1,h_j1)
        A2[m] = cal_A2(b,C,t,x,psi,beta,g,q_j,h_j,h1_j)
        B2[m] = cal_B2(b,x,theta,g,h_j,h_j1,h1_j,h1_j1)
        C2[m] = cal_C2(b,C,t,x,psi,beta,g,q_j1,h_j1,h1_j1)
        D2[m] = cal_D2(b,x,theta,g,h_j,h_j1,h1_j,h1_j1)
        E2[m] = cal_E2(b,S0,t,x,theta,psi,g,q_j,h_j,q_j1,h_j1,h1_j,h1_j1)
        R[m] = -C1/(A1*F[m]+B1)
        I[m] = - D1/(A1*F[m]+B1)
        J[m] = (E1[m]-A1*G[m])/(A1*F[m]+B1)
        F[m+1] = (-I[m]*(A2[m]*F[m]+B2[m])-D2[m])/(R[m]*(A2[m]*F[m]+B2[m])+C2[m])
        G[m+1] = (E2[m] - A2[m]*F[m]*J[m]-A2[m]*G[m]-B2[m]*J[m])/(R[m]*(A2[m]*F[m]+B2[m])+C2[m])
    # Downstream boundary condition
    if flag_down == 0: # Water level
        h_1[M-1] = np.interp(T_series[n+1],H_down[:,0],H_down[:,1])
        q_1[M-1] = F[M-1] * h_1[M-1] + G[M-1]
    else: # Discharge
        q_1[M-1] = np.interp(T_series[n+1],Q_down[:,0],Q_down[:,1])
        h_1[M-1] = (q_1[M-1]-G[M-1])/F[M-1]
    
    # Backward sweep
    for m in range(M-1,0,-1):
        h_1[m-1] = R[m-1] * q_1[m] + I[m-1] * h_1[m] + J[m-1]
        q_1[m-1] = F[m-1] * h_1[m-1] + G[m-1]
    result = [q_1,h_1]
    return result


# Root Mean Square Error  
def RMSE_ds(q_1,h_1,q,h,Iteration):
    Error = 0
    for i in range(M):
        Error += (q_1[i] - q[i])**2 + (h_1[i] - h[i])**2
    Error = np.sqrt(Error/(2*M))
    Iteration += 1
    return [Error,Iteration]

# Main code for double sweep algorithm  
def double_sweep():
    # Initial value
    for m in range(M):
        Q[0,m] = np.interp(X_series[m],Q_ini[:,0],Q_ini[:,1])
        H[0,m] = np.interp(X_series[m],H_ini[:,0],H_ini[:,1])

    # Iterate and compare with the Err      
    for n in range(N-1):
        q = Q[n,:]
        h = H[n,:]
        Iteration = 0
        Error = 1
        while Error > Err and Iteration <= Iter:
            [q_1,h_1] = calculation_ds(n,q,h)
            [Error,Iteration] = RMSE_ds(q_1,h_1,q,h,Iteration)
            q = q_1
            h = h_1
        Q[n+1,:] = q
        H[n+1,:] = h
    return [Q,H,X_series,T_series]


# =============================================================================
# Main code imported in the main.py
# =============================================================================
def calculation(read_data):
    global flag_up,flag_down,H_up,Q_up,H_down,Q_down,H_ini,Q_ini,L,b,S0,C,t,T,x,theta,psi,beta,Iter,Err,g,flag_method,M,N,X_series,T_series,A1,B1,C1,D1,Q,H
    # Initial value
    [flag_up,flag_down,H_up,Q_up,H_down,Q_down,H_ini,Q_ini,L,b,S0,C,t,T,x,theta,psi,beta,Iter,Err,g,flag_method] = read_data
    M = int(L/x) + 1
    N = int(T/t) + 1
    X_series = np.array(range(M)) * x
    T_series = np.array(range(N)) * t
    A1 = cal_A1(x,theta)
    B1 = cal_B1(b,t,psi)
    C1 = cal_C1(x,theta)
    D1 = cal_D1(b,t,psi)
    
    # Target value
    Q = np.zeros((N,M))
    H = np.zeros((N,M))
    
    # Choose method
    if flag_method == 1:
        result = matrix_inversion()
    else:
        result = double_sweep()
    return result