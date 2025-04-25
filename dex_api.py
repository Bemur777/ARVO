import requests
import numpy as np

class RaydiumAPI:
    @staticmethod
    def get_pool_info(pool_address: str):
        url = f"https://api.raydium.io/v2/sdk/liquidity/mainnet.json"
        response = requests.get(url)
        for pool in response.json()["official"]:
            if pool["id"] == pool_address:
                return {
                    "price": pool["price"],
                    "base_reserve": float(pool["base_reserve"]),
                    "quote_reserve": float(pool["quote_reserve"])
                }
        return None

class OrcaAPI:
    @staticmethod
    def get_pool_info(pool_address: str):
        url = f"https://api.orca.so/pools"
        response = requests.get(url)
        for pool in response.json()["pools"]:
            if pool["address"] == pool_address:
                return {
                    "price": pool["price"],
                    "volume": pool["volume"]
                }
        return None
