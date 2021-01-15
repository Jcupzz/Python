import pandas as pd

collist = ['Team name', 'Intuitiveness', 'Creativity',
           'Responsiveness', 'Novelilty']  # column names list
csvlist = ['jacob.csv', 'cyril.csv']  # csv files list

jd = pd.read_csv('jacob.csv',usecols=collist,skipinitialspace=True)
cd = pd.read_csv('cyril.csv',usecols=collist,skipinitialspace=True)

con = pd.concat([jd,cd])

result = con.set_index('Team name').sum(level=0)

print(result)


# for i in range(len(csvlist)):
#    result = pd.concat([pd.read_csv(csvlist[i],usecols=collist,skipinitialspace=True)])
#result.to_csv("resultcsv")  