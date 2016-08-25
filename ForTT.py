import pandas as pd


data_file1 = pd.read_excel(r"/Users/Emily/Desktop/Python/TestData/file1.xlsx",parse_cols = "A,B,C")
data_file1 = pd.read_excel(r"/Users/Emily/Desktop/Python/TestData/file1.xlsx")
data_filew = pd.read_excel(r"/Users/Emily/Desktop/Python/TestData/filew.xlsx")

data_filew['a1'] = data_filew['b1']

result = pd.merge(data_file1, data_filew, how='outer', on=['a1']).fillna(0).sort_values(by = 'a1', ascending = True)

result['Minus'] = result['b13'] - result['a13']

result = result[['a1','Minus','b12','a13','b13']]

result[result['Minus'] > 0]

print result