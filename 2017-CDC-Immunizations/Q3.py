import pandas as pd

def chickenpox_by_sex():
    # dataframe
    df = pd.read_csv('NISPUF17.csv', usecols=['SEX', 'HAD_CPOX', 'P_NUMVRC'])
    # create two dataframes: male and female
    male = df.loc[df['SEX'] == int(1)]
    female = df.loc[df['SEX'] == int(2)]
    # get only the ones who received at least a single vaccine shot for each group
    m_vac = male.loc[male['P_NUMVRC'] > 0]
    f_vac = female.loc[female['P_NUMVRC'] > 0]
    # among the two vaccinated groups
    # get those who contracted chickenpox (m_cpox, f_cpox) 
    # and those who did not contract it (m_ncpox, f_ncpox)
    m_cpox = m_vac.loc[m_vac['HAD_CPOX'] == int(1)]
    m_ncpox = m_vac.loc[m_vac['HAD_CPOX'] == int(2)]
    f_cpox = f_vac.loc[f_vac['HAD_CPOX'] == int(1)]
    f_ncpox = f_vac.loc[f_vac['HAD_CPOX'] == int(2)]
    # get the cpox-ncpox ratio per gender
    male_ratio = m_cpox.shape[0] / m_ncpox.shape[0]
    female_ratio = f_cpox.shape[0] / f_ncpox.shape[0]
    return {'male': male_ratio, 'female': female_ratio}

assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."