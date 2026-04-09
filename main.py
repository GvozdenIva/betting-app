from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Betting AI läuft 🚀"}

@app.get("/value-bets")
def bets():
    teams = ["Arsenal", "Chelsea", "Bayern", "Dortmund"]
    
    data = []
    for t in teams:
        odds = round(random.uniform(1.5, 3.0), 2)
        ev = round(random.uniform(0.01, 0.1), 3)

        data.append({
            "team": t,
            "odds": odds,
            "ev": ev
        })

    return data
