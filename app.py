"""FastAPI wrapper exposing the Tic-Tac-Toe headless engine as a microservice.

Endpoints:
- GET /state -> current game state
- POST /move -> {"row":1,"col":2}
- POST /reset -> reset the game
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conint
from engine import GameEngine


class Move(BaseModel):
    row: conint(ge=1, le=3)
    col: conint(ge=1, le=3)


app = FastAPI(title='TicTacToe Engine')
engine = GameEngine()


@app.get('/state')
def state():
    return engine.get_state()


@app.post('/move')
def move(m: Move):
    try:
        return engine.make_move(m.row, m.col)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post('/reset')
def reset():
    engine.reset()
    return engine.get_state()
