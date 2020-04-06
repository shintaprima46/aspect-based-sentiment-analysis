
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings; warnings.simplefilter('ignore')
import time
import pyLDAvis, pyLDAvis.sklearn; pyLDAvis.enable_notebook()
import pickle, TSutanto_lib as ittc
import imblearn
import numpy as np
import sklearn
import seaborn as sns
from nltk.stem import WordNetLemmatizer
from spacy.lang.id import Indonesian
from nltk import word_tokenize, sent_tokenize
from tqdm import tqdm_notebook as tqdm
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA


# In[4]:


# VSM term Frekuensi : "tf"
df = pd.read_csv('tokped_bersih3 fix - Copy.csv') 
data = df['Cleaned_review'] # input data for clustering is review that has been cleaned

Tf_vectorizer = CountVectorizer(max_df=0.75, min_df=5)

listdf=data.values.astype('U')
listdf = [d for d in listdf]

tf = Tf_vectorizer.fit_transform(listdf)
tfidf_term = Tf_vectorizer.get_feature_names()


n_topics4 = 4
lda4 = LDA(n_components=n_topics4, learning_method='batch', random_state=0).fit(tf)
lda4


# In[28]:


Top_Words=15
print('Printing top {0} Topics, with top {1} Words:'.format(n_topics4, Top_Words))
ittc.print_Topics(lda4, tfidf_term, n_topics4, Top_Words)
