def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    # read dataset
    df = pd.read_csv('NISPUF17.csv', usecols=['HAD_CPOX', 'P_NUMVRC'])
    # dataframe: those who had and never had chickenpox
    samples = df.loc[df['HAD_CPOX'] <= int(2)]
    # drop entries with NaNs
    samples = samples.dropna()
    # set up columns
    had_chickenpox_column = samples['HAD_CPOX']
    num_chickenpox_vaccine_column = samples['P_NUMVRC']
    # correlation
    corr, pval = stats.pearsonr(had_chickenpox_column, num_chickenpox_vaccine_column)
    return corr

print(corr_chickenpox())