import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler
from solana.rpc.async_api import AsyncClient
from arbitrage import ArbitrageFinder

class ArbitrageBot:
    def __init__(self):
        self.client = AsyncClient(cfg.RPC_URL)
        self.is_running = False
        self.app = Application.builder().token(cfg.TG_TOKEN).build()
        
        # Регистрация команд
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("stop", self.stop))
        self.app.add_handler(CommandHandler("status", self.status))

    async def start(self, update: Update, _):
        if update.effective_user.id != cfg.ADMIN_ID:
            return
        self.is_running = True
        await update.message.reply_text("✅ Arbitrage bot started")
        asyncio.create_task(self.run_arbitrage())

    async def stop(self, update: Update, _):
        self.is_running = False
        await update.message.reply_text("🛑 Bot stopped")

    async def status(self, update: Update, _):
        status = "🔄 Running" if self.is_running else "🛑 Stopped"
        await update.message.reply_text(f"Status: {status}")

    async def run_arbitrage(self):
        while self.is_running:
            try:
                opportunities = ArbitrageFinder.find_opportunities()
                if opportunities:
                    await self.execute_trades(opportunities)
                await asyncio.sleep(5)
            except Exception as e:
                print(f"Error: {e}")
                await self.stop(None)

    async def execute_trades(self, opportunities):
        for opp in opportunities:
            print(f"Executing arbitrage: {opp}")
            # Здесь реализация исполнения через Solana
            # tx = create_arbitrage_transaction(opp)
            # await client.send_transaction(tx)

    def run(self):
        self.app.run_polling()

if __name__ == "__main__":
    bot = ArbitrageBot()
    bot.run()
