# Spotify_ML

#### This goal of this project is to try and train a model to estimate the numbers of streams of a song based on certain features. https://zenodo.org/records/10253415 is the metadata for the data, and you can run the file CSV_Download.py to programmatically download it. Running: Interactive_chart.py allows you to look at an interactive dash chart. Lastly, my attmpt at creating the model is in Machine_Learning.ipynb. 


##### The dataset I chose is a music dataset titled “Spotify and YouTube”. I found it on Kaggle, and it provides the satistics of the top 10 songs of different Spotify artists and their corresponding YouTube videos. The data was retrieved using the applications’ respective APIs. There is north of 17K different tracks (2K different artists) and 26 different variables (or features). Some of those features are generic such as song title and artist and album name, but the ones I want to focus mostly on are “danceability”, “speechiness”, “liveness”, “tempo”, etc. This data is presented in the form of an excel .csv file, which would allow me to easily import into python IDEs. Also, the data set is in the public domain (CC0: Public Domain). My main goal from this data set is to be able to train a model to recommend new music based on the features of liked songs.

## Thank you!