import streamlit as st
import plotly.express as px
import glob
from datetime import datetime
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

files = glob.glob("diary/*.txt")
files = sorted(files)

def convert_date(path):
    date_str = path.split('/')[1].split('.')[0]  # Extract the date part
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # Convert string to date object
    return date_obj.strftime('%b %d')  # Format the date

formatted_dates = [convert_date(path) for path in files]
print(formatted_dates)

diary = []

for file in files:
    with open(file, "r") as file:
        content = file.read()
    diary.append(content)

positivity = []
negativity = []
analyzer = SentimentIntensityAnalyzer()
for chapter in diary:
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(chapter)
    positivity.append(result["pos"])
    negativity.append(result["neg"])
print(positivity)
print(negativity)

dates = [file.strip(".txt").strip("diary/") for file in files]
print(dates)

st.title("Diary Tone")

st.subheader("Positivity")

pos_chart = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_chart)

st.subheader("Negativity")

neg_chart = px.line(x=formatted_dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_chart)

print(files)
