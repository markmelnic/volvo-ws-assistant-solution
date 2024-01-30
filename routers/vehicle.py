from . import *

router = APIRouter()

"""
Implement the vehicle router.
It should only contain CRUD methods.
"""


@router.get("/vehicle")
def get_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(Vehicle).all()

    return {"data": vehicles}


@router.post("/vehicle", status_code=201)
def create_vehicle(json: JsonData, db: Session = Depends(get_db)):
    data = json.read()

    new_vehicle = Vehicle(**data)

    db.add(new_vehicle)
    db.commit()

    db.refresh(new_vehicle)

    return {"data": new_vehicle}


@router.put("/vehicle/{id}")
def update_vehicle(id: int, json: JsonData, db: Session = Depends(get_db)):
    data = json.read()

    vehicle = db.query(Vehicle).filter(Vehicle.id == id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    for key, value in data.items():
        if key != "id":
            setattr(vehicle, key, value)

    db.commit()

    return {"data": vehicle}


@router.delete("/vehicle/{id}")
def delete_vehicle(id: int, db: Session = Depends(get_db)):
    vehicle = db.query(Vehicle).filter(Vehicle.id == id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    db.delete(vehicle)
    db.commit()

    return {"data": "Vehicle deleted"}
