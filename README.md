Aspect based sentiment analysis also called ABSA in short. I try doing this project using LDA and Naive Bayes model.

This is a task which classify topic and sentiment, and then we look proportion of sentiments in each topic. In this code, I try ABSA task of e-commerce application review. THe data was taken by scraping Google play Store review (scraping play store.py).

I did splitting sentence first by dot because some sentences in each document have different topic and sentiment (split kalimat.ipynb). LDA model used for getting how many topics on the corpus by seeing the coherence score (Coherence.ipynb). I also evaluate the number topic using LDA sklearn. After getting the number of topic and its name, I give manual label for topic, also for sentiment.
To get the accuracy score for this classification, I use Naive Bayes model.

