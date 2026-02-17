Trader Performance vs Market Sentiment:

Objective:
The goal of this analysis was to understand how trader performance and behavior relate to overall market sentiment (Fear vs Greed) using Hyperliquid trading data and the Bitcoin Fear & Greed Index. The focus was on data preparation, correct alignment of datasets, and extracting meaningful insights rather than building complex models


Data Preparation:
Two datasets were used-
1) Bitcoin Fear & Greed Index (daily sentiment)
2) Historical trader-level data from Hyperliquid
During preprocessing, special attention was given to timestamps. The sentiment dataset contained Unix timestamps, and an initial parsing issue caused all dates to default to 1970. This was resolved by reconstructing dates directly from the raw timestamp field using the correct unit (seconds).
The trade dataset used high-frequency timestamps, which were converted to daily dates for alignment. Column names were standardized, and timestamps were validated to ensure clean merging.


Data Alignment Challenge:
After aligning both datasets by date, it was observed that there was little to no overlap between the available sentiment dates and the trading data dates. As a result, sentiment-based comparisons (Fear vs Greed) could not be reliably performed at scale.

Instead of forcing results, this limitation was explicitly identified and documented. This reflects a real-world data challenge where datasets from different sources may not always align perfectly in time.


Analysis & Key Observations:
Even without full sentiment overlap, meaningful insights were extracted from the trading data:
. PnL Distribution:
. Most trades resulted in very small profits or losses, while a small number of trades produced extremely large       outcomes. This heavy-tailed behavior is typical in trading data.
. Risk Characteristics:
  A log-scaled histogram of absolute PnL showed that overall risk is driven by rare but significant events rather than by average trade outcomes.
. Trading Behavior:
The distribution suggests frequent small trades combined with occasional large gains or losses, highlighting the importance of risk control over simply increasing trade frequency.


Visualization Approach:
Standard histograms compressed most data near zero due to extreme values. To address this, a log-scale visualization of absolute PnL was used, which made both common small trades and rare extreme outcomes visible in a single chart. This provided a clearer view of risk exposure.


Actionable Takeaways:
1) Risk management matters more than average returns
   Since a few extreme trades dominate outcomes, controlling downside risk is more important than optimizing mean PnL.
2) Position sizing should be conservative in volatile conditions
   Large position sizes increase exposure to tail losses, which can significantly impact overall performance.


Conclusion:
This analysis highlights the importance of correct timestamp handling, careful dataset alignment, and honest evaluation of data limitations. Even when ideal conditions for sentiment analysis are not met, valuable insights can still be derived by focusing on trader behavior and risk characteristics. The work emphasizes practical data handling, transparency, and realistic interpretation—key skills in applied data science and trading analytics