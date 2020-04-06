
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
data = df['Cleaned_review']

Tf_vectorizer = CountVectorizer(max_df=0.75, min_df=5)

listdf=data.values.astype('U')
listdf = [d for d in listdf]

tf = Tf_vectorizer.fit_transform(listdf)
tfidf_term = Tf_vectorizer.get_feature_names()


# In[5]:


n_topics9 = 9
lda9 = LDA(n_components=n_topics9, learning_method='batch', random_state=0).fit(tf)
lda9


# In[11]:


Top_Words=15
print('Printing top {0} Topics, with top {1} Words:'.format(n_topics9, Top_Words))
ittc.print_Topics(lda9, tfidf_term, n_topics9, Top_Words)


# In[9]:


ldavis = pyLDAvis.sklearn.prepare(lda9, tf, Tf_vectorizer)  
ldavis


# In[16]:


print(lda2.perplexity(tfidf, sub_sampling=False)) #sama aja caranya ini kayak pake bound di atas
print(lda3.perplexity(tfidf, sub_sampling=False))
print(lda4.perplexity(tfidf, sub_sampling=False))
print(lda5.perplexity(tfidf, sub_sampling=False))
print(lda6.perplexity(tfidf, sub_sampling=False))
print(lda7.perplexity(tfidf, sub_sampling=False))
print(lda8.perplexity(tfidf, sub_sampling=False))
print(lda9.perplexity(tfidf, sub_sampling=False))


# In[20]:


n_topics4 = 4
lda4 = LDA(n_components=n_topics4, learning_method='batch', random_state=0).fit(tf)
lda4


# In[28]:


Top_Words=15
print('Printing top {0} Topics, with top {1} Words:'.format(n_topics4, Top_Words))
ittc.print_Topics(lda4, tfidf_term, n_topics4, Top_Words)


# In[22]:


ldavis = pyLDAvis.sklearn.prepare(lda4, tf, Tf_vectorizer)  
ldavis


# ##### doc_topic_prior: float
# ##### Prior of document topic distribution (theta, tapi di blei 2010 disebut alpha). If the value is None, it is 1 / n_components. berarti di n_components=4, theta=0.25
# ##### topic_word_prior: float
# ##### Prior of topic word distribution (beta). If the value is None, it is 1 / n_components. berarti beta=0.25
# ##### default=None

# In[12]:


# Melihat Topik-topiknya
vsm_topics = lda.transform(tfidf)
print(vsm_topics.shape)
vsm_topics


# In[13]:


# Seandainya diasumsikan 1 dokumen hanya 1 topic dengan nilai skor topic terbesar
doc_topic =  [a.argmax()+1 for a in tqdm(vsm_topics)] # topic of docs
doc_topic[:10]
sns.countplot(doc_topic)


# In[114]:


Top_Words=20
print('Printing top {0} Topics, with top {1} Words:'.format(n_topics, Top_Words))
ittc.print_Topics(lda, tfidf_term, n_topics, Top_Words)


# In[ ]:


topik 1: tampilan 
topik 2: pelayanan
topik 3: helpful
topik 4: pengalaman belanja


# In[115]:


ldavis = pyLDAvis.sklearn.prepare(lda, tfidf, Tfidf_vectorizer)  
ldavis


# In[14]:


# Log Likelyhood: Higher the better
print("Log Likelihood: ", lda.score(tfidf))

# Perplexity: Lower the better. Perplexity = exp(-1. * log-likelihood per word)
print("Perplexity: ", lda.perplexity(tfidf))


# In[18]:


n_topics16 = 16
lda16 = LDA(n_components=n_topics16, learning_method='batch', random_state=0).fit(tf)
lda16


# In[19]:


ldavis = pyLDAvis.sklearn.prepare(lda16, tf, Tf_vectorizer)  
ldavis

