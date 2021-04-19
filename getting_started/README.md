# Getting Started

Kaggle has an API which we can use to interact with the data and competitions.

It can be installed on your machine using `pip install kaggle`.

Please read the [docs](https://www.kaggle.com/docs/api "Kaggle API") on how to get started. It is important to set up your API keys in this way so you don't accidently upload them to Kaggle or Github.

You can then either use the Command Line Interface (CLI) detailed in the previous link, or you can use the Kaggle API directly in [Python](https://technowhisp.com/kaggle-api-python-documentation/ "Python Kaggle API").

The file *0_data_download.py* has the code needed to download a zip file of all the articles direct to your device. NOTE: this will only work if you have correctly setup your API keys. This zip file will need unzipped (it is quite a large folder). Then *1_create_dataframe.py* will create a Pandas dataframe of all the articles. Each row is a section with *section_title, text* and *article_id* as the columns. NOTE: please update the file path in the Python file before running. The script outputs a pickle file which can be used in our Python scripts or Juypter notebooks using the following code:

```
!pip3 install pickle5

import pickle5 as pickle

with open("articles_df.pkl", "rb") as fh:

> tweets = pickle.load(fh)
```