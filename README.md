# From Posts to Predictions: Leveraging Reddit Sentiments for Bitcoin Price Analysis

**Authors:**
- **Randall Bevan** - rbevan6@gatech.edu
- **Jessica Ly** - jly31@gatech.edu
- **Henry Zhang** - hzhang902@gatech.edu
- **Priyanshu Mehta** - pmehta305@gatech.edu
- **Srisankaet Cheemalamarri** - scheemal3@gatech.edu

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
![randallgraph](https://github.com/priyanshum17/ReplicationStudy/assets/70831431/c08e81a8-2e95-434b-b3c4-5d21d963f014)
*Figure 1: Graphing of Bitcoin Close Price vs. Comment Sentiment*

![volume vs sentiment](https://github.com/priyanshum17/ReplicationStudy/assets/70831431/ebba0ced-5d08-4e2c-8180-0537f8a0a2be)
*Figure 2: Scatter Plot of Bitcoin Trading Volume vs. Comments Sentiment*

## Models

### LSTM-GRU Model

<img width="358" alt="newplot (9)" src="https://github.com/priyanshum17/ReplicationStudy/assets/70831431/f0f801fb-1f87-4175-b834-3978081c7fba">
*Figure 3: Training loss vs epochs for LSTM-GRU Model showing a large drop in training loss after a few epochs indicating possible over-fitting*

### Transformer Model

![newplot (8)](https://github.com/priyanshum17/ReplicationStudy/assets/70831431/dc265382-d29e-4bea-9aaf-9d054ef593b4)
*Figure 4: Training loss graphs for the Transformer model, trained on different datasets*

## Data Collection

Details on the data collection process using Python wrappers and the challenges faced with the Reddit API.

## Conclusion

In conclusion, our study provides a nuanced understanding of the intricate interplay between social media sentiment and Bitcoin market dynamics. While initial analyses suggest limited predictive power of sentiment alone, the deployment of advanced deep learning models presents avenues for refinement and exploration.

## References

1. Pavlo Seroyizhko, Zhanel Zhexenova, Muhammad Zohaib Shafiq, Fabio Merizzi, Andrea Galassi, and Federico Ruggeri. 2022. "A Sentiment and Emotion Annotated Dataset for Bitcoin Price Forecasting Based on Reddit Posts." In Proceedings of the Fourth Workshop on Financial Technology and Natural Language Processing (FinNLP), pages 203–210, Abu Dhabi, United Arab Emirates (Hybrid). Association for Computational Linguistics.
2. Esuli, A., & Sebastiani, F. (2009). "Training data cleaning for text classification." In Conference on the Theory of Information Retrieval, pages 29-41. Springer Berlin Heidelberg.
3. Antweiler, W., & Frank, M. Z. (2004). "Is all that talk just noise? The information content of internet stock message boards." The Journal of finance, 59(3), 1259-1294.
4. Bollen, J., Mao, H., & Zeng, X. (2011). "Twitter mood predicts the stock market." Journal of computational science, 2(1), 1-8.
5. Mai, F., Shan, Z., Bai, Q., Wang, X., & Chiang, R. H. (2018). "How does social media impact Bitcoin value? A test of the silent majority hypothesis." Journal of management information systems, 35(1), 19-52.
6. Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). "Bert: Pre-training of deep bidirectional transformers for language understanding." arXiv preprint arXiv:1810.04805.
7. Radford, A., Narasimhan, K., Salimans, T., & Sutskever, I. (2018). "Improving language understanding by generative pre-training."
8. Hochreiter, S., & Schmidhuber, J. (1997). "Long short-term memory." Neural computation, 9(8), 1735-1780.
9. Cho, K., Van Merriënboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., & Bengio, Y. (2014). "Learning phrase representations using RNN encoder-decoder for statistical machine translation." arXiv preprint arXiv:1406.1078.
10. Fischer, T., & Krauss, C. (2018). "Deep learning with long short-term memory networks for financial market predictions." European journal of operational research, 270(2), 654-669.
