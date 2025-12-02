HOW TO RUN

Step 1. Install Python 3 on your system.
Step 2. Install required library: pip to install nltk
Step 3. Run the program hash.py
Step 4. Type your message. Type 'exit' or 'quit' to end the chat.


CHOSEN TECHNOLOGIES

Programming language: Python 3
Library for sentiment analysis: NLTK


EXPLANATION OF SENTIMENT LOGIC

The program uses VADER from the nltk library to get a SCORE for each user message.
This score is a number between -1 and +1.
For one message:
If score >= 0.05 sentiment is Positive
If score <= -0.05 sentiment is Negative
If score is between -0.05 and 0.05 sentiment is Neutral
Tier 1 (overall conversation analysis):
Every user message and its sentiment are stored in a list.
At the end, all user messages are joined into one big string.
The same rules above are used on this big string to get the sentiment.
Tier 2 (statement level analysis):
For each user message, the program immediately prints the sentiment Positive, Negative or Neutral.
The compound score of each message is also saved in a list.
At the end mood trend is summarised.


STATUS OF TEAR 2 IMPLEMENTATION

Statement level sentiment: Implemented
Mood trend: Implemented
