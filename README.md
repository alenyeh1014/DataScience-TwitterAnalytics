# Web Analytics: NBA Predictions with Twitter
Hi all, this is a Data Science Project ! - Twitter Analytics with Machine Learning and Deep Learning methodologies.


### Project Objective

* The purpose of this project is to apply Machine Learning and Deep Learning methodologies in social media analytics such as 
**Twitter** in order to predict the game results of NBA. Thus, more business opportunities may be detected and utilized not only for NBA but also for other relevant sport leagues.

### Methods Used

* Inferential Statistics
* Web Scraping
* Data Wrangling
* Data Visualization
* Machine Learning
* Deep Learning
* Predictive Modeling


### Algorithms Used

- Supervised Learning: 
  - Naive Bayes Classifiers (NB)
  - Support Vector Machines (SVM)
  
- Unsupervised Learning: 
  - K-means Clustering (K-means)
  - Latent Dirichlet Allocation (LDA)
  
- Deeping Learning: 
  - Convolutional Neural Network (CNN)


### Technologies and Packages Used

* Python, Jupyter Notebook
* Numpy, Pandas, Sklearn, Nltk
* Matplotlib, Scipy, Seaborn, Keras


### Project Description

* Motivation:

  - Since we are NBA sport fans and twitter lovers, we decide to work on a **social media analytics** project combining the skills and technologies from we have learned to see how it works. Therefore, we apply **Machine Learning and Deep Learning methodologies** to predict the NBA game results from Twitter. Meanwhile, in order to obtain good performance of each methodology, accuracies are also important and necessary for every individual user.  
  
* Data and Scope:

  - There are total 30 teams in the NBA league and can be divided by 15 teams respectively in Eastern and Western
  conferences. Here, we randomly pick **8 teams as sample data and scrape the data from tweets**.
  
  - Since we cannot obtain the data for more than past 30 days from the standard twitter API, we move on to find another way to gain the data.
  
  - We apply twitter search engine to receive the tweets related to “NBA teams” in 2016 and 2017. The basic idea is to request directly from tweets and then return them as **JSON** files.
  
  - We collect tweets every day for the entire 2017 NBA season. Since the ￼￼competition started from 2016-10-25 to 2017-04-12, we get more than 2,000 tweets for a day and totally **more than 2,500,000 tweets!**  
  
* Initial Text Analysis:

  - At first, we do not know which methodology has the best performance for this project. Therefore, we consider and decide to try three possible ways **(Highest Frequency Words, Injury and Recovery Factors and Sentiment Analysis)** to test with our sample dataset as our first step.
  
    - Highest Frequency Words:
    
      * Separate the entire dataset into **three subset datasets** based on the time period and they are "3 days", "7 days" and "1 month" individually.
      * Remove the **useless** contents such as 'twitter', 'http', 'com', 'pic', 'ift', 'tt', 'https' and so on.
      * After pointing out the top 20 highest frequency words in each time period, we take **5 most meaningful words** for the demonstration.
      * However, the results are not good enough to make the game predictions accurately.

    - Injury and Recovery Factors:
      
      * In this section, we are more interested in finding some **influential factors** which could affect the results of the games. 
      * Therefore, we wonder if there are **injured players or recovered players** in the team because they may have huge influences on the game results if they are key players for that team.
      * Here are some commom key words for tweets related to **injury and recovery words**:
        * Injury words (Negative): ￼￼￼['hurt','injury','injured','broken','tear','missed','ill', 'illness']
        * Recovery words (Positive): ￼￼￼￼['recover','recovery','return','health','healthy','heal', 'back', 'rehab']
      * After that we count these words and determine if **Injury words > Recovery words** then which means it is a **good expectation** for that team. 
      * Otherwise, if **Recovery words > Injury words** then which means it is a **bad expectation** for the team.
      
    - Sentiment Analysis:
    
      * First of all, we count the amount of positive/negative words from all tweets. **Once the amount of positive words greater than negative words we treat it as a good result**.
      * In addition, if **good results are more than bad results** 24 hours before the competition, we predict the result of the game is to **win**.
      * Furthermore, we apply **TF-IDF model** to filter tweets and discover this accuracy is much higher than the previous ones. 
  
  - After processing three different kinds of methodologies, **we find out that Sentiment Analysis has the best performance** at the end; therefore, we determine to implement Sentiment Analysis with mentioned algorithms.


### Methodology Approach 

* In this section, we gain the accuracy of combining algorithms with and without Sentiment Analysis:  


  * Supervised Learning Algorithms:
  
    (1) Accuracy of Naive Bayes Classifiers (NB):

      | Non_Sentiment Analysis | Sentiment Analysis |
      | --- | --- |
      | **around 50% to 60%** | around 50% |


    (2) Accuracy of Support Vector Machines (SVM):

      | Non_Sentiment Analysis | Sentiment Analysis |
      | --- | --- |
      | **around 50% to 60%** | around 50% |
    
    
  * Unsupervised Learning Algorithms:
    
    (3) Accuracy of K-means Clustering (K-means):

      | Non_Sentiment Analysis |
      | --- |
      | around 50% |
    
        
    (4) Accuracy of Latent Dirichlet Allocation (LDA):

      | Non_Sentiment Analysis |
      | --- |
      | around 50% | 

   
   * Deep Learning Algorithm:
   
     (5) Accuracy of Convolutional Neural Network (CNN):

      | Non_Sentiment Analysis |
      | --- |
      | **around 60%** | 
    
      - P.S. We do not apply **Sentiment Ananlysis** for **Unsupervised Learning** and **Deep Learning** Algorithms because Sentiment Ananlysis is not appropriate for Unsupervised Learning and also no need for Deep Learning Alogrithms.
          
          
### Conclusion:

  - After comparing with five different algorithms, we conclude that **supervised learning algorithms (Naive Bayes and SVM) have better performances than unsupervised learning algorithms (K-means and LDA)**. The possible reason is because **labels** utilized in supervised learning alogritms may strengthen the features of tweets; therefore, it can improve the accuracy of predictions in NBA game results. However, **CNN still has the highest accuracy performance over than any other methodologies**. That is to say, CNN is the most practical algorithm in this twitter project and we should keep modifying the parameters set inside the model in order to gain a better performance.



