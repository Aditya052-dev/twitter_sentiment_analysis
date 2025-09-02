# twitter_sentiment_analysis

📖 Overview

This tool provides a comprehensive analysis of any public Twitter user's timeline. In an era where social media is a key indicator of public opinion and personal expression, this application offers a way to programmatically understand the nuances of a user's Twitter presence. By simply entering a username, it generates a series of visualizations and statistics that reveal insights into their tweeting habits, audience engagement, and the overall sentiment of their posts. The application is built with a user-friendly Tkinter GUI, making complex data analysis accessible to everyone, regardless of their technical skills.

🤔 How It Works
The application follows a streamlined, four-step process to transform raw tweets into actionable insights:

1.	Data Fetching: Upon entering a username, the application uses the Tweepy library to connect to the Twitter API v1.1 and fetches the 200 most recent tweets from the specified user's timeline.
	
2.	Data Structuring: The raw tweet data, which includes text, metadata like likes, retweets, creation date, and source, is organized into a Pandas DataFrame. This structured format is essential for efficient analysis and manipulation.
	
3.	Sentiment Analysis: For each tweet, the text is cleaned by removing hashtags, mentions, and URLs. The cleaned text is then processed by TextBlob, which performs lexicon-based sentiment analysis to classify the tweet as Positive, Neutral, or Negative based on its polarity score.
	
4.	Visualization: The aggregated data and analysis results are visualized using Matplotlib. The tool generates several plots, including pie charts for sentiment breakdown and tweet sources, and time-series line graphs for engagement metrics. These plots are displayed sequentially to the user.
   
✨ Key Features
•	🗣️ Sentiment Analysis: Classifies each tweet as Positive, Neutral, or Negative and visualizes the overall distribution in a pie chart.

•	📈 Activity Metrics: Fetches and analyzes data on tweet length, likes, and retweet counts to quantify user activity and engagement.

•	📊 Rich Visualizations: Generates multiple plots:

o	Sentiment distribution pie chart.

o	Tweet sources pie chart (e.g., iPhone vs. Android vs. Web).

o	Line graphs showing likes, retweets, and tweet length over time.

•	🏆 Top Tweet Identification: Automatically finds and displays the user's most popular tweets based on the highest number of likes and retweets.

•	🖱️ Simple GUI: An easy-to-use interface built with Tkinter for straightforward operation. No command-line knowledge is required to use the tool.

🛠️ Technology Stack

Technology	Purpose

Python 3	Core programming language.

Tweepy	For seamless interaction with the Twitter API v1.1.

TextBlob	For simple and effective rule-based sentiment analysis.

Pandas	For structuring and managing the tweet data in DataFrames.

Matplotlib	For creating all the data visualizations.

Tkinter	For building the native desktop GUI.

📂 Project Structure
.
├── gui.py              # Main application script with the Tkinter GUI

├── config.py           # Configuration file for API keys (must be created manually)

├── assets/               # (Optional) Folder for images like the banner

│   └── twitter_analysis_banner.png

└── README.md           # This file

⚙️ Getting Started

1. Prerequisites
   
•	Python 3.6 or higher.

•	A Twitter Developer account with approved API keys and access tokens for the v1.1 API. You can apply for one here.

3. Clone the Repository
   
git clone [https://github.com/your-username/twitter-sentiment-analysis.git](https://github.com/your-username/twitter-sentiment-analysis.git)
cd twitter-sentiment-analysis

5. Install Dependencies
   
This command will install all the necessary libraries for the project.
pip install tweepy pandas textblob matplotlib

7. Configure API Keys
   
IMPORTANT: To protect your credentials, never hardcode API keys in the main script.

1.	Create a new file in the project's root directory and name it config.py.

2.	Add your Twitter API keys and tokens to this file:
   
config.py

# Twitter API Credentials

CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET'

3.	Ensure you have added config.py to your .gitignore file to prevent it from being committed to GitHub.
▶️ Usage
To run the application, execute the gui.py script from your terminal:
python gui.py

1.	The application window will open.
2.	Enter a target Twitter username in the input box (without the @ symbol).
3.	Click the "Get Analysis" button.
4.	The script will begin fetching and analyzing the data. Please wait for the process to complete.
5.	A series of Matplotlib windows will pop up one by one, displaying the analysis results.
   
🔬 Analysis Details

The script performs the following in-depth analyses:

1.	Sentiment Polarity: This analysis reveals the overall tone of the user's tweets. It's useful for understanding public opinion, brand perception, or an individual's emotional state.

o	Polarity > 0: Positive (indicates happiness, agreement, or positive language)

o	Polarity == 0: Neutral (often factual statements or tweets without strong sentiment)

o	Polarity < 0: Negative (indicates sadness, anger, or disagreement)

2.	Tweet Engagement: By identifying the most liked and retweeted tweets, you can understand what content resonates most with the user's audience.
	
3.	Tweet Source: This breakdown shows which platforms the user tweets from. It can indicate whether they are a mobile-first user and can sometimes reveal the use of automated tweeting tools.

4.	Temporal Patterns: Plotting engagement metrics over the timeline of the 200 tweets can reveal trends, such as whether recent tweets are becoming more or less popular.

💡 Future Improvements

•	[ ] Asynchronous Execution: Move the API calls and analysis to a separate thread to prevent the GUI from freezing during data processing, providing a smoother user experience.

•	[ ] Robust Error Handling: Implement try...except blocks to gracefully manage API rate limits, invalid usernames, protected accounts, and network issues.

•	[ ] Use a .env File: Transition from config.py to a more standard .env file and the python-dotenv library for managing environment variables.

•	[ ] Advanced Sentiment Analysis: Integrate a more sophisticated model, such as VADER (Valence Aware Dictionary and sEntiment Reasoner) or a fine-tuned transformer model (like BERT), for more nuanced and accurate sentiment analysis.

•	[ ] Interactive Dashboards: Rebuild the UI with a framework like Streamlit or Plotly Dash. This would allow for interactive, in-app charts and a more modern user interface, eliminating the need for multiple pop-up windows.

