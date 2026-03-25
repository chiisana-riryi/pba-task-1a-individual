# Week 2-3
## scraping.ipynb
1. Data scraping 10000 steam reviews
2. Stores the data in ./data/raw/
## preprocess.ipynb
1. Retrieves data from ./data/raw
2. Performs contraction expanding (`contractions`), emoji removal (`emoji`), emoticon removal (`emot`), and stopword removal (`NLTK`) in order
3. Stores the results in ./data/preprocessed