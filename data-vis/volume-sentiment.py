import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'btc_reddit_sentiment_august2021.csv'
data = pd.read_csv(file_path)

plt.figure(figsize=(12, 7))

# Scatter plot of Comments Sentiment vs. Bitcoin Volume
plt.scatter(data['comments_sentiment'], data['Volume BTC'], color='green', alpha=0.5)

# Adding plot titles and labels
plt.title('Bitcoin Volume vs. Comments Sentiment', fontsize=16)
plt.xlabel('Comments Sentiment', fontsize=14)
plt.ylabel('Volume BTC', fontsize=14)

# Enhancing grid visibility for better analysis
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Display the plot
plt.show()
