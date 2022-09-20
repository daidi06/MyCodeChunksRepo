
data.agg(['sum', 'min'])

data.agg(['sum', 'min', 'max'])

data.agg({'Col_A' : ['sum', 'min'], 
        'Col_B' : ['min', 'max']})
        
data.agg({'Col_A' : ['sum', 'min'],
        'Col_B' : ['min', 'max'],
        'Col_C' : ['sum', 'mean']})

data.agg("mean", axis = "columns")

# Importing reduce for 
# rolling computations
from functools import reduce
  
# define a Custom aggregation 
# function for finding total
def total(series):
      return reduce(lambda x, y: x + y, series)
  
# Grouping the output according to 
# student id and printing the corresponding 
# total marks and to check whether the
# output is correct or not, sum function 
# is also used to print the sum.
data.groupby('stud_id').agg({'marks': ['sum', total]})

# Basic math

agg_func_math = {
    'fare':
    ['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'mad', 'prod']
}
df.groupby(['embark_town']).agg(agg_func_math).round(2)


agg_func_describe = {'fare': ['describe']}
df.groupby(['embark_town']).agg(agg_func_describe).round(2)


# Counting

agg_func_count = {'embark_town': ['count', 'nunique', 'size']}
df.groupby(['deck']).agg(agg_func_count)

# First and last

agg_func_selection = {'fare': ['first', 'last']}
df.sort_values(by=['fare'],
            ascending=False).groupby(['embark_town'
                                        ]).agg(agg_func_selection)                                        

## use idxmax and idxmin to select the index value that corresponds to the maximum or minimum value

agg_func_max_min = {'fare': ['idxmax', 'idxmin']}
df.groupby(['embark_town']).agg(agg_func_max_min)

## to see the rows with the max "fare"

df.loc[df.groupby('class')['fare'].idxmax()]

# You are not limited to the aggregation functions in pandas

from scipy.stats import skew, mode
agg_func_stats = {'fare': [skew, mode, pd.Series.mode]}
df.groupby(['embark_town']).agg(agg_func_stats)

