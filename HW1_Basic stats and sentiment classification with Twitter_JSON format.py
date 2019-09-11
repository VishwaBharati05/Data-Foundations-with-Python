""" hwcode.py
    Write the code for the HW exercises in this file.
"""

import json

# INSTRUCTOR: Your code is clean and easy to understand! Nice work!
# INSTRUCTOR: 35/30


def total_number_of_users(jsonl_filename):
    '''
    Returns the total number of tweets in jsonl_filename
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The total number (int) of tweets
    '''
    # Write code for exercise 1 part 1 here
    total = 0
    uniqname = []
    myFile = open(jsonl_filename,encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip())
        name = lineData["user"]["screen_name"]
        if name not in uniqname:
            uniqname.append(name)
            total += 1
    myFile.close()
    return total

def total_number_of_tweets(jsonl_filename):
    '''
    Returns the total number of tweets in jsonl_filename
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The total number (int) of tweets
    '''
    # Write code for exercise 1 part 1 here
    total = 0
    myFile = open(jsonl_filename,encoding='utf-8')
    for line in myFile:
        '''lineData = json.loads(line.strip())'''
        total += 1
    myFile.close()
    return total


def average_tweets_per_user(jsonl_filename):
    '''
    Returns the average number of tweets per user
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The average number (float) of tweets tweeted by a user
    '''
    # Write code for exercise 1 part 2 here
    average = 0.0
    total_tweets = 0
    total_users = 0
    uniqname = []
    myFile = open(jsonl_filename,encoding='utf-8')
    for line in myFile:
        total_tweets += 1
        lineData = json.loads(line.strip())
        name = lineData["user"]["screen_name"]
        if name not in uniqname:
            uniqname.append(name)
            total_users += 1
    average = float(total_tweets/total_users)
    myFile.close()
    return average

def max_tweets_per_user(jsonl_filename):
    '''
    Returns the max number of tweets made by a user
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The max number (int) of tweets tweeted by a user
    '''
    # Write code for exercise 1 part 2 here
    max_tweets = 0
    repdict = {}
    myFile = open(jsonl_filename,encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip())
        name = lineData["user"]["screen_name"]
        if name in repdict:
            repdict[name] += 1
        else:
            repdict[name] = 1
    max_tweets = repdict[max(repdict, key=(lambda k: repdict[k]))]
    myFile.close()
    return max_tweets

def user_with_most_tweets(jsonl_filename):
    '''
    Returns the user who made the most tweets
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The screen_name (a string) of the user with the most tweets
    '''
    # Wrte code for exercise 1 part 3 here
    user_tweetsalot = ''
    repdict = {}
    myFile = open(jsonl_filename,encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip())
        name = lineData["user"]["screen_name"]
        if name in repdict:
            repdict[name] += 1
        else:
            repdict[name] = 1
    user_tweetsalot = max(repdict, key=(lambda k: repdict[k]))
    myFile.close()
    return user_tweetsalot

