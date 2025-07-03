# Sarah Goodyear
# Exam 3

# Sentiment Analysis

# predefined key words
positiveWords = ["good", "happy", "joy", "love", "positive", "amazing", "great"]
negativeWords = ["bad", "sad", "upset", "hate", "negative", "horrible", "anger"]


# function: prints menu
def menu():
    print("\nSentiment Analysis Tool")
    print("1. Analyze a sentence")
    print("2. Get sentiment count")
    print("3. Get most frequent sentiment")
    print("4. Save results to file")
    print("5. Exit")
    

# function: count the number of positive and negative words in text based on key words
def countSentimentWords(text):
    # convert string to lower case
    text = text.lower()
    # get count of positive and negative words based on key words
    positiveCount = sum(1 for word in positiveWords if word in text)
    negativeCount = sum(1 for word in negativeWords if word in text)
    # return counts of positive and negative words
    return positiveCount, negativeCount

# function: analyze sentiment of input text based on key words
def analyzeSentiment(text):
    # get counts of positive and negative words from countSentimentWords func
    positiveCount, negativeCount = countSentimentWords(text)
    # if more positive words, return that it is positive
    if positiveCount > negativeCount:
        return "Positive"
    # if more negative words, return that it is negative
    elif negativeCount > positiveCount:
        return "Negative"
    # if same number positive and negative, return that it is neutral
    else:
        return "Neutral"

# function: determines most frequent sentiment
def getMostSentiment(texts):
    # dictionary to track sentiment counts
    sentimentCounts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    # analyze all sentiments in texts array with for loop and update counts for each analysis
    for text in texts:
        sentiment = analyzeSentiment(text)
        sentimentCounts[sentiment] += 1
    # return senitment with maximum count
    return max(sentimentCounts, key=sentimentCounts.get)

# function: saves seniments to file
def saveToFile(texts):
    # set filename
    filename="sentiment_results.txt"
    # open file
    with open(filename, "w") as file:
        # loop through input array and analyze, writing sentiments to file
        for i, text in enumerate(texts, 1):
            sentiment = analyzeSentiment(text)
            file.write(f"Sentence {1}: {sentiment}\n")
    # print success message
    print(f"Results saved to {filename}")

# main function
def main():
    # empty array to store inputs
    texts = []
    while True:
        # print menu and get user input
        menu()
        choice = input("Choose an option: ")

        # option 1: analyze a sentence & add input to array
        if choice == "1":
            text = input("Enter a sentence: ")
            sentiment = analyzeSentiment(text)
            print(f"Sentiment: {sentiment}")
            texts.append(text)
        # option 2: get sentiment counts & add input to array
        elif choice == "2":
            text = input("Enter a sentence: ")
            positiveCount, negativeCount = countSentimentWords(text)
            print(f"Positive words: {positiveCount}, Negative words: {negativeCount}")
            texts.append(text)
        # option 3: get most frequent sentiment from input array unless empty
        elif choice == "3":
            if texts:
                mostFrequent = getMostSentiment(texts)
                print(f"Most frequent sentiment: {mostFrequent}")
            else:
                # print message if empty
                print("No sentences analyzed yet.")
        # option 4: save input array analysis to file unless empty
        elif choice == "4":
            if texts:
                saveToFile(texts)
            else:
                # print message if empty
                print("No sentences to save.")
        # option 5: exit program
        elif choice == "5":
            print("Exiting program...")
            break
        # invalid choice
        else:
            print("Invalid choice: please enter a valid menu option. ")

if __name__ == "__main__":
    main()
