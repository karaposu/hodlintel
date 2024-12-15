from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

# 1. Coins Table (Central reference for each coin)
class Coins(Base):
    __tablename__ = 'coins'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    handler = Column(String, nullable=True)
    unique_id = Column(String, nullable=True)

    # Relationships to other tables (optional but helpful)
    tokenomics = relationship('Tokenomics', back_populates='coin')
    exchange_distributions = relationship('ExchangeDistribution', back_populates='coin')
    social_sentiments = relationship('SocialSentiment', back_populates='coin')
    community_activities = relationship('CommunityActivity', back_populates='coin')
    developments = relationship('Development', back_populates='coin')
    market_conditions = relationship('MarketConditions', back_populates='coin')
    liquidity_records = relationship('Liquidity', back_populates='coin')
    whalecomics_records = relationship('Whalecomics', back_populates='coin')
    prices = relationship('Price', back_populates='coin')

# 2. Tokenomics Table
class Tokenomics(Base):
    __tablename__ = 'tokenomics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    market_cap = Column(Float)
    circulating_supply = Column(Float)
    max_supply = Column(Float)
    burn_mechanism = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Coins
    coin = relationship('Coins', back_populates='tokenomics')

# 3. Exchange Distribution Table
class ExchangeDistribution(Base):
    __tablename__ = 'exchange_distribution'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    num_exchanges_published = Column(Integer)
    num_big_exchanges_published = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Coins
    coin = relationship('Coins', back_populates='exchange_distributions')

# 4. Social Sentiment Table
class SocialSentiment(Base):
    __tablename__ = 'social_sentiment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    social_media_hype = Column(Integer)
    influencer_support = Column(Integer)
    visibility_50k_posts = Column(Integer)
    visibility_10k_posts = Column(Integer)
    visibility_100k_posts = Column(Integer)
    visibility_250k_posts = Column(Integer)
    visibility_500k_posts = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Coins
    coin = relationship('Coins', back_populates='social_sentiments')

# 5. Community Activity Table
class CommunityActivity(Base):
    __tablename__ = 'community_activity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    reddit_size = Column(Integer)
    discord_member_size = Column(Integer)
    twitter_size = Column(Integer)
    community_positivity_level = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Coins
    coin = relationship('Coins', back_populates='community_activities')

# 6. Development Table
class Development(Base):
    __tablename__ = 'development'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    developer_activity = Column(Integer)
    partnerships = Column(Integer)
    roadmap_clarity = Column(Integer)
    utilities = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Coins
    coin = relationship('Coins', back_populates='developments')

# 7. Market Conditions Table
class MarketConditions(Base):
    __tablename__ = 'market_conditions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    macro_economic_factors = Column(Integer)
    regulatory_climate = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Coins
    coin = relationship('Coins', back_populates='market_conditions')

# 8. Liquidity Table
class Liquidity(Base):
    __tablename__ = 'liquidity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    daily_trading_volume = Column(Float)
    liquidity_on_exchanges = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Coins
    coin = relationship('Coins', back_populates='liquidity_records')

# 9. Whalecomics Table
class Whalecomics(Base):
    __tablename__ = 'whalecomics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    number_of_whales = Column(Integer)
    number_of_sharks = Column(Integer)
    whale_to_total_market_ratio = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Coins
    coin = relationship('Coins', back_populates='whalecomics_records')

# 10. Price Table
class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    price = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Coins
    coin = relationship('Coins', back_populates='prices')

