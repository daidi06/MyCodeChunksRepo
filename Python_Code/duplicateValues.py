# How to Find Duplicates in Pandas DataFrame

## find duplicate rows across all columns
duplicateRows = df[df.duplicated()]

## find duplicate rows across specific columns
duplicateRows = df[df.duplicated(['col1', 'col2'])]

#use the argument keep=’last’ to display the first duplicate rows instead of the last. keep{"first","last",False}
duplicateRows = df[df.duplicated(keep='last')]

# dropping ALL duplicate values
data.drop_duplicates(subset="First Name", keep=False, inplace=True)