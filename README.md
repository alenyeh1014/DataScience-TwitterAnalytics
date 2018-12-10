# NBA Predictions with Twitter
Hi all, this is a Data Science Project ! - Twitter Analytics with Machine Learning and Deep Learning Methodologies.


### Project Objective

* The purpose of this project is to apply Machine Learning and Deep Learning Methodologies in Social Media Analytics such as 
Twitter in order to forecast NBA result predictions in this project.


### Partners

* Ming-Ting Hsieh, Chieh Shih
* Website for partners: [Ming-Ting], [https://github.com/Cosoet]
* Website for partners: [Chieh], [https://github.com/cshih685]


### Methods Used

* Inferential Statistics
* Web Scraping
* Data Wrangling
* Data Visualization
* Machine Learning
* Deep Learning Learning
* Predictive Modeling


### Algorithms Used

- Supervised Learning: 
  - Naive Bayes Classifiers (NB)
  - Support Vector Machines (SVM)
  
- Unsupervised Learning: 
  - K-means Clustering
  - Latent Dirichlet Allocation (LDA)
  
- Deeping Learning: 
  - Convolutional Neural Network (CNN)


### Technologies and Packaged Used

* Python, Jupyter Notebook
* Numpy, Pandas, Sklearn, Nltk
* Matplotlib, Scipy, Seaborn, Keras


### Project Description

* Motivation:

  - It is simple and straightforward since we are all sport fans and twitter lovers making a related project seems persuasive and reasonable for us ! 
  - Thus, we would like to apply ML and DL methodologies to predict the NBA game results from Twitter. 
  - Furthermore, the accuracy of each methodology is also crucial and practical for users friendly.  
  
* Details:

  - There are total 30 teams in the NBA league and can be filtered by 15 teams respectively in Eastern and Western
  conferences. Here, we randomly pick 8 teams as our references and then scraping the data from tweets.
  
  - Since we cannot obtain the data for more than past 30 days from the standard Twitter API, we move on to find another way to gain the data.
  
  - We apply Twitter search engine to receive the tweets related to “NBA teams” in 2016 and 2017. The basic idea is to request directly from tweets and then return them as JSON files.
  
  - We collect tweets every day for the entire 2017 NBA season. Since the ￼￼competition started from 2016-10-25 to 2017-04-12, we get more than 2,000 tweets for a day and totally more than 2,500,000 tweets !  
  
* Initial Text Analysis:

  - Since we do not know which methodology has the best performance for our Twitter project, we decide to try three possible ways (Highest Frequency Words, Injury and Recovery Factors and Sentiment Analysis) to test with our dataset as our first step.
  
    - Highest Frequency Words:
    
    * Separate the entire dataset into three subset datasets based on the time period and they are "3 days", "7 days" and "1 month" individually.
    * Remove the useless contents such as 'twitter', 'http', 'com', 'pic', 'ift', 'tt', 'https' and so on.
    * After pointing out the top 20 highest frequency words in each time period, we decide to take 5 most meaningful words in the demonstration, but the results still not good enough for us to make the predictions.

    - Injury and Recovery Factors:
    - Sentiment Analysis:
  
  - After that we find out that Sentiment Analysis has the best performance at the end; therefore, we determine to implement Sentiment Analysis with five mentioned algorithms.




