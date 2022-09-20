# filter pandas dataframe using another dataframe
## You can do this efficiently using isin on a multiindex constructed from the desired columns
### Filter df1 base on df2 rows

#### 1st method
keys = list(df2.columns.values)
i1 = df1.set_index(keys).index
i2 = df2.set_index(keys).index
df1[~i1.isin(i2)]

#### 2nd method
# create a column marking df2 values
df2['marker'] = 1

# join the two, keeping all of df1 's indices
joined = pd.merge(df1, df2, on = ['c', 'l'], how = 'left')
joined

# extract desired columns where marker is NaN
joined[pd.isnull(joined['marker'])][df1.columns]

df1 = df1[~df1.index.isin(df2.index)]

#### 3rd method would be to do left join with the argument indicator=True
df1.merge(df2, on = ['c', 'l'], how = 'left', indicator = True)