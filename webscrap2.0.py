import pandas as pd

collist = ['Team name','Intuitiveness','Creativity','Responsiveness','Novelilty'] #column names list
csvlist = ['jacob.csv','cyril.csv'] # csv files list

# Dictionary variables
Intuitiveness = 0
Creativity = 0
Responsiveness = 0
Novelilty = 0

# initalize Dictionary
dict = {
        'Intuitiveness':Intuitiveness,
        'Creativity':Creativity,
        'Responsiveness':Responsiveness,
        'Novelilty':Novelilty
        }

#initalize DataFrame
df = pd.DataFrame()

# Read through each file        

for i in range(len(csvlist)):
    df = pd.read_csv(csvlist[i],usecols=collist,skipinitialspace=True)
    print(df.iloc[0:21])

# jf = pd.read_csv('jacob.csv',usecols=collist,skipinitialspace=True,) # set path of your csv
# cf = pd.read_csv('cyril.csv',usecols=collist,skipinitialspace=True) # set path of your csv

#print(jf.iloc[0:21])
#print("################################################################################")
#print(cf.iloc[0:21])



