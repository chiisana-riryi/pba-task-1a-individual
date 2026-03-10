import os
import csv

# constants
app_id : str = "com.valvesoftware.android.steam.community"
scrape_review_count : int = 2000

raw_data_path = "../data/raw/"
reviews_csv_file_template : str = os.path.join(raw_data_path, "reviews-{}-stars.csv")

preprocessed_data_path = "../data/preprocessed"

STOPWORDS = [
"a","about","above","after","again","against","ain","all","am","an","and","any","are",
"aren","aren't","as","at","be","because","been","before","being","below","between",
"both","but","by","can","can't","cannot","could","couldn","couldn't","d","did","didn",
"didn't","do","does","doesn","doesn't","doing","don","don't","down","during","each",
"few","for","from","further","had","hadn","hadn't","has","hasn","hasn't","have",
"haven","haven't","having","he","he'd","he'll","he's","her","here","hers","herself",
"him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into",
"is","isn","isn't","it","it's","its","itself","just","ll","m","ma","me","mightn",
"mightn't","more","most","mustn","mustn't","my","myself","needn","needn't","no",
"nor","not","now","o","of","off","on","once","only","or","other","our","ours",
"ourselves","out","over","own","re","s","same","shan","shan't","she","she'd",
"she'll","she's","should","should've","shouldn","shouldn't","so","some","such",
"t","than","that","that'll","the","their","theirs","them","themselves","then",
"there","these","they","they'd","they'll","they're","they've","this","those",
"through","to","too","under","until","up","ve","very","was","wasn","wasn't","we",
"we'd","we'll","we're","we've","were","weren","weren't","what","what's","when",
"when's","where","where's","which","while","who","who's","whom","why","why's",
"will","with","won","won't","would","wouldn","wouldn't","y","you","you'd","you'll",
"you're","you've","your","yours","yourself","yourselves"
]

def output_csv(data: list, file):
    if (len(data) > 0):
        writer = csv.writer(file)

        header_keys = data[0].keys()
        writer.writerow(header_keys)
        
        for review in data:
            writer.writerow(review.values())