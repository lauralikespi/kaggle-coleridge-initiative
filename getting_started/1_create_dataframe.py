# Code to convert all the JSON files with articles into on Pandas dataframe

## Import the necessary libraries
import pandas as pd # pandas
from os import listdir # os
from os.path import isfile, join

## The file path to the folder with all the JSON files (this will need updating)
my_path = "/Users/laura/Documents/Coding/kaggle/kaggle-coleridge-initiative/coleridgeinitiative-show-us-the-data/train"

## Code to go through the directory (or folder) and list any files
only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

## Create an empty dataframe with three columns
df = pd.DataFrame(columns=['section_title','text','article_id'])

## For each of the files, read in the JSON and add a column with the article ID
for file_name in only_files:
    file_location = str(my_path) + str("/") + str(file_name) # create the file path
    # print(file_location) # print file location
    article_df = pd.read_json(file_location) # read the JSON to a dataframe
    article_df['article_id'] = str(file_name[:-5]) # add column with article ID, remove .json from end
    # print(article_df.head()) # print top 5 lines
    df = df.append(article_df, ignore_index=True, sort=False) # append to bottom of previous dataframe, ignore index or rows will have the same index in final dataframe

print(df.shape) # (258714,3) (rows, columns)
print(df.describe()) # print out a summary of the columns
print(df.head()) # print out top 5 lines