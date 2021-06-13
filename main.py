import pandas as pd

# prompts user for the file location
filename = input("Please input the filename or directory route: ")

# reads in the data from the file
in_csv = pd.read_csv(filename)

# goes ahead and replaces any spaces in column names with underscores so they're easier to work with
in_csv.columns = in_csv.columns.str.replace(' ', '_')

# Sorts by version number then deletes all but the last version number for
# rows with duplicate IDs and Insurance Companies
no_dupes = in_csv.sort_values('Version').drop_duplicates(['User_Id', 'Insurance_Company'], keep='last')

# groups by insurance company and for each unique company outputs a CSV with
# it's data
for k, v in no_dupes.groupby('Insurance_Company'):
    v.to_csv(f'{k}.csv')

