# Parliamentary AI

This is my little experiment with using a LSTM model in Tensorflow to generate text based on Canadian federal parliamentart debates. 

The debate corpus is hosted online here: https://openparliament.ca/debates

I wrote the `scraper.py` script to download specific parliamentry debate years into .csv files. The `combine_data.ipynb` notebook let me combine the data into a text file that Tensorflow could ingest. 

The `Parliamentary_Model.ipynb` was run on Google Colab using a TPU runtime. Once trained on the data set, I downloaded the `model.h5` file. My local Tensorflow set up uses that weight file to generate debates in `predict.ipynb`.

### Sample Output

```
Liberal: Mr. Speaker, I will listen to last once again.

 -- 

NDP: Mr. Speaker, I do not know why The bill begs in unada all that the Liberals remember the same massive current interference be here and the police recently called Western Alberta to help the rail systems that exist it comes for just disturbing a pan-Canadian.Bill would add a vacation site that really lost. He is understanding that the Liberal Party has indeed raised true in a surprise here than millions yet no action. He has the criminal pharmacare protection program with this petition, putting over $1.2 million. The experience a decision that all registry, and low the Prime Minister's Office, and, if that is why I will have the Prime Minister and the NDP, should out there. If Canada agree that the minister's questions have expressed by a crossing at free trade agreement with exercising existing families from a free and railway.First, I rise to one thing I am of it.Many of them want incident.

 -- 
``



