import nltk
import csv
import string
import numpy as np 
import pandas as pd
from nltk.corpus import stopwords
from scipy.spatial import distance
from sklearn.preprocessing import normalize
from nltk.stem.porter import PorterStemmer


def happypython():
  print ("Happy Python")

def get_doc_tokens(doc, normalize=None):
    porter_stemmer = PorterStemmer()
    stop_words = nltk.corpus.stopwords.words('english')
    tokens=[token.strip()             for token in nltk.word_tokenize(doc.lower())             if token.strip() not in stop_words and               token.strip() not in string.punctuation]
    # Stermming
    if(normalize == "stem"):
        tokens = map(porter_stemmer.stem, tokens)
        
    # create token count dictionary
    token_count=nltk.FreqDist(tokens)

    return token_count

def tfidf(docs, normalize=None, percentage=1):
    
    showSimilarityCount = int(percentage*len(docs))
    print("collecting counts: {}".format(showSimilarityCount))
    keyWordIdx = 0
    
    if(normalize == "stem"):
        print("Find similar documents -- STEMMING")
        docs_tokens={idx:get_doc_tokens(doc,"stem") for idx,doc in enumerate(docs)}
    else:
        print("Find similar documents -- No STEMMING")
        docs_tokens={idx:get_doc_tokens(doc) for idx,doc in enumerate(docs)}
    

    # step 3. get document-term matrix
    dtm=pd.DataFrame.from_dict(docs_tokens, orient="index" )
    dtm=dtm.fillna(0)

      
    # step 4. get normalized term frequency (tf) matrix        
    tf=dtm.values

    doc_len=tf.sum(axis=1)
    tf=np.divide(tf.T, doc_len).T

    # step 5. get idf
    df=np.where(tf>0,1,0)
    idf=np.log(np.divide(len(docs),        np.sum(df, axis=0)))+1

    tf_idf=tf*idf

    similarity=1-distance.squareform(distance.pdist(tf_idf, 'cosine'))

    similarList = np.argsort(similarity)[:,::-1][keyWordIdx,1:(showSimilarityCount+1)]

    return similarList