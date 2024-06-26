import streamlit as st
import pickle
import time


# load the model
model = pickle.load(open('./twitter_sentiment.pkl', 'rb'))

with open("style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)



st.title('Twitter Sentiment Analysis')
st.image('https://assets-global.website-files.com/614c82ed388d53640613982e/64f7989c55786e5b4de9b9cb_sentiment-analysis-explained.webp',width=700)
tweet = st.text_input("Enter your Tweet")
submit = st.button('Predict',type="primary")
if submit:
    start = time.time()
    prediction = model.predict([tweet])
    print(prediction[0])

    end = time.time()

    st.header('Prediction time taken:{} seconds'.format(round(end-start, 2))) 
    if prediction[0]=='Positive':
        st.markdown("<h1 style='color:pink;'>Predicted sentiment= Positive</h1>",unsafe_allow_html=True)
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5gTpjUxBnj4ugjxmU7c18lJCh3kdRRd4Orw&usqp=CAUhttps://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5gTpjUxBnj4ugjxmU7c18lJCh3kdRRd4Orw&usqp=CAU',width=500)
    if prediction[0]=='Negative':
        st.markdown("<h1 style='color:yellow;'>Predicted sentiment= Negative</h1>",unsafe_allow_html=True)
        st.image('https://pbs.twimg.com/media/EvuLwplXAAAOgrX.jpg',width=500)
    if prediction[0]=='Neutral':
        st.markdown("<h1 style='color:yellow;'>Predicted sentiment= Neutral</h1>",unsafe_allow_html=True)
        st.image('https://images.emojiterra.com/twitter/v13.1/512px/1f610.png',width=500)


    
        
    
    
        