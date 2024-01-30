from . import *

router = APIRouter()

"""
Create the customer router.
It should include CRUD methods,
as well as a method to leave an inquiry regarding a vehicle.
"""


@router.get("/customer")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer).all()

    return {"data": customers}


@router.post("/customer", status_code=201)
def create_customer(json: JsonData, db: Session = Depends(get_db)):
    data = json.read()

    if db.query(Customer).filter(Customer.username == data["username"]).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    if db.query(Customer).filter(Customer.email == data["email"]).first():
        raise HTTPException(status_code=400, detail="Email already taken")

    new_customer = Customer(**data)

    db.add(new_customer)
    db.commit()

    db.refresh(new_customer)

    return {"data": new_customer}


@router.put("/customer/{id}")
def update_customer(id: int, json: JsonData, db: Session = Depends(get_db)):
    data = json.read()

    customer = db.query(Customer).filter(Customer.id == id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    for key, value in data.items():
        if (
            key != "id"
            and key != "password"
            and key != "is_admin"
            and key != "is_active"
        ):
            setattr(customer, key, value)

    db.commit()

    return {"data": customer}


@router.delete("/customer/{id}")
def delete_customer(id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    db.delete(customer)
    db.commit()

    return {"data": "Customer deleted"}


@router.post("/customer/{id}/inquire", status_code=201)
def create_inquire(id: int, json: JsonData, db: Session = Depends(get_db)):
    data = json.read()

    customer = db.query(Customer).filter(Customer.id == id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    if not db.query(Vehicle).filter(Vehicle.id == data["vehicle_id"]).first():
        raise HTTPException(status_code=404, detail="Vehicle not found")

    new_inquiry = Inquiry(**data)

    db.add(new_inquiry)
    db.commit()

    db.refresh(new_inquiry)

    return {"data": new_inquiry}
