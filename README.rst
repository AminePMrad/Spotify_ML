.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/ML_Project.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/ML_Project
    .. image:: https://readthedocs.org/projects/ML_Project/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://ML_Project.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/ML_Project/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/ML_Project
    .. image:: https://img.shields.io/pypi/v/ML_Project.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/ML_Project/
    .. image:: https://img.shields.io/conda/vn/conda-forge/ML_Project.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/ML_Project
    .. image:: https://pepy.tech/badge/ML_Project/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/ML_Project
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/ML_Project

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

==========
ML_Project
==========


    This goal of this project is to try and train a model to estimate the numbers of streams of a song based on certain features. https://zenodo.org/records/10253415 is the metadata for the data, and you can run the file CSV_Download.py to programmatically download it. Running: Interactive_chart.py allows you to look at an interactive dash chart. Lastly, my attmpt at creating the model is in Machine_Learning.ipynb. 

    


The dataset I chose is a music dataset titled “Spotify and YouTube”. I found it on Kaggle, and it provides the satistics of the top 10 songs of different Spotify artists and their corresponding YouTube videos. The data was retrieved using the applications’ respective APIs. There is north of 17K different tracks (2K different artists) and 26 different variables (or features). Some of those features are generic such as song title and artist and album name, but the ones I want to focus mostly on are “danceability”, “speechiness”, “liveness”, “tempo”, etc. This data is presented in the form of an excel .csv file, which would allow me to easily import into python IDEs. Also, the data set is in the public domain (CC0: Public Domain). My main goal from this data set is to be able to train a model to recommend new music based on the features of liked songs.
Thank you!


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
