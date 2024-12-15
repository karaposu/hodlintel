Below is a **README** for **HodlIntel**, a crypto price prediction project aimed at providing **3-month outlooks** on new and existing coins based on a rich set of fundamental and community-driven metrics.

---

# HodlIntel

**HodlIntel** is a predictive analytics platform designed to forecast cryptocurrency prices over a 3-month horizon. By unifying multiple data sources—tokenomics, social sentiment, exchange distribution, developer activity, market conditions, liquidity, and whale activity—this project aims to deliver actionable insights for both new and seasoned crypto enthusiasts.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Database Schema](#database-schema)
3. [Data Flow & Architecture](#data-flow--architecture)
4. [Modeling Approach](#modeling-approach)
5. [Setup & Installation](#setup--installation)
6. [Usage](#usage)
7. [Roadmap](#roadmap)
8. [License](#license)

---

## Project Overview

**HodlIntel** provides a **medium-term (3 months) forecast** of crypto prices. While short-term predictions can be overly reactive to daily market noise, and long-term predictions can be fraught with broad uncertainties, a 3-month window strikes a balance, capturing fundamental growth patterns without being overwhelmed by extreme market cycles.

### Key Features
- **Unified Data Model**: Consolidates crypto-related metrics across multiple dimensions (e.g., tokenomics, community activity, whale activity).
- **Interactive "What If" Dashboard**: Users can adjust factors (like community size or developer activity) to see how the predicted price might change.
- **Multi-Coin Support**: Easily extendable to handle multiple coins, each stored under a unique `coin_id`.

---

## Database Schema

HodlIntel uses a relational database with the following tables:

1. **Coins**: Central reference for each coin, including:
   - `id` (PK), `full_name`, `handler`, `unique_id`
2. **Tokenomics**: Market cap, circulating supply, etc. 
   - `coin_id` (FK to `coins.id`)
3. **ExchangeDistribution**: Number of exchanges published, coverage on big exchanges, etc.
   - `coin_id` (FK to `coins.id`)
4. **SocialSentiment**: Social media hype, influencer support, etc.
   - `coin_id` (FK to `coins.id`)
5. **CommunityActivity**: Reddit size, Discord members, Twitter size, etc.
   - `coin_id` (FK to `coins.id`)
6. **Development**: Developer activity, partnerships, roadmap clarity, etc.
   - `coin_id` (FK to `coins.id`)
7. **MarketConditions**: Macro-economic factors, regulatory climate, etc.
   - `coin_id` (FK to `coins.id`)
8. **Liquidity**: Daily trading volume, liquidity on exchanges.
   - `coin_id` (FK to `coins.id`)
9. **Whalecomics**: Whale statistics, ratio of whale holdings to total market.
   - `coin_id` (FK to `coins.id`)
10. **Price**: Historical daily price data per coin.
   - `coin_id` (FK to `coins.id`)

**ER Diagram (Conceptual)**

```
Coins ---< Tokenomics
      \--< ExchangeDistribution
      \--< SocialSentiment
      \--< CommunityActivity
      \--< Development
      \--< MarketConditions
      \--< Liquidity
      \--< Whalecomics
      \--< Price
```

For convenience, each table has a `date` column to align daily metrics.

---

## Data Flow & Architecture

1. **Data Ingestion**  
   - Each metric table (e.g. `Tokenomics`, `SocialSentiment`) receives daily or periodic updates for each coin via an ETL pipeline or direct data entry.  
   - The `Price` table is updated with daily closing prices, or intraday intervals if needed.

2. **Data Consolidation**  
   - A unifying script or model queries all tables by `(coin_id, date)` to merge features into a single dataset. This dataset becomes the basis for training or inference.

3. **Model Training**  
   - Data is split by time (e.g., train on historical data prior to a cutoff date, then validate on the subsequent 3-month period).  
   - A regression or advanced ML model is trained to forecast price 3 months out.

4. **Prediction & Dashboard**  
   - Once the model is trained, new or hypothetical data points (like "If the Reddit community size doubles...") can be fed in to get a **predicted price** in 3 months.  
   - A dashboard or web app (e.g., **Streamlit** or **Dash**) provides a user-friendly interface for these “what-if” scenarios.

---

## Modeling Approach

- **Linear Regression or Tree-Based Models**: For interpretability and robust handling of mixed data, you might use:
  - **Linear Regression**: Yields direct coefficients for each feature (easy to interpret and do “what-if” scenarios).
  - **Random Forest / Gradient Boosting**: Can capture nonlinear interactions. Tools like SHAP can help interpret feature contributions.
- **Time Series**: If strictly forecasting future prices, methods like ARIMA or Prophet could incorporate time-series aspects, but your data is more akin to tabular regressors plus historical price, so a regression approach often works well.

**Target Variable**: The coin price 3 months from `t`.  
**Feature Set**: Values from all metric tables at time `t` (or an average over a lookback window).

---

## Setup & Installation

### Prerequisites
1. **Python 3.8+**  
2. **Virtual Environment** (recommended)
3. **Database**: SQLite, PostgreSQL, or any SQLAlchemy-compatible database.

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/hodlintel.git
   cd hodlintel
   ```
2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS / Linux
   # or venv\Scripts\activate on Windows
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Database Setup**:
   - Update the `DATABASE_URL` in your code to match your local or remote DB settings.  
   - Create tables:
     ```python
     from your_app.models import Base, engine
     Base.metadata.create_all(engine)
     ```

---

## Usage

### 1. Data Ingestion
- **Insert or Update** rows in the relevant tables (`tokenomics`, `price`, etc.) for each coin.  
- Ensure all tables include the correct `coin_id` linking back to the `coins` table.

### 2. Model Training
- Run a script (e.g., `train_model.py`) that:
  1. Joins all tables on `(coin_id, date)`.
  2. Splits data into training and validation sets based on time.
  3. Trains a model (Linear Regression, XGBoost, etc.).
  4. Saves the trained model to disk (pickle, joblib, etc.).

### 3. Dashboard / Prediction
- Run `streamlit run app.py` or the equivalent for your chosen framework.
- Interactively set features like **Reddit size**, **daily trading volume**, etc., and get a **3-month predicted price**.
- Optionally compare predictions across different “what-if” scenarios.

---

## Roadmap

1. **API Integration**: Automate data ingestion from popular crypto APIs (e.g., CoinGecko, CMC).
2. **Real-Time Updates**: Add near real-time ingestion and model updates for fast-evolving new coins.
3. **Advanced Analytics**: Integrate sentiment from Twitter, Reddit posts, or Discord chat logs.
4. **Multi-Coin Dashboard**: Extend the “what-if” dashboard to easily compare predictions across multiple coins side-by-side.
5. **Model Optimization**: Experiment with neural networks or advanced time-series models.

---

## License

Choose a license that suits your project’s requirements, e.g., **MIT** or **Apache 2.0**. Include a **LICENSE** file in your repository.

---

### Contact / Contributing

If you have questions, suggestions, or want to contribute to **HodlIntel**, please open an issue or submit a pull request on [GitHub](#).

---

**Happy HODLing!**
