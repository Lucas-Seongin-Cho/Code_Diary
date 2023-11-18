# Upbit Auto Trading Bot

This Python script is an example of a simple automated trading bot using the Upbit API. The bot implements a basic strategy known as the "Moving Average and Bollinger Bands Strategy" to make buy/sell decisions for Bitcoin (BTC) against the Korean Won (KRW). The strategy involves the following components:

- **Moving Average (MA15):** The bot calculates the 15-day simple moving average of the closing prices to identify trends.

- **Bollinger Bands:** The target price for buying is determined based on the Bollinger Bands strategy, where the target price is set at the previous day's closing price plus half of the day's high-low range.

- **Buy Condition:** If the current price is higher than both the target price and the 15-day moving average, and the available KRW balance is greater than 5000 KRW, the bot executes a market buy order for Bitcoin.

- **Sell Condition:** If the current time is outside the specified trading time window (9:00 AM to 8:59:50 AM next day) and the Bitcoin balance is greater than 0.00008 BTC, the bot executes a market sell order for Bitcoin.

## Prerequisites

To run this script, you need to have:

- Python installed on your machine.
- The required Python packages installed. You can install them using:

   ```bash
   pip install pyupbit
   ```

## Usage

1. Set your Upbit API access and secret keys in the `access` and `secret` variables.
2. Make sure you have sufficient funds (KRW) in your Upbit account for trading.
3. Run the script:

   ```bash
   python upbit_auto_trader.py
   ```

   The script will start executing the trading strategy based on the defined conditions.

## Important Note

- This script is a basic example and might not be suitable for actual trading without further customization and thorough testing.
- It's essential to understand the risks involved in automated trading and use this script responsibly.
- Make sure to comply with Upbit's terms of service and API usage policies.

## Disclaimer

This trading bot script is provided for educational and informational purposes only. Trading cryptocurrencies involves significant risk, and past performance is not indicative of future results. The author is not responsible for any losses incurred while using this script. Use it at your own risk and discretion.
