#!/usr/bin/env python
# coding: utf-8

# In[20]:


with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]


# In[43]:


print(data[0:6])


# In[1]:


with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]

def score_word(word):

    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    word_score = 0
    for letter in word:
        word_score += scores[letter.lower()]
    return word_score
    
def valid_word(input_word):
    '''Returns valid words from the text file as a list'''
    words=[]
    for word in data:
        input_word_list = list(input_word)
        for i, letter in enumerate(word):
            if letter in input_word_list:
                input_word_list.remove(letter)
            else:
                break
            if i == len(word)-1:
                words.append(word)
    return words

def wildcards(input_word):
    '''To handle inputs with wildcard characters'''
    
    words = valid_word(input_word.replace('?','').replace('*',''))
    words_scores = [(score_word(word),word.lower()) for word in words]
    n = len(words)
    
    if '?' in input_word:
        for letter in list(string.ascii_uppercase):
            score_letter = score_word(letter)
            new_word = input_word.replace('?',letter)
            if '*' in input_word:
                for next_letter in list(string.ascii_uppercase):
                    new_word = input_word.replace('?',letter).replace('*',next_letter)
                    score_next_letter = score_letter + score_word(next_letter)
                    word_set_list = [(score_word(word)-score_next_letter,word.lower()) for word in valid_word(new_word) if word not in words]
                    words.extend(valid_word(new_word))
                    words=list(set(words))
                    words_scores.extend(word_set_list)
            else:
                words_scores.extend([(score_word(word)-score_letter,word.lower()) for word in valid_word(new_word) if word not in words])
                words.append(new_word)
        return words_scores
    elif '*' in input_word:
        for letter in list(string.ascii_uppercase):
            score_letter = score_word(letter)
            new_word = input_word.replace('*',letter)
            words_scores.extend([(score_word(word)-score_letter,word.lower()) for word in valid_word(new_word) if word not in words])
        return words_scores
    if __name__=='__main__':
    
        begin_time = datetime.datetime.now()
    
    input_word = sys.argv[1].upper()
    
    if len(input_word) < 2:
        
        print("Input too short, number of characters must be greater than 2.")

    elif len(input_word) > 7:
        
        print("Input too big, number of characters must be less than 7.")
        
    elif (input_word.count('?') > 2) or  (input_word.count('*') > 2):
        
        print("Too many wild card character, only 2 allowed.")
        
    elif re.match(r'^[\?\*A-Z]*$',input_word):
        
        words_scores = []
        
        if re.match('[A-Z]*[\?\*]+[A-Z]*',input_word):
            
            words_scores = wildcards(input_word)
            
        else:
            
            words_scores = [(score_word(word), word.lower()) for word in valid_word(input_word)]
            
        output = words_scores
        output = sorted(output, key = lambda x : x[1])
        output = sorted(output, key = lambda x : x[0], reverse=True)
        for word in output:
            print(word)
        print("Total number of words:",len(output))
        
    else:
        
        print("Invalid input, should only contain alpahabets and ?,* wildcards")


# In[ ]:




