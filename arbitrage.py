from dex_api import RaydiumAPI, OrcaAPI
import numpy as np

class ArbitrageCalculator:
    def __init__(self):
        self.fee_rate = 0.003  # 0.3% fee
        
    def calculate_profit(self, buy_price, sell_price, amount):
        gross_profit = (sell_price - buy_price) * amount
        fees = (buy_price * self.fee_rate) + (sell_price * self.fee_rate)
        net_profit = gross_profit - fees
        return net_profit
        
    def optimal_trade_size(self, pool1, pool2):
        # Рассчитываем оптимальный размер сделки по формуле арбитража
        k = (pool1["quote_reserve"] * pool2["base_reserve"]) / \
            (pool1["base_reserve"] * pool2["quote_reserve"])
        return np.sqrt(k) - 1

class ArbitrageFinder:
    @staticmethod
    def find_opportunities():
        opportunities = []
        
        # Пример для SOL/USDC
        raydium_pool = RaydiumAPI.get_pool_info(cfg.POOLS["SOL/USDC"]["raydium"])
        orca_pool = OrcaAPI.get_pool_info(cfg.POOLS["SOL/USDC"]["orca"])
        
        if raydium_pool and orca_pool:
            calculator = ArbitrageCalculator()
            trade_size = calculator.optimal_trade_size(raydium_pool, orca_pool)
            profit = calculator.calculate_profit(
                buy_price=raydium_pool["price"],
                sell_price=orca_pool["price"],
                amount=trade_size
            )
            
            if profit > cfg.MIN_PROFIT:
                opportunities.append({
                    "pair": "SOL/USDC",
                    "buy_at": "Raydium",
                    "sell_at": "Orca",
                    "profit": profit,
                    "amount": trade_size
                })
                
        return opportunities