def classify_tweets(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Classifies each tweet in jsonl_filename as either having positive
    or negative sentiment.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: A list of predictions (a list of strings "positive"
             or "negative") with a prediction for each tweet
    '''
    # Write code for exercise 2 part 1 here
    predictions = []
    myFile = open(jsonl_filename,encoding='utf-8')
    # INSTRUCTOR: Very clean code!
    for line in myFile:
        pos = 0
        neg = 0
        lineData = json.loads(line.strip())
        text = lineData["full_text"].lower()
        for word in text.split():
            if word in positive_lexicon:
                pos += 1
            elif word in negative_lexicon:
                neg += 1
        if pos > neg:
            predictions.append("positive")
        elif neg > pos:
            predictions.append("negative")
        elif pos == neg:
            # INSTRUCTOR: This could simply be "else", elif not needed
            predictions.append("neutral")
    myFile.close()
    return predictions

def most_negative_tweet(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Return the tweet that is the "most" negative - has the most negative words.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: The most negatives tweet text (string) 
    '''
    most_negative_tweet = ''
    # Write code for exercise 2 part 2 here.
    myFile = open(jsonl_filename,encoding='utf-8')
    most_negative = 0
    for line in myFile:
        lineData = json.loads(line.strip())
        text = lineData["full_text"].lower()
        neg = 0
        pos = 0
        for word in text.split():
            if word in positive_lexicon:
                pos += 1
            elif word in negative_lexicon:
                neg += 1
        if neg > pos:
            if neg > most_negative:
                most_negative = neg
                most_negative_tweet = lineData["full_text"]
    myFile.close()
    return most_negative_tweet
 
def most_positive_tweet(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Return the tweet that is the "most" positive - has the most positive words.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: The most negatives tweet text (string) 
    '''
    # Write code for the exercise 2 part 2 here.
    most_positive_tweet = ''
    myFile = open(jsonl_filename,encoding='utf-8')
    most_positive = 0
    for line in myFile:
        lineData = json.loads(line.strip())
        text = lineData["full_text"].lower()
        neg = 0
        pos = 0
        for word in text.split():
            if word in positive_lexicon:
                pos += 1
            elif word in negative_lexicon:
                neg += 1
        if pos > neg:
            if pos > most_positive:
                most_positive = pos
                most_positive_tweet = lineData["full_text"]  
    myFile.close()
    return most_positive_tweet
 
def most_negative_users(jsonl_filename, positive_lexicon, negative_lexicon, min_tweets):
    '''
    Return the 10 most negative users in the jsonl_filename dataset.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :param int min_tweets: The minimum number of tweets a user must have
                           to be considered the most positive.
    :return: A list of the 10 most negative users (screen names /strings)
             in the dataset.
    '''
    # Write code for the exercise 2 part 3 here.
    # INSTRUCTOR: You can remove the following line
    most_negative_users = ["a user"] * 10
    myFile = open(jsonl_filename,encoding='utf-8')
    total_dict = {}
    mydict = {}
    for line in myFile:
        lineData = json.loads(line.strip())
        text = lineData["full_text"].lower()
        person = lineData["user"]["screen_name"]
        if person in total_dict:
            total_dict[person] += 1
        else:
            total_dict[person] = 1
        neg = 0
        pos = 0
        for word in text.split():
            if word in positive_lexicon:
                pos += 1
            elif word in negative_lexicon:
                neg += 1
        if neg > pos:
            if person in mydict:
                mydict[person] += 1
            else:
                mydict[person] = 1
    top_ten = {}
    sortuser = []
    for i in mydict:
        # INSTRUCTOR: Shouldn't all users be in total_dict?
        if i in total_dict:
            if total_dict[i] >= min_tweets:
                average_score = mydict[i]/total_dict[i]
                top_ten[i] = average_score
    sortuser = sorted(top_ten, key = (lambda k : top_ten[k]), reverse = True)
    most_negative_users = [v for v in sortuser[:10]]
            
    myFile.close()
    return most_negative_users     

def most_positive_users(jsonl_filename, positive_lexicon, negative_lexicon, min_tweets):
    '''
    Return the 10 most positive users in the jsonl_filename dataset.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :param int min_tweets: The minimum number of tweets a user must have
                           to be considered the most positive.
    :return: A list of the 10 most positive users (screen names /strings)
             in the dataset.
    '''
    # Write code for the exercise 2 part 3 here.
    most_positive_users = ['a user'] * 10
    myFile = open(jsonl_filename,encoding='utf-8')
    total_dict = {}
    mydict = {}
    for line in myFile:
        lineData = json.loads(line.strip())
        text = lineData["full_text"].lower()
        person = lineData["user"]["screen_name"]
        if person in total_dict:
            total_dict[person] += 1
        else:
            total_dict[person] = 1
        neg = 0
        pos = 0
        for word in text.split():
            if word in positive_lexicon:
                pos += 1
            elif word in negative_lexicon:
                neg += 1
        if pos > neg:
            if person in mydict:
                mydict[person] += 1
            else:
                mydict[person] = 1
    top_ten = {}
    sortuser = []
    for i in mydict:
        if i in total_dict:
            if total_dict[i] >= min_tweets:
                average_score = mydict[i]/total_dict[i]
                top_ten[i] = average_score
    sortuser = sorted(top_ten, key = (lambda k : top_ten[k]), reverse = True)
    most_positive_users = [v for v in sortuser[:10]]
    myFile.close()
    return most_positive_users

def dates_with_most_tweets(jsonl_filename):
    '''
    Returns a list of dates that had the most tweets.

    :param str jsonl_filename: The file path of the twitter dataset
    :return: A list of the 3 days (strings) with the most tweets
    '''
    # Write code for extra credit
    days_with_most_tweets = ['Wed Oct 04 22:16:18 +0000 2017', 'Wed Oct 05 22:16:18 +0000 2017', 'Wed Oct 06 22:16:18 +0000 2017']
    myFile = open(jsonl_filename,encoding='utf-8')
    datedict = {}
    sortdict = {}
    for line in myFile:
        lineData = json.loads(line.strip())
        dates = lineData["created_at"]
        date = dates[0:10]
        if date[4:7] == "Oct":
            if int(date[8:10]) >= 4:
                if date in datedict:
                    datedict[date] += 1
                else:
                    datedict[date] = 1
        elif date[4:7] == "Nov":
            if int(date[8:10]) <= 7:
                if date in datedict:
                    datedict[date] += 1
                else:
                    datedict[date] = 1
    sortdict = sorted(datedict.items(), key=lambda x: x[1], reverse = True)  
    days_with_most_tweets.clear()
    for a in sortdict[0:3]:        
        days_with_most_tweets.append(a[0])
    myFile.close()    
    return days_with_most_tweets

def dates_with_least_tweets(jsonl_filename):
    '''
    Returns a list of dates that had the least tweets.

    :param str jsonl_filename: The file path of the twitter dataset
    :return: A list of the 3 days (strings) with the least tweets
    '''
    # Write code for extra credit
    days_with_least_tweets = ['Wed Oct 04 22:16:18 +0000 2017', 'Wed Oct 05 22:16:18 +0000 2017', 'Wed Oct 06 22:16:18 +0000 2017']
    myFile = open(jsonl_filename,encoding='utf-8')
    datedict = {}
    sortdict = {}
    for line in myFile:
        lineData = json.loads(line.strip())
        dates = lineData["created_at"]
        date = dates[0:10]
        if date[4:7] == "Oct":
            if int(date[8:10]) >= 4:
                if date in datedict:
                    datedict[date] += 1
                else:
                    datedict[date] = 1
        elif date[4:7] == "Nov":
            if int(date[8:10]) <= 7:
                if date in datedict:
                    datedict[date] += 1
                else:
                    datedict[date] = 1
    sortdict = sorted(datedict.items(), key=lambda x: x[1])  
    days_with_least_tweets.clear()
    for a in sortdict[0:3]:        
        days_with_least_tweets.append(a[0]) 
    myFile.close()
    return days_with_least_tweets 

