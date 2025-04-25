import os
from dotenv import load_dotenv
from solders.pubkey import Pubkey

load_dotenv()

class Config:
    RPC_URL = os.getenv("RPC_URL", "https://api.mainnet-beta.solana.com")
    WALLET = Pubkey.from_string(os.getenv("WALLET"))
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")
    TG_TOKEN = os.getenv("TG_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    
    # Arbitrage параметры
    MIN_PROFIT = 0.05  # SOL
    SLIPPAGE = 0.8  # %
    POOLS = {
        "SOL/USDC": {
            "raydium": "58oQChx4yWmvKdwLLZzwBaygHQsQwghb綾WAwguVaDwB",
            "orca": "9WDPi1uZVxrJ2R6jY5o3VQ2pL7QXsQWa6QJUwqB5L5J7"
        }
    }

cfg = Config()
