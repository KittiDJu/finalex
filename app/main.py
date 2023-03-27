from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/mothly/{money}")
def get_money(money: int):

    
handler = Mangum(app)
