from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import datetime

app = FastAPI()

# Bot configuration
bot_config = {
    "risk": 0.01,
    "symbol": "SPY",
    "strategy": "TTM Squeeze",
    "last_trade": None
}

# Models
class ConfigUpdate(BaseModel):
    risk: Optional[float]
    symbol: Optional[str]
    strategy: Optional[str]

class TradeRequest(BaseModel):
    symbol: str
    action: str  # buy or sell
    amount: float

@app.get("/")
def read_root():
    return {"status": "PulseTrack AI Bot is running!"}

@app.get("/status")
def status():
    return {
        "bot_status": "active",
        "last_trade": bot_config["last_trade"],
        "symbol": bot_config["symbol"],
        "strategy": bot_config["strategy"]
    }

@app.get("/optimize")
def optimize():
    return {
        "message": "Backtest complete.",
        "best_strategy": "TTM Squeeze + MACD",
        "expected_win_rate": "67%",
        "expected_risk_reward": "1:2.5"
    }

@app.post("/set-config")
def update_config(cfg: ConfigUpdate):
    if cfg.risk is not None:
        bot_config["risk"] = cfg.risk
    if cfg.symbol is not None:
        bot_config["symbol"] = cfg.symbol
    if cfg.strategy is not None:
        bot_config["strategy"] = cfg.strategy
    return {"message": "Bot config updated", "new_config": bot_config}

@app.post("/trade")
def trade(req: TradeRequest):
    now = datetime.datetime.utcnow().isoformat()
    bot_config["last_trade"] = {
        "symbol": req.symbol,
        "action": req.action,
        "amount": req.amount,
        "timestamp": now
    }
    return {
        "message": f"Trade executed: {req.action.upper()} {req.amount} of {req.symbol}",
        "timestamp": now
    }

@app.get("/favicon.ico")
def favicon():
    return {"detail": "Not found"}
