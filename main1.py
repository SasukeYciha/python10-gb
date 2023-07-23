import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
 
print('')

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)


#import random
#import pandas as pd
##lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#print(lst)
#print()
#data = pd.DataFrame({'whoAmI':lst})
#data.loc[data['whoAmI'] == 'robot', 'robot_group'] = '1'
#data.loc[data['whoAmI'] != 'robot', 'robot_group'] = '0'
#data.loc[data['whoAmI'] == 'human', 'human_group'] = '1'
#data.loc[data['whoAmI'] != 'human', 'human_group'] = '0'

#data.head(n=20) 