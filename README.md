# Twitter_Sentiment_Analysis

- Twitter is a big storehouse of human emotions and how people react to situations every second. This emotional data can be used for sentiment analysis.
- We use the process of tokenization ie; by dividing th received tweet into different parts.
- By the model called as Bag of Words model we count the no. of times a word has been repeated in a tweet and the appraoch to this program is Lexicon Based. 
- We use [Twitter Developer](https://developer.twitter.com/apps) and make an account in twitter api then we get 4 tokens 2 Consumer API keys and 2 Access token & access token secret as the two main keys for the same. 
- We use the twitter api system connect it to the sentiment analyzer and use it in the script. 
- The to main libraries in this program are tweepy and textblob.
- In the end we get to factors to measure polarity means emotions expressed in a sentence eg:emotional negative (-2), rational negative (-1), neutral (0), rational positive (+1), and emotional positive (+2) and subjectivity means personal feeling, views or beliefs.

**Step 1:** Import all required modules and libraries

**Step 2:** Insert you consumer key, consumer secret, access token and access token secret from your twitter developer account. Authorize them. Import your twitter api to code.

**Step 3:** Define which sentiments represent what words and their alternatives.

**Step 4:** Using textblob define polarity of sentiment in dictionary.

**Step 5:** Test the analyzer and export the result in a csv format.

**Results**

![sentiment](https://github.com/ShrishtiHore/Twitter_Sentiment_Analysis/blob/master/twitter_sentiment_analysis_output.PNG)

![tweet](https://github.com/ShrishtiHore/Twitter_Sentiment_Analysis/blob/master/tweet.PNG)

**References**
1. https://github.com/rishavinvincible/Siraj-Raval-
2. https://www.youtube.com/watch?v=o_OZdbCzHUA
3. https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa3hWUlIyU1lLSnN2V2tvWEFUVmFxLUR0Slk1Z3xBQ3Jtc0tsS3l5YjdsOUpsaktUNV9kcmFoSHI2bWdHTXAtQWI2dEREeVFsaXl2VkhpNTNhT01ScE9vb0gwWFNLSGE1SDJycjV0RUE0dlJhYzJvaUlwNFdEMWZMZ09SdGxyeEhqel9IVlkwTUZnYkJJNmNVMVhBZw&q=https%3A%2F%2Fgithub.com%2FllSourcell%2Ftwitter_sentiment_challenge
