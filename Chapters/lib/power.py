import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import norm


def plot_power():
    n_samples = [8, 16, 32, 64, 128]
    alpha = 0.05
    
    mu0 = 30
    mua = np.linspace(30, 35, 100)
    sigma = 4
    
    df_power_plot = pd.DataFrame(
        columns=['x', 'power', 'n_samples']
    )
    
    for samples in n_samples:
        sem = sigma/np.sqrt(samples)
        
        df_temp = pd.DataFrame(
            columns=['x', 'power', 'n_samples']
        )
    
        df_temp['x'] = mua
        df_temp['power'] = (1-norm.cdf(mu0 + norm.ppf(1-alpha)*sem, loc = mua, scale = sem))
        df_temp['n_samples'] = str(samples)
    
        df_power_plot = pd.concat([df_power_plot, df_temp])
    
    
    from matplotlib import rcParams
    
    # figure size in inches
    rcParams['figure.figsize'] = 11.7,4.27
    
    sns.lineplot(
        data=df_power_plot,
        x = 'x',
        y = 'power',
        hue = 'n_samples',
    );
    
    plt.legend(title = 'n of samples', loc='lower right')
    plt.xlabel(r'$\mu_a$');
    plt.title('Plot of power as $\mu_a$ varies')