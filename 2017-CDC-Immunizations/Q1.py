import pandas as pd

def proportion_of_education():
    # dataframe
    df = pd.read_csv('NISPUF17.csv')
    # get the total number of rows within the EDUC1 column (doesn't matter which column anyway)
    total_rows = df['EDUC1'].shape[0]
    # less than high school
    lt_hs = (df['EDUC1'].values == int(1)).sum()
    # high school
    hs = (df['EDUC1'].values == int(2)).sum()
    # more than high school but not college
    gt_hs = (df['EDUC1'].values == int(3)).sum()
    # college
    college = (df['EDUC1'].values == int(4)).sum()
    # results
    return {
        'less than high school': (lt_hs / total_rows),
        'high school': (hs / total_rows),
        'more than high school but not college': (gt_hs / total_rows),
        'college': (college / total_rows)
    }

assert type(proportion_of_education())==type({}), "You must return a dictionary."
assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."