import os
from dotenv import load_dotenv
from py_clob_client.order_builder.constants import BUY
from helpers.clob_client import create_clob_client
from markets.get_markets import get_market
from trades.trade_specific_market import create_and_submit_order

def main():
    load_dotenv()
    
    print("=== Simple Polymarket Bot ===")
    
    # Check if we have the required private key
    if not os.getenv('PK'):
        print("❌ Missing PK in .env file")
        print("💡 Export your private key from Polymarket Settings and add to .env")
        return
    
    print("✅ Private key found")
    print("💡 Make sure you've done at least one manual trade on Polymarket first!")
    
    try:
        # Step 1: Get market data
        print("📊 Fetching market data...")
        condition_id = '0x6a8c775d3a7ab901a5c4595dbc33478d654dc3b293be2b80fd64500cabbfcc37'
        market = get_market(condition_id)
        yes_token = next((item for item in market['tokens'] if item.get('outcome') == 'Yes'), None)
        
        print(f"📈 Market: {market.get('question', 'Unknown')}")
        
        # Step 2: Place trade
        print("💰 Placing order...")
        price = 0.044  # $0.044 per share
        size = 26      # 26 shares  
        side = BUY     # BUY or SELL
        
        print(f"   {side} {size} shares at ${price} each")
        print(f"   Total: ${price * size:.2f}")
        
        create_and_submit_order(yes_token['token_id'], side, price, size)
        print("✅ Order placed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()