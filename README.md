# Parliamentary AI

This is my little experiment with using a LSTM model in Tensorflow to generate text based on Canadian federal parliamentart debates. 

The debate corpus is hosted online here: https://openparliament.ca/debates

I wrote the `scraper.py` script to download specific parliamentry debate years into .csv files. The `combine_data.ipynb` notebook let me combine the data into a text file that Tensorflow could ingest. 

The `Parliamentary_Model.ipynb` was run on Google Colab using a TPU runtime. Once trained on the data set, I downloaded the `model.h5` file. My local Tensorflow set up uses that weight file to generate debates in `predict.ipynb`.





