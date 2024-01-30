import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.testclient import TestClient


app: FastAPI = FastAPI()

from routers import server_router, staff_router, vehicle_router, customer_router

app.include_router(server_router)
app.include_router(staff_router)
app.include_router(vehicle_router)
app.include_router(customer_router)


client = TestClient(app)
