import pandas as pd


# Generic function that calls specific function on each element in dataframe.
def generic_func(specific_func):

    df = get_csv_file()
    songs = df[df.Title]
    for i in len(df[df.SongNumber]):
        specific_func(songs[i])

# Returns CSV file converted from HD5 file
def get_csv_file():
    df = pd.read_csv('/Users/ashank/Documents/Song Recommendation/SongCSV.csv', header=0)
    return df


# Specific function to call on each element in dataframe.
def specific_func():
    return -1
