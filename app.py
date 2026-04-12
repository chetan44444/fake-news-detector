
import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Fake News Detector")

input_text = st.text_area("Enter News Text:")

if st.button("Predict"):
    data = vectorizer.transform([input_text])
    result = model.predict(data)

    if result[0] == 0:
        st.error("Fake News ❌")
    else:
        st.success("Real News ✅")
