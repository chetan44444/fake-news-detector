# Fake News Detector (AI)

This project is a machine learning-based web application that predicts whether a news headline or statement is **real or fake**.

## Overview

The model is trained on a labeled dataset of news articles and uses text classification techniques to identify patterns commonly found in fake and real news.

The application is built using Streamlit, allowing users to input any news text and get an instant prediction.


## Features

* Classifies news as Real or Fake
* Uses TF-IDF for text vectorization
* Logistic Regression model for prediction
* Simple and interactive web interface
* Deployed on cloud for public access


## Tech Stack

* Python
* Scikit-learn
* Pandas
* Streamlit

## How It Works

1. Input text is taken from the user
2. Text is converted into numerical features using TF-IDF
3. The trained model predicts the class (Real/Fake)
4. Result is displayed on the web interface


## Project Structure

Fake-News-Detector/
│── app.py
│── train.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt


## Running the Project

```bash
pip install -r requirements.txt
streamlit run app.py
```
---
## Live Demo
https://fake-news-detector-newzy.streamlit.app/
