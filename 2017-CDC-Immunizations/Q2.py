import pandas as pd

def average_influenza_doses():
    # dataframe
    df = pd.read_csv('NISPUF17.csv', usecols=['CBF_01', 'P_NUMFLU'])
    # create two dataframes: bfed (breastfed), nbfed (not breastfed)
    bfed = df.loc[df['CBF_01'] == int(1)]
    nbfed = df.loc[df['CBF_01'] == int(2)]
    # get number of vaccine shots for each group
    vs_bfed = bfed['P_NUMFLU'].dropna()
    vs_nbfed = nbfed['P_NUMFLU'].dropna()
    # get average
    len_bfed = vs_bfed.shape[0]
    len_nbfed = vs_nbfed.shape[0]
    ave_bfed = vs_bfed.mean()
    ave_nbfed = vs_nbfed.mean()
    return ave_bfed, ave_nbfed

print(average_influenza_doses())