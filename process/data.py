#!/usr/bin/env python
# coding: utf-8

# dependencies
import os
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
import seaborn as sns
import copy
import pandas as pd

sns.set()
# sns.set_style("dark")
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=3, rc={"lines.linewidth": 3})
# mpl.rcParams['lines.linewidth'] = 3

##
## Methods for [datasets/covid-19](https://github.com/datasets/covid-19)
##

# list confirmed cases of one country
def get_country_data_1(df, country):
    
    d1 = df['Date']
    d2 = df['Country/Region']
    d3 = df['Confirmed']
      
    #     print(d1.head(5))
    #     print(d2.head(5))
    
    a = []
    b = []
    c = []
    d = []
    counter = -1
    for i in range(len(d1)):
        if str(d2[i]) == country:
            
            if float(d3[i]) > 0.:
                counter += 1
            
            
            a.append(counter)
            b.append(d1[i])
            c.append(country)
            d.append(float(d3[i]))
              
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)
    data = [a, b, c, d]
    data = np.array(data)
    dd = pd.DataFrame(data.T, columns=['day', 'date', 'country', 'cases'])
    return dd

# list confirmed cases of one country
def get_confirmed_1(df, country):
    
    d1 = df['Date']
    d2 = df['Country/Region']
    d3 = df['Confirmed']
    a = []
    b = []
    c = []
    d = ''
    counter = -1
    for i in range(len(d1)):
        if str(d2[i]) == country:
            
            if float(d3[i]) > 0.:
                counter += 1
                c.append(counter)
                a.append(d1[i])
                b.append(float(d3[i]))
            if counter == 0:
                d = str(d1[i])
              
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    return a, b, c, d


# plot data
def plot_countries_1(df, countries):
    
    n = len(countries)
    fig = plt.figure(figsize=(20., 20.))
    axes = fig.subplots(nrows=n, ncols=1)
    
    for i in range(n):
        
        a,b,c,d = get_confirmed(df, countries[i])
        axes[i].plot(c, b, label='Country: {}, Start date: {}'.format(countries[i], d))
        
        axes[i].set_title(countries[i])                            
        axes[i].set_xlabel('Date')
        axes[i].set_ylabel('Confirmed cases')
        axes[i].legend()
        
        
    plt.show() 
    
# plot data
def plot_countries_all_1(df, countries):
    
    n = len(countries)
    fig = plt.figure(figsize=(12., 8.))
    
    for i in range(n):
        
        a,b,c,d = get_confirmed_1(df, countries[i])
        
        if i == 0:
            print('Num days: {}'.format(c[-1] + 1))
        
        plt.plot(c, b, label='Country: {}, Start date: {}'.format(countries[i], d))
        
        plt.title('Confirmed cases for different countries')                            
        plt.xlabel('Day')
        plt.ylabel('Confirmed cases')
        
        plt.legend(prop={'size': 15})
        
        
        
        
    plt.show() 
    
    
# plot data
def plot_countries_all_normalize_1(df, countries):
    
    n = len(countries)
    fig = plt.figure(figsize=(10., 5.))
    
    for i in range(n):
        
        a,b,c,d = get_confirmed_1(df, countries[i])
        
        scale = np.max(b)
        b = np.true_divide(b, scale)
            
            
        print('Country: {}. Num days: {}'.format(countries[i], c[-1] + 1))
        
        plt.plot(c, b, label='Country: {}, Start date: {}'.format(countries[i], d))
        
        plt.title('Normalized plot of confirmed cases')                            
        plt.xlabel('Day')
        plt.ylabel('Confirmed cases')
        
        plt.legend(prop={'size': 15})
        
        
    plt.show() 
    
    
def plot_countries_all_plus_normalize_1(df, countries):
    
    n = len(countries)
    
    sns.set_context("notebook", font_scale=2, rc={"lines.linewidth": 3})
    
    fig = plt.figure(figsize=(30., 10.))
    axes = fig.subplots(nrows=1, ncols=2)
    
    for i in range(n):
        
        a,b,c,d = get_confirmed_1(df, countries[i])
        if i == 0:
            print('Num days: {}'.format(c[-1] + 1))
        
        # plot unnormalized first
        axes[0].plot(c, b, label='Country: {}, Start date: {}'.format(countries[i], d))
        axes[0].set_title('Confirmed cases for different countries')                            
        axes[0].set_xlabel('Day')
        axes[0].set_ylabel('Confirmed cases')
        axes[0].legend(prop={'size': 15})
        
        # plot normalized now
        
        scale = np.max(b)
        b = np.true_divide(b, scale)
        
        axes[1].plot(c, b, label='Country: {}, Start date: {}'.format(countries[i], d))
        axes[1].set_title('Normalized confirmed cases for different countries')                            
        axes[1].set_xlabel('Day')
        axes[1].set_ylabel('Normalized confirmed cases')
        axes[1].legend(prop={'size': 15})
        
        
    plt.show() 
    
    
def save_country_data_1(df, countries):
    
    n = len(countries)
    
    for i in range(n):
        
        # write to file
        inpf = open(countries[i]+'.csv','w')
        
        a,b,c,d = get_confirmed_1(df, countries[i])
        
        for j in range(len(c)):
            inpf.write('{}, {}\n'.format(c[j], b[j]))
        
        inpf.close()

        
##
## Methods for [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
##

Nrows = 264
Ncols = 88

def find_row_2(df, country):
    for i in range(Nrows):
        a = df.iloc[i][1]
        
        if a == country:
            
            return i
        
def get_array_2(d):
    a = []
    for i in range(Ncols-2):
        a.append(int(d[i+2]))
        
    return np.array(a)


# plot data
def plot_countries_all_2(df, countries):
    
    n = len(countries)
    fig = plt.figure(figsize=(20., 20.))
    
    for i in range(n):
        
        a = df.iloc[find_row_2(df, countries[i])]
        b = get_array_2(a)
        
        plt.plot(b, label='Country: {}'.format(countries[i]))
        
        plt.title('Confirmed cases for different countries')                            
        plt.xlabel('Day')
        plt.ylabel('Confirmed cases')
        
        plt.legend(prop={'size': 40})
        
        
    plt.show() 