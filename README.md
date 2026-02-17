Trader Performance vs Market Sentiment

Overview
This project analyzes trader behavior and performance using historical Hyperliquid trading data and the Bitcoin Fear & Greed Index. The goal is to explore how trader outcomes and risk characteristics relate to broader market conditions.

Datasets
- **Bitcoin Fear & Greed Index**  
  Daily market sentiment data labeled as Fear or Greed.

- Hyperliquid Historical Trader Data 
  Trade-level data including account, position size, direction, timestamps, and closed PnL.

Data Preparation
- Column names were standardized for consistency.
- Unix timestamps in the sentiment dataset were correctly converted to dates.
- Trade timestamps were converted to daily dates to enable alignment.
- Data quality checks were performed to ensure no missing or invalid timestamps.

Analysis Performed
- Daily PnL aggregation at the trader level
- Trade frequency and win-rate calculations
- PnL distribution analysis
- Visualization of risk using log-scaled PnL histograms

Key Insights
- Most trades result in small profits or losses, while a small number of trades contribute large outcomes.
- PnL distribution is heavy-tailed, meaning overall risk is driven by rare extreme events.
- Average performance metrics alone are insufficient to understand trading risk.

Limitations
- Limited temporal overlap was observed between sentiment data and trading data.
- As a result, sentiment-based comparisons were constrained and are noted transparently.

Actionable Takeaways
- Risk management should focus on limiting extreme losses rather than maximizing average returns.
- Position sizing plays a critical role in controlling downside risk.

# Trader Performance vs Market Sentiment

## Overview
This project analyzes trader behavior and performance using historical Hyperliquid trading data and the Bitcoin Fear & Greed Index. The goal is to explore how trader outcomes and risk characteristics relate to broader market conditions.

## Datasets
- **Bitcoin Fear & Greed Index**  
  Daily market sentiment data labeled as Fear or Greed.

- **Hyperliquid Historical Trader Data**  
  Trade-level data including account, position size, direction, timestamps, and closed PnL.

## Data Preparation
- Column names were standardized for consistency.
- Unix timestamps in the sentiment dataset were correctly converted to dates.
- Trade timestamps were converted to daily dates to enable alignment.
- Data quality checks were performed to ensure no missing or invalid timestamps.

## Analysis Performed
- Daily PnL aggregation at the trader level
- Trade frequency and win-rate calculations
- PnL distribution analysis
- Visualization of risk using log-scaled PnL histograms

## Key Insights
- Most trades result in small profits or losses, while a small number of trades contribute large outcomes.
- PnL distribution is heavy-tailed, meaning overall risk is driven by rare extreme events.
- Average performance metrics alone are insufficient to understand trading risk.

## Limitations
- Limited temporal overlap was observed between sentiment data and trading data.
- As a result, sentiment-based comparisons were constrained and are noted transparently.

## Actionable Takeaways
- Risk management should focus on limiting extreme losses rather than maximizing average returns.
- Position sizing plays a critical role in controlling downside risk.

 How to Run
1. Install required libraries:
  ( pip install  numpy , pandas , matplotlib , seaborn)
2. Open the Jupyter notebook.
3. Run all cells from top to bottom.

Author:
Rohan

