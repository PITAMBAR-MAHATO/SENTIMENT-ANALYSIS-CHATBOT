import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia =SentimentIntensityAnalyzer()

def sentiment(text):
    score =sia.polarity_scores(text)['compound']
    if score >=0.05:
        label ="Positive"
    elif score <=-0.05:
        label ="Negative"
    else:
        label ="Neutral"
    return label, score

def reply(sent):
    if sent =="Negative":
        return "Sorry to hear that."
    elif sent =="Positive":
        return "That sounds good!"
    else:
        return "Okay, got it."
    
def overall_sentiment(chat):
    if not chat:
        return "Neutral"
    text =""
    for i in chat:
        text +=" " + i[0]
    label, _ =sentiment(text)
    return label

def mood_trend(score):
    if not score:
        return "no data"
    start =score[0]
    end =score[-1]
    diff =end - start
    if diff > 0.1:
        return "mood got better"
    elif diff < -0.1:
        return "mood got worse"
    else:
        return "mood almost same"

def main():
    print("Welcome to Sentiment Analysis Chatbot!")
    print("To exit, type 'exit' or 'quit'")
    chat_history =[]
    score_list =[]

    while True:
        user =input("User :")
        if user.strip().lower() in ["exit","quit"]:
            break
        s_label, score =sentiment(user)
        chat_history.append((user, s_label))
        score_list.append(score)
        print("→ Sentiment:", s_label)
        bot_reply=reply(s_label)
        print("Chatbot:", bot_reply)
        print()
    
    overall =overall_sentiment(chat_history)
    trend =mood_trend(score_list)

    print("Overall Mood Sentiment Analysis")
    print("Overall Sentiment: ", overall,)
    print("Mood Trend: ", trend)

if __name__ =="__main__":
    main()
