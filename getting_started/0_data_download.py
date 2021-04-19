from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate() # requires your computer to have a JSON file with your API keys

api.competition_download_files('coleridgeinitiative-show-us-the-data') # downloads as a zip, you will need to unzip

print("Done")