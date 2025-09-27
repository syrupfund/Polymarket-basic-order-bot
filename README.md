# Polymarket proxywallet Trading Bot

A simple Python bot that automatically trades on Polymarket using the CLOB API. This bot is designed for users with **email/Magic wallet** accounts on Polymarket.

## 🚀 Quick Start (5 Minutes Setup)

### Prerequisites
- Python 3.9+
- A Polymarket account (email login)
- At least one manual trade done on Polymarket (to set allowances)

### Step 1: Clone and Setup
```bash
git clone <repository-url>
cd polymarket-auto-trade-example

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Get Your Polymarket Credentials

1. **Do one manual trade** on Polymarket (any amount) - this sets up necessary permissions
2. **Export your private key**:
   - Go to Polymarket Settings
   - Click "Export Private Key"
   - Copy the private key
3. **Copy your proxy wallet address**:
   - Look below your profile picture on Polymarket
   - Copy the wallet address shown there

### Step 3: Configure Environment

Create a `.env` file in the root directory:
```
HOST=https://clob.polymarket.com
PK=your_exported_private_key_here
```

### Step 4: Update Configuration

Edit `src/helpers/clob_client.py` and replace:
```python
polymarket_proxy_address = "YOUR_PROXY_ADDRESS_HERE"
```
With your actual Polymarket proxy address:
```python
polymarket_proxy_address = "0x1234567890abcdef1234567890abcdef12345678"
```

### Step 5: Customize Your Trade

Edit `src/main.py` to modify:
- **Market**: Change `condition_id` to trade different markets
- **Price**: Change the `price` value (in dollars, e.g., 0.044 = $0.044)
- **Size**: Change the `size` value (number of shares)
- **Side**: Change to `BUY` or `SELL`

### Step 6: Run the Bot

```bash
python src/main.py
```

## 📊 How It Works

1. **Connects to your Polymarket email account** using exported credentials
2. **Automatically manages API keys** - no manual setup required
3. **Places trades using your Polymarket funds** - no need to transfer money
4. **No gas fees** - Polymarket covers transaction costs for email wallet users

## 🛠 Configuration Options

### Trading Parameters
```python
# In src/main.py
price = 0.044  # Price per share ($0.044)
size = 26      # Number of shares to buy/sell
side = BUY     # BUY or SELL
```

### Market Selection
```python
# Change this condition_id to trade different markets
condition_id = '0xbb96f092cb5d54138c6af2ae824bb276c3e20969fb2acfced30ac7f88f60862e'
```

Find condition IDs by:
- Browsing Polymarket markets
- Using the [Polymarket API](https://docs.polymarket.com/)
- Checking market URLs on Polymarket

## 📁 Project Structure

```
polymarket-auto-trade-example/
├── .env                    # Your environment variables
├── requirements.txt        # Python dependencies
└── src/
    ├── main.py            # Main bot script
    ├── helpers/
    │   ├── clob_client.py # CLOB API client setup
    │   └── generate_wallet.py # (Not needed for email wallets)
    ├── markets/
    │   └── get_markets.py # Market data fetching
    └── trades/
        └── trade_specific_market.py # Order execution
```

## ⚡ Key Advantages for Email Wallet Users

- ✅ **Polymarket interface** - Trading directly with the polymarket proxywallet enable an easier and better monitoring
- ✅ **No token allowances needed** - Set automatically after first manual trade
- ✅ **No MATIC required** - Polymarket covers gas fees
- ✅ **Uses your existing funds** - Trades with your Polymarket balance 
- ✅ **Automatic API management** - No manual credential setup
- ✅ **Simple setup** - Just export private key and run

## 🔒 Security Notes

- **Keep your private key secure** - Never share your `.env` file
- **Start with small amounts** - Test with $1-5 first
- **Understand markets** before trading
- **The private key is only for signing** - funds stay in your Polymarket account

## 🐛 Troubleshooting

### Common Issues:

**"Error: when sending a str, it must be a hex string"**
- Replace `YOUR_PROXY_ADDRESS_HERE` with your actual Polymarket address

**"No such file or directory: main.py"**
- Run from root directory: `python src/main.py`

**"HOST environment variable not found"**
- Make sure `.env` file is in root directory, not in `src/`

**"NoneType object has no attribute 'endswith'"**
- Check your `.env` file format (no quotes around values)

### Getting Help:

1. Check that you've done at least one manual trade on Polymarket
2. Verify your private key is correctly exported from Polymarket
3. Ensure your proxy address is copied from below your profile picture
4. Make sure `.env` file is in the correct location

## 📚 Resources

- [Polymarket CLOB API Documentation](https://docs.polymarket.com/)
- [Polymarket Python Client](https://github.com/Polymarket/py-clob-client)
- [YouTube Tutorial Video](https://www.youtube.com/watch?v=ZbFTmDgSe_4)

## ⚠️ Disclaimer

This code is for educational purposes and demonstrates API usage. **Use at your own risk.** 
- Only trade amounts you can afford to lose
- Test thoroughly with small amounts first
- Understand the markets you're trading
- This is not financial advice

## 🤝 Contributing

Feel free to submit issues, feature requests, or improvements. This is a community learning project!

---

**Happy Trading! 🚀**
