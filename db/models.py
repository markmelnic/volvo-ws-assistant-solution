from . import DB_BASE

from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, Boolean

"""
Create staff,  customer, vehicle and inquiry models for an API, 
which enables the customers to leave inquiries regardinga vehicle they are interested in,
to which staff can then respond.
"""


class Staff(DB_BASE):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Staff {self.username}>"


class Customer(DB_BASE):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Customer {self.name}>"


class Vehicle(DB_BASE):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    color = Column(String, index=True)
    price = Column(Integer, index=True)
    is_sold = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Vehicle {self.make} {self.model}>"


class Inquiry(DB_BASE):
    __tablename__ = "inquiry"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True)
    vehicle_id = Column(Integer, index=True)
    message = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Inquiry {self.id}>"
