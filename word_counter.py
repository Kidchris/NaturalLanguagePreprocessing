# %% [markdown]
# Abhijit Banerjee, the Indian-born American is the Nobel prize winner for the year 2019 in Economics. He retrieved a text from the web for his research work. Unfortunately, he was surprised to see there were many duplicate words present in the text. He is in need of a text which contains only unique words. Help Abhijit to write a python code to achieve this task without using inbuilt methods. If there are no duplicates, print the text as it is.
# 
# Input Format:
# 
# The first line contains the text. Assume there are no special characters in the text and the text contains words separated by spaces
# 
# Output Format:
# 
# In the first line, print the duplicate word and the number of times it occurs in the text, if any, separated by a space.
# 
# In the next line, print the indices of the duplicate words in the text, with the first index being 0, separated by spaces(if more than one).
# 
# Repeat the above two steps for other duplicate words, if any.
# 
# In the last line, print the updated text containing unique words.
# 
# If no duplicate words are found then just print the text as it is.

# %%
import string
punct = string.punctuation

table = str.maketrans("", "", punct)
def dup_counter(text):
    words = {}
    splitted = text.split()
    for w in splitted:
        words[w] = splitted.count(w)

    print(words)

def indexes(text):
    ind = {}
    splitted = text.split()
    i = 0
    indexes = []
    for w in splitted:
        indexes.append(i)
        # to be implemented
        i += 1
    print(ind)  

# %%
dup_counter("Abhijit Banerjee, the Indian-born is is is is is American is the Nobel prize winner for the year 2019 in Economics")
indexes("Abhijit Banerjee, the Indian-born is is is is is American is the Nobel prize winner for the year 2019 in Economics")

# %%


# %%
dir(list)


