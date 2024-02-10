import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'btc_reddit_sentiment_august2021.csv'
data = pd.read_csv(file_path)

# Create a figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'tab:red'
ax1.set_xlabel('Time (index)')
ax1.set_ylabel('Price', color=color)
ax1.plot(data.index, data['close'], color=color, label='Close Price')
ax1.tick_params(axis='y', labelcolor=color)

# Instantiate a second y-axis sharing the same x-axis
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Sentiment', color=color)
ax2.plot(data.index, data['comments_sentiment'], color=color, linestyle='--', label='Comments Sentiment')
ax2.tick_params(axis='y', labelcolor=color)

# Title and legend
plt.title('Bitcoin Close Price and Reddit Comments Sentiment - August 2021')
fig.tight_layout()

# Show the plot
plt.show()
