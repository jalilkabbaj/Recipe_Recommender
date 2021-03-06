
##################################################################################################################################
import streamlit as st

import pandas as pd

from gensim.models.word2vec import Word2Vec

import numpy as np

from sklearn.metrics.pairwise import pairwise_distances, cosine_distances, cosine_similarity

from nltk.stem import WordNetLemmatizer

import nltk

import pickle

##################################################################################################################################
class MeanEmbeddingVectorizer(object):

    
    def __init__(self, model):

        self.model = model
        self.vector_size = model.vector_size

    def fit(self):
        return self

    def transform(self,docs):

        doc_word_vector = self.doc_average_list(docs)
        return doc_word_vector

    def doc_average(self, doc):

        mean = []

        for word in doc:
            if word in self.model.wv.index_to_key:
                mean.append(self.model.wv.get_vector(word))

        if not mean:
                return np.zeros(self.vector_size)
        else:
            mean = np.array(mean).mean(axis = 0)
            return mean

    def doc_average_list(self,docs):

        return np.vstack([self.doc_average(doc) for doc in docs])
##################################################################################################################################
st.markdown("<h1 style='text-align: center;'>Haku Recommender System</h1>", unsafe_allow_html=True)

st.image('./web_img.png')


st.write("""

    #### Don't know what to cook ? 

    ###### The Haku recommender system suggests recipes you can make with ingredients you already have. Let Haku figure out your next meal and get cookin' !

   
    """)


##################################################################################################################################

df = pd.read_csv('Data/recipe_cleaned_spacy2.csv',index_col=0)
df.dropna(inplace = True)
df.reset_index(inplace = True)
df.drop(columns = ['index'], inplace = True)
df.drop(columns = ['level_0'],inplace = True)


##################################################################################################################################
model1 = pickle.load(open('Pickle Models/Trained_Word2Vec_Model.pkl', 'rb'))
recipes = pickle.load(open('Pickle Models/Trained_Recipes.pkl','rb'))

model2 = pickle.load(open('Pickle Models/Trained_Word2Vec_Model2.pkl', 'rb'))
recipes2 = pickle.load(open('Pickle Models/Trained_Recipes2.pkl','rb'))

model3 = pickle.load(open('Pickle Models/Trained_Word2Vec_Model3.pkl', 'rb'))
recipes3 = pickle.load(open('Pickle Models/Trained_Recipes3.pkl','rb'))


##################################################################################################################################
data_set = st.selectbox(" Select the number of recipes the model will train on: ",("100,000 Recipes","500,000 Recipes","Over 1 Million Recipes"))

recs = st.slider("How many recommendations would you like ?", 1,100)


message = st.text_area("Add your ingredients (separate each ingredient with a space): ")

lemmatizer = WordNetLemmatizer()
clean_input = [lemmatizer.lemmatize(w) for w in nltk.word_tokenize(message)]




if data_set == "100,000 Recipes":

    model_data = MeanEmbeddingVectorizer(model2)
    recipe_data = recipes2 
    data_frame = df[:100000]
        

    
if data_set == "500,000 Recipes":
    model_data = MeanEmbeddingVectorizer(model3)
    recipe_data = recipes3
    data_frame = df[:500000]

    

if data_set == "Over 1 Million Recipes":
    model_data = MeanEmbeddingVectorizer(model1)
    recipe_data = recipes
    data_frame = df


ingredients_vec = model_data.doc_average(clean_input)
ingredients_vec = ingredients_vec.reshape(1,-1)




if st.button('Recommend !'):

    df = data_frame

    df['Cosine Similarity'] =list(map(lambda x: cosine_similarity(ingredients_vec, x)[0][0],recipe_data))

    st.success(st.dataframe(df.sort_values(by = 'Cosine Similarity', ascending = False)[:recs]))





       

    

