from fastapi import APIRouter, status, Depends, HTTPException
from typing import Any
from pydantic import BaseModel

from db import *


class JsonData(BaseModel):
    data: Any

    def read(self):
        return self.data


from .server import router as server_router
from .staff import router as staff_router
from .vehicle import router as vehicle_router
from .customer import router as customer_router
