# Checking for missing values using isnull() and notnull()

## using isnull() function 
data.isnull()

## creating bool series True for NaN values
bool_series = pd.isnull(data["Gender"])
   
## filtering data
## displaying data only with Gender = NaN
data[bool_series]

# Checking for missing values using notnull()

## using notnull() function
data.notnull()

## creating bool series True for NaN values
bool_series = pd.notnull(data["Gender"])
   
## filtering data
## displaying data only with Gender = Not NaN
data[bool_series]

# Filling missing values using fillna(), replace() and interpolate()

## filling missing value using fillna() 
data.fillna(0)

## filling a missing value with
## previous ones 
data.fillna(method ='pad')

## filling  null value using fillna() function 
data.fillna(method ='bfill')

## filling a null values using fillna()
data["Gender"].fillna("No Gender", inplace = True)

## will replace  Nan value in dataframe with value -99 
data.replace(to_replace = np.nan, value = -99)

## to interpolate the missing values
data.interpolate(method ='linear', limit_direction ='forward')

# using dropna() function 
data.dropna()

# Dropping rows if all values in that row are missing.
## using dropna() function   
data.dropna(how = 'all')

# Dropping columns with at least 1 null value. 
## using dropna() function    
df.dropna(axis = 1)

# Heatmap
sns.heatmap(dataMD.isnull(), cbar=False)
