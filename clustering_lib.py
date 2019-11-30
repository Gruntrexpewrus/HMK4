#!/usr/bin/env python
# coding: utf-8

# In[6]:
import numpy as np
import pandas as pd

def dist2(dFrame, centr, index):
    S=0
    for j in range(2):
        S+= (dFrame[dFrame.columns[j]]-centr[index][j])**2
    ret=np.sqrt(S)
    return ret


# In[7]:


def distAll(dFrame, centr, index):
    S=0
    for j in range(13):
        S+= (dFrame[dFrame.columns[j]]-centr[index][j])**2
    ret=np.sqrt(S)
    return ret


# In[8]:


def assignment2(dFrame, centr):
    for i in centr.keys():
        dFrame['distance_from_{}'.format(i)] = dist2(dFrame, centr, i)
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centr.keys()]
    dFrame['closest'] = dFrame.loc[:, centroid_distance_cols].idxmin(axis=1)
    dFrame['closest'] = dFrame['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    colmap = {1: 'r', 2: 'g', 3: 'b'}
    dFrame['color'] = dFrame['closest'].map(lambda x: colmap[x])
    
    return dFrame

def assignmentAll(dFrame, centr):
    for i in centr.keys():
        dFrame['distance_from_{}'.format(i)] = distAll(dFrame, centr, i)
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centr.keys()]
    dFrame['closest'] = dFrame.loc[:, centroid_distance_cols].idxmin(axis=1)
    dFrame['closest'] = dFrame['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    colmap = {1: 'r', 2: 'g', 3: 'b'}
    dFrame['color'] = dFrame['closest'].map(lambda x: colmap[x])
    
    return dFrame


# In[9]:


def update2(dFrame, centr):
    for i in centr.keys():
        centr[i][0] = np.mean(dFrame[dFrame['closest'] == i]['Alcohol'])
        centr[i][1] = np.mean(dFrame[dFrame['closest'] == i]['Malic acid'])
    return centr


# In[10]:


def updateAll(dFrame, centr):
    for i in centr.keys():
        for j in range(13):
            centr[i][j] = np.mean(dFrame[dFrame['closest'] == i][dFrame.columns[j]])

    return centr


# In[ ]:
