# Parliamentary AI

This is my little experiment with using a character-based RNN in Tensorflow to generate text based on Canadian federal parliamentart debates. 

The debate corpus is hosted online here: https://openparliament.ca/debates

I wrote the `scraper.py` script to download all of the parliaments recorded debates between 1996 and 2018 into .csv files in a `/data/` folder. 

I will be following [this](https://www.tensorflow.org/tutorials/sequences/text_generation) Tensorfow tutorial.

## Installation & Setup

I'm using Tensorflow's Docker image to run my notebooks so the set-up goes as:

```bash

git clone https://github.com/jtloong/parliamentary-ai
cd parliamentary-ai
docker pull tensorflow/tensorflow

```

