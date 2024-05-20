import numpy as np
import pandas as pd

import scipy as sp
from scipy.stats import norm

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


def mpoisson(l, x):
    return((l**x)*np.exp(-l))/sp.special.factorial(x)


def draw_coins_flip(p = 0.5, n_of_experiments = 15000, figsize=(14, 5)):
    # https://stackoverflow.com/questions/43080259/how-to-add-edge-color-to-a-histogram
    # https://seaborn.pydata.org/tutorial/function_overview.html#figure-level-vs-axes-level-functions

    p = p
    n_of_experiments = n_of_experiments

    df_experiments = pd.concat(
        [
            pd.DataFrame(
                {
                    'means' : (np.random.choice([0,1], p = [1-p,p], size = [n_of_experiments,10]).mean(axis = 1)-p)/(np.sqrt(p*(1-p)/10)),
                    'n_of_coins' : '10'
                }
            ),
            pd.DataFrame(
                {
                    'means' : (np.random.choice([0,1], p = [1-p,p], size = [n_of_experiments,20]).mean(axis = 1)-p)/(np.sqrt(p*(1-p)/20)),
                    'n_of_coins' : '20'
                }
            ),
            pd.DataFrame(
                {
                    'means' : (np.random.choice([0,1], p = [1-p,p], size = [n_of_experiments,30]).mean(axis = 1)-p)/(np.sqrt(p*(1-p)/30)),
                    'n_of_coins' : '30'
                }
            )
        ]
    )
    
    x = np.linspace(-3, 3, 100)
    y = norm.pdf(x)
    
    fig, axs = plt.subplots(ncols=3, sharey=True, sharex = True, figsize=figsize)
    
    sns.histplot(
        data=df_experiments[df_experiments['n_of_coins'] == '10'],
        x = 'means',
        binwidth=0.35,
        stat = 'density',
        color = 'coral',
        edgecolor='k',
        ax = axs[0],
    ).set_title('10 coins');
    
    sns.lineplot(
        x = x,
        y = y,
        color = 'k',
        ax = axs[0]
    )
    
    sns.histplot(
        data=df_experiments[df_experiments['n_of_coins'] == '20'],
        x = 'means',
        binwidth=0.35,
        stat = 'density',
        color = 'mediumseagreen',
        edgecolor='k',
        ax = axs[1]
    ).set_title('20 coins');
    
    sns.lineplot(
        x = x,
        y = y,
        color = 'k',
        ax = axs[1]
    );
    
    sns.histplot(
        data=df_experiments[df_experiments['n_of_coins'] == '30'],
        x = 'means',
        binwidth=0.35,
        stat = 'density',
        color = 'steelblue',
        edgecolor='k',
        ax = axs[2]
    ).set_title('30 coins');
    
    sns.lineplot(
        x = x,
        y = y,
        color = 'k',
        ax = axs[2]
    );


def draw_n_dice(n_of_dice = [10,20,30], n_of_experiments = 15000, figsize = (14,7)):
    figsize = figsize
    n_of_dice = n_of_dice
    n_of_experiments = n_of_experiments
    df_experiments = pd.DataFrame(columns=['count', 'n_of_dice'])
    
    for die in n_of_dice:
        means = []
        sigma = 1.71/np.sqrt(die)
        for i in np.arange(0,n_of_experiments):
            means.append((np.random.choice(np.arange(1, 7),size = die,replace = True).mean()-3.5)/sigma)
        df_means = pd.DataFrame({'count' : means, 'n_of_dice': str(die)})
        df_experiments=pd.concat([df_experiments, df_means])
    
    x = np.linspace(-4, 4, 100)
    y = norm.pdf(x)
        
    fig, (axs1, axs2, axs3) = plt.subplots(ncols=3, sharey=True, sharex = True, figsize=figsize)
        
    p1 = sns.histplot(
            data=df_experiments[df_experiments['n_of_dice'] == '10'],
            x = 'count',
            binwidth=0.30,
            stat = 'density',
            color = 'coral',
            edgecolor='k',
            ax = axs1,
        label = '10'
        ).set_title('10 dice');
        
    sns.lineplot(
            x = x,
            y = y,
            color = 'k',
            ax = axs1
        )
        
    p2 = sns.histplot(
            data=df_experiments[df_experiments['n_of_dice'] == '20'],
            x = 'count',
            binwidth=0.30,
            stat = 'density',
            color = 'mediumseagreen',
            edgecolor='k',
         label = '20',
            ax = axs2
        ).set_title('20 dice');
        
    sns.lineplot(
            x = x,
            y = y,
            color = 'k',
            ax = axs2
    );
        
    p3 = sns.histplot(
            data=df_experiments[df_experiments['n_of_dice'] == '30'],
            x = 'count',
            binwidth=0.30,
            stat = 'density',
            color = 'steelblue',
            edgecolor='k',
         label = '30',
            ax = axs3
    ).set_title('30 dice');
        
    sns.lineplot(
            x = x,
            y = y,
            color = 'k',
            ax = axs3
    );
