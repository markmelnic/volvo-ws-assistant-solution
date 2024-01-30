from . import *

router = APIRouter()

"""
Create the staff router.
It should include CRUD methods,
as well as a method to respond to customer inquiries.
"""


@router.get("/staff")
def get_staff(db: Session = Depends(get_db)):
    staff = db.query(Staff).all()

    return {"data": staff}


@router.post("/staff", status_code=201)
def create_staff(json: JsonData, db: Session = Depends(get_db)):
    data = json.read()

    if db.query(Staff).filter(Staff.username == data["username"]).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    if db.query(Staff).filter(Staff.email == data["email"]).first():
        raise HTTPException(status_code=400, detail="Email already taken")

    new_staff = Staff(**data)

    db.add(new_staff)
    db.commit()

    db.refresh(new_staff)

    return {"data": new_staff}


@router.put("/staff/{id}")
def update_staff(id: int, json: JsonData, db: Session = Depends(get_db)):
    data = json.read()

    staff = db.query(Staff).filter(Staff.id == id).first()

    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")

    for key, value in data.items():
        if (
            key != "id"
            and key != "password"
            and key != "is_admin"
            and key != "is_active"
        ):
            setattr(staff, key, value)

    db.commit()

    return {"data": staff}


@router.delete("/staff/{id}")
def delete_staff(id: int, db: Session = Depends(get_db)):
    staff = db.query(Staff).filter(Staff.id == id).first()

    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")

    db.delete(staff)
    db.commit()

    return {"data": staff}


@router.post("/staff/respond/{id}")
def respond_to_inquiry(id: int, json: JsonData, db: Session = Depends(get_db)):
    data = json.read()

    staff = db.query(Staff).filter(Staff.id == id).first()

    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")

    inquiry = db.query(Inquiry).filter(Inquiry.id == data["inquiry_id"]).first()

    if not inquiry:
        raise HTTPException(status_code=404, detail="Inquiry not found")

    inquiry.responded_by = staff.id
    inquiry.response = data["response"]

    db.commit()

    return {"data": inquiry}
