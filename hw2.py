# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import numpy as np
import scipy.stats as st


#%%
def J_r_calc(data,q):
    '''
    Calculation of J_r statistic
    
    Parameters:
    
    data: 1D array, time series data of a certain stock (difference between each time point)
    
    q: int, parameter of the VR test
    
    Return:
    
    return 1: float, value of J_r statistic
    
    return 2: int, n of the VR test, namely Size of data devided by q
    
    '''
    # modify the length of data to nq
    if len(data)%q != 0:
        data = data[len(data)%q:]
    
    n = len(data)//q
    
    sigma_a_sq=np.power(data,2).sum()
    print(q,n,len(data))
    data_q = data.reshape(q,n)
    sigma_b_sq=np.power(data_q.sum(axis=0),2).sum()
    
    return sigma_b_sq/sigma_a_sq - 1 ,n

def VR_test(data,q):
    '''
    Operate the VR test to the time series data
    
    Parameters:
    
    data: 1D array, time series data of a certain stock (difference between each time point)
    
    q: int, parameter of the VR test
    
    Return:
    
    return 1: float, p-value of the VR test
    
    '''
    
    J_r,n=J_r_calc(data,q)
    
    sigma=np.sqrt(2*(q-1)/q)
    
    print(sigma,J_r)
    
    return (1-st.norm.cdf(np.sqrt(n)*abs(J_r)/sigma))*2


#%%
import quandl


#%%
quandl.ApiConfig.api_key="uHpSg7KFWwTFxsidU6x-"


#%%
IBM = quandl.get("EOD/IBM",start_data="2000-01-01")


#%%
import pandas as pd


#%%
IBM


#%%
IBM_value_closed = IBM['Adj_Close']


#%%
IBM_return=IBM_value_closed.pct_change()[1:].values


#%%
IBM_return


#%%
[VR_test(IBM_return,i) for i in [2,3,6,12]]


#%%
alpha_plus=1-(1-0.05)**(1/4)


#%%
alpha_plus


#%%



#%%
p_values=[VR_test(IBM_return,q) for q in [2,3,6,12]]


#%%
S_star_p=min(p_values)


#%%
if(S_star_p<alpha_plus):
    print('Reject')


#%%
print(p_values)


#%%



