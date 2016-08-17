import pandas as pd

InputData = pd.read_excel(r"/Users/Emily/Desktop/Python/TestData/DataInput.xlsx", sheetname='Sheet1')

InputData['Cost'] = InputData['Price']*InputData['Amount']

InputData.to_excel(r"/Users/Emily/Desktop/Python/TestData/DataOuput.xlsx", sheet_name='Result',startrow = 1, startcol = 1,index=False)
