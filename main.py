from pydantic import BaseModel
import models
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Flight
import requests

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

# class StockRequest(BaseModel):
#     symbol: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request, db: Session=Depends(get_db)):
    """
    displays the stock screener dashboard
    """
    airline = db.query(Flight.airline).all()
    # airline = db.query(Flight.airline).all()
    price = db.query(Flight.price).all()
    # departure = db.query(Flight.departure).all()
    # duration = db.query(Flight.duration).all()
    return templates.TemplateResponse("home.html", {
        "request": request, "airlines": airline, "prices": price
    })

# , "departures": departure, "durations": duration

def fetch_flight_data(id: int):
    db = SessionLocal()
    stock = db.query(Flight).filter(Flight.id == id).first()

@app.post("/flight")
async def create_stock(background_tasks: BackgroundTasks,db: Session=Depends(get_db)):
    """
    creates a stock and stores it in the database
    """
    flight = Flight()

    # req = requests.get('https://api.flightapi.io/onewaytrip/632ddcfccaa6ed253fcf9e6e/BER/CDG/2022-10-03/2/0/1/Economy/EUR')

    # data = req.json()
    # for data_flight in data['legs']:
    #     flight.airline = data_flight['airlineCodes']
    #     flight.price = 100

    db.add(flight)
    db.commit()

    background_tasks.add_task(fetch_flight_data, flight.id)

    return {
        "code": "successs",
        "message": "stock created"
    }