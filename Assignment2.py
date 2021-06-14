# Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

# This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

#     {"less than high school":0.2,
#     "high school":0.4,
#     "more than high school but not college":0.2,
#     "college":0.2}

import pandas as pd 

def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    df = pd.read_csv('assets/NISPUF17.csv', index_col = 0)
    
    less_HS = (df[df['EDUC1'] == 1].shape[0])/df['EDUC1'].shape[0]
    HS = (df[df['EDUC1'] == 2].shape[0])/df['EDUC1'].shape[0]
    more_HS = (df[df['EDUC1'] == 3].shape[0])/df['EDUC1'].shape[0]
    college = (df[df['EDUC1'] == 4].shape[0])/df['EDUC1'].shape[0]

    edu_dict = dict({'less than high school': less_HS,'high school': HS, 'more than high school but not college': more_HS, 'college': college})
    
    return edu_dict

    raise NotImplementedError()
    
print (proportion_of_education())


# Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

# This function should return a tuple in the form (use the correct numbers:

# (2.5, 0.1)

def average_influenza_doses():
    # YOUR CODE HERE - CBF_01, P_NUMFLU
    df = pd.read_csv('assets/NISPUF17.csv', index_col = 0)
    yes_BM = df[(df['CBF_01']==1) & (df['P_NUMFLU']>=0)].loc[:,['P_NUMFLU','CBF_01']].dropna()
    no_BM = df[(df['CBF_01']==2) & (df['P_NUMFLU']>=0)].loc[:,['P_NUMFLU','CBF_01']].dropna()
    
    avg_yes = yes_BM['P_NUMFLU'].sum()/ (yes_BM.shape[0])
    avg_no = no_BM['P_NUMFLU'].sum()/ (no_BM.shape[0])
    
    return (avg_yes, avg_no)
    
    raise NotImplementedError()

print(average_influenza_doses())



# It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.

# This function should return a dictionary in the form of (use the correct numbers):

#     {"male":0.2,
#     "female":0.4}

# Note: To aid in verification, the chickenpox_by_sex()['female'] value the autograder is looking for starts with the digits 0.0077.

import pandas as pd
def chickenpox_by_sex():
    # YOUR CODE HERE
    # HAD_CPOX , SEX, P_NUMVRC
    df = pd.read_csv('assets/NISPUF17.csv', index_col = 0)
#     num_vacc = (df['P_NUMVRC']>0).shape[0]
#     num_no_vacc = (df['P_NUMVRC']==0).shape[0]
#     total_vacc = num_vacc + num_no_vacc
    
    male_cpox = (df[(df['HAD_CPOX']==1) & (df['SEX'] == 1) & (df['P_NUMVRC'] > 0)].shape[0])
    male_no_cpox = (df[(df['HAD_CPOX']==2) & (df['SEX'] == 1) & (df['P_NUMVRC'] > 0)].shape[0])
    female_cpox = (df[(df['HAD_CPOX']==1) & (df['SEX'] == 2) & (df['P_NUMVRC'] > 0)].shape[0])
    female_no_cpox = (df[(df['HAD_CPOX']==2) & (df['SEX'] == 2) & (df['P_NUMVRC'] > 0)].shape[0])
    
    male = male_cpox / male_no_cpox
    female = female_cpox / female_no_cpox
    
    results = dict({'male': male, 'female': female})
    return results

    raise NotImplementedError()

print (chickenpox_by_sex())


# A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).

# Some notes on interpreting the answer. The had_chickenpox_column is either 1 (for yes) or 2 (for no), and the num_chickenpox_vaccine_column is the number of doses a child has been given of the varicella vaccine. A positive correlation (e.g., corr > 0) means that an increase in had_chickenpox_column (which means more no’s) would also increase the values of num_chickenpox_vaccine_column (which means more doses of vaccine). If there is a negative correlation (e.g., corr < 0), it indicates that having had chickenpox is related to an increase in the number of vaccine doses.

# Also, pval is the probability that we observe a correlation between had_chickenpox_column and num_chickenpox_vaccine_column which is greater than or equal to a particular value occurred by chance. A small pval means that the observed correlation is highly unlikely to occur by chance. In this case, pval should be very small (will end in e-18 indicating a very small number).

# [1] This isn’t really the full picture, since we are not looking at when the dose was given. It’s possible that children had chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate the timing of the dose?


def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    # this is just an example dataframe
#     df=pd.DataFrame({"had_chickenpox_column":np.random.randint(1,3,size=(100)),
#                    "num_chickenpox_vaccine_column":np.random.randint(0,6,size=(100))})

    # here is some stub code to actually run the correlation
#     corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
    
    # just return the correlation
    #return corr
    
    # YOUR CODE HERE
    df = pd.read_csv('assets/NISPUF17.csv', index_col = 0)
    
    df=df[df['HAD_CPOX'] < 3].loc[:,['HAD_CPOX','P_NUMVRC']].dropna()
#     print(df)

    df.columns=['had_chickenpox_column','num_chickenpox_vaccine_column']
    
    corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
    
    return corr
    raise NotImplementedError()
print(corr_chickenpox())