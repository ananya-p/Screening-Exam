import pandas as pd
from tabulate import tabulate

one_df = pd.read_csv('Q2 csv1.csv')     #reading the first .csv file into a dataframe
one_df = one_df[one_df['Time'].isna() == False]     #identifying the common header and verifying of no duplicate values

two_df = pd.read_csv('Q2 csv2.csv')     #reading the second .csv file into a dataframe
two_df = two_df[two_df['Time'].isna() == False]     #identifying the common header and verifying of no duplicate values

final = pd.merge(one_df,two_df, left_on='Time', right_on='Time', how='left')    #merging both the dataframes into a single dataframe by specifying the left join
final.to_csv('final.csv', index=False)      #coverting the merged dataframe into a .csv file and removing the index values

final = pd.read_csv('final.csv')    #reading the final csv file into a dataframe   
print(tabulate(final, headers='keys',tablefmt='psql'))      #view the csv file in a tabular format