import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

stemmer = SnowballStemmer('english')  # why ?
stop_words = set(stopwords.words("english"))   # set()

# read raw file:  -> DataFrame
train_set = pd.read_csv("./survey2.csv")
#train_set.head()

# get the 'comment column':
#train_text = train_set["comment_text"]
train_text = train_set.loc[:,"S2-Structure"]
#train_text = train_set.loc[:,"S2-Delivery"]
#train_text = train_set.loc[:,"S2-VisualAids"]



train_array = train_set["S2-Structure"].values  # -> ndarray  (159571,)
#train_array = train_set["S2-Delivery"].values  # -> ndarray  (159571,)
#train_array = train_set["S2-VisualAids"].values  # -> ndarray  (159571,)
# A list to store cleaned text
train_cleaned_comment_list = [] 



def clean_comment(comment):
    #reserve a to z and A to Z, other characters are replaced by ' '
    for _ in train_set:
        if _ == '\n':
            pass
        else:
            re_train = str(re.sub("[^a-zA-Z]"," ", str(comment)))
            #make words in lower case
            tokened_train = word_tokenize(re_train.lower())
            #reserve the words which are in tokenen_train but not in stop_words
            #stoped_train = [_ for _ in tokened_train if _ not in stop_words]
            #integrate the words by using ' '
            stoped_train_str = " ".join(tokened_train) # -> string
            #return the results of cleaned data
            return stoped_train_str


'''
Input cleaned data into lists and files
'''
# writelines to filess
count = 0
my_file = open('./cleaned_data/cleaned_survey2.csv','w')
for _ in train_array:
    i = clean_comment(_)
    print(i)
    train_cleaned_comment_list.append(i)
    my_file.writelines(i)
    my_file.writelines('\n')
    count+=1
my_file.close()
print("The length of the list(train): ",len(train_cleaned_comment_list))
print("The number of commnents(train): ", count)

