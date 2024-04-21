# Replication Study
---
title: "From Posts to Predictions: Leveraging Reddit Sentiments for Bitcoin Price Analysis"
author: Randall Bevan, Jessica Ly, Henry Zhang, Priyanshu Mehta, Srisankaet Cheemalamarri
email: rbevan6@gatech.edu, jly31@gatech.edu, hzhang902@gatech.edu, pmehta305@gatech.edu, scheemal3@gatech.edu
---

## Abstract

This study investigates the relationship between Reddit sentiment and Bitcoin market behavior using graphical analysis and deep learning models. Graphs comparing Bitcoin's price and trading volume against Reddit sentiment reveal a limited correlation. LSTM-GRU and Transformer models trained on historical data aim to predict Bitcoin's future price movements. Results suggest challenges in using social media sentiment as a sole predictor, highlighting the need for further model refinement and exploration of additional influencing factors.

## Introduction

As cryptocurrencies, particularly Bitcoin, begin to grow in their financial prowess and public opinion, concurrently their presence on social media has been growing as well. Platforms such as Reddit have become hubs of discussion regarding opinions and uses of cryptocurrency. Inspired by the market impact of the r/WallStreetBets subreddit regarding the stock evaluation of GameStop in 2021, the study by Seroyizhko et al. (2021) at the University of Bologna sought to investigate the relationship between Reddit comment sentiment and Bitcoin market behavior using graphical analysis and machine learning models, both separately and together. Through their research they found a limited correlation between Reddit sentiment and Bitcoin’s market behavior, these results challenge the idea of utilizing social media sentiment as a predictor for cryptocurrency price movements (Seroyizhko et al., 2021).

In our replication study, we aim to reassess these findings using the dataset built by the previous research as well as expand upon it with web-scraped current data.

## Overview of Methodology

- **Replication with Original Dataset:** We followed the original study’s method of utilizing the LSTM-GRU and Transformer models, trained on the same data set as the original study, to replicate their findings.
- **Data Augmentation through Scraping:** Enhance the study by scraping new data from the same Reddit sources to augment the original dataset.
- **Application and Analysis:** Use the augmented data set to mimic the original study’s attempt to conduct predictive analysis, aiming to increase the accuracy of our new data set’s Reddit sentiment with Bitcoin Market Behavior.

## Graphical Analysis

### Bitcoin Price vs. Reddit Sentiment

![Bitcoin Close Price vs. Comment Sentiment](path_to_image/randallgraph.png)
*Figure 1: Graphing of Bitcoin Close Price vs. Comment Sentiment*

![Bitcoin Trading Volume vs. Comments Sentiment](path_to_image/volume_vs_sentiment.png)
*Figure 2: Scatter Plot of Bitcoin Trading Volume vs. Comments Sentiment*

## Models

### LSTM-GRU Model

![Training loss vs epochs for LSTM-GRU Model](path_to_image/newplot_9.png)
*Figure 3: Training loss vs epochs for LSTM-GRU Model showing a large drop in training loss after a few epochs indicating possible over-fitting*

### Transformer Model

![Graphs of the training loss (MSE) of the Transformer model](path_to_image/newplot_1_2.png)
*Figure 4: Training loss graphs for the Transformer model, trained on different datasets*

## Data Collection

Details on the data collection process using Python wrappers and the challenges faced with the Reddit API.

## Conclusion

In conclusion, our study provides a nuanced understanding of the intricate interplay between social media sentiment and Bitcoin market dynamics. While initial analyses suggest limited predictive power of sentiment alone, the deployment of advanced deep learning models presents avenues for refinement and exploration.

## References

1. Pavlo Seroyizhko, Zhanel Zhexenova, Muhammad Zohaib Shafiq, Fabio Merizzi, Andrea Galassi, and Federico Ruggeri. 2022. A Sentiment and Emotion Annotated Dataset for Bitcoin Price Forecasting Based on Reddit Posts. In Proceedings of the Fourth Workshop on Financial Technology and Natural Language Processing (FinNLP), pages 203–210, Abu Dhabi, United Arab Emirates (Hybrid). Association for Computational Linguistics.
2. Other references...
