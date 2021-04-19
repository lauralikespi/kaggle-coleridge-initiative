# Getting Started

Kaggle has an API which we can use to interact with the data and competitions.

It can be installed on your machine using `pip install kaggle`.

Please read the [docs](https://www.kaggle.com/docs/api "Kaggle API") on how to get started. It is important to set up your API keys in this way so you don't accidently upload them to Kaggle or Github.

You can then either use the Command Line Interface (CLI) detailed in the previous link, or you can use the Kaggle API directly in [Python](https://technowhisp.com/kaggle-api-python-documentation/ "Python Kaggle API").

The file *0_data_download.py* has the code needed to download a zip file of all the articles direct to your device. NOTE: this will only work if you have correctly setup your API keys. This zip file will need unzipped (it is quite a large folder). Then *1_create_dataframe.py* 