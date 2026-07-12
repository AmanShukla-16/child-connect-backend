from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Vendor, Booking, Parent, LoginParent
from db import db, cursor
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.post("/add_vendor")
def add_vendor(vendor: Vendor):

    sql = """
    INSERT INTO vendors
    (
        name,
        category,
        city,
        phone,
        description,
        fees,
        morning_batch,
        evening_batch,
        address,
        rating,
        image
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        vendor.name,
        vendor.category,
        vendor.city,
        vendor.phone,
        vendor.description,
        vendor.fees,
        vendor.morning_batch,
        vendor.evening_batch,
        vendor.address,
        vendor.rating,
        vendor.image
    )

    cursor.execute(sql, values)
    db.commit()

    return {"message": "Vendor Added Successfully"}

@app.post("/book_vendor")
def book_vendor(booking: Booking):

    sql = """
    INSERT INTO bookings
    (parent_name, parent_phone, vendor_id, vendor_name, booking_date, batch_time)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        booking.parent_name,
        booking.parent_phone,
        booking.vendor_id,
        booking.vendor_name,
        booking.booking_date,
        booking.batch_time
    )

    cursor.execute(sql, values)
    db.commit()

    return {"message": "Booking Successful"}
@app.post("/register_parent")
def register_parent(parent: Parent):

    # Check if email already exists
    cursor.execute(
        "SELECT * FROM parents WHERE email=%s",
        (parent.email,)
    )

    existing = cursor.fetchone()

    if existing:
        return {
            "success": False,
            "message": "Email already registered"
        }

    sql = """
    INSERT INTO parents
    (name,email,phone,password)
    VALUES(%s,%s,%s,%s)
    """

    values = (
        parent.name,
        parent.email,
        parent.phone,
        parent.password
    )

    cursor.execute(sql, values)
    db.commit()

    return {
        "success": True,
        "message": "Registration Successful"
    }

@app.post("/login_parent")
def login_parent(parent: LoginParent):

    cursor.execute(
        "SELECT * FROM parents WHERE email=%s AND password=%s",
        (parent.email, parent.password)
    )

    user = cursor.fetchone()

    if user:
        return {
            "success": True,
            "message": "Login Successful",
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "phone": user[3]
        }

    return {
        "success": False,
        "message": "Invalid Email or Password"
    }

@app.get("/vendors")
def get_vendors():

    cursor.execute("SELECT * FROM vendors")
    rows = cursor.fetchall()

    vendors = []

    for row in rows:
        vendors.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "city": row[3],
            "phone": row[4],
            "description": row[5],
            "fees": row[6],
            "morning_batch": row[7],
            "evening_batch": row[8],
            "address": row[9],
            "rating": row[10],
            "image": row[11]
        })

    return vendors

@app.get("/bookings")
def get_bookings():

    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()

    bookings = []

    for row in rows:
        bookings.append({
            "id": row[0],
            "parent_name": row[1],
            "parent_phone": row[2],
            "vendor_id": row[3],
            "vendor_name": row[4],
            "booking_date": str(row[5]),
            "batch_time": row[6],
            "status": row[7]
        })

    return bookings

@app.get("/vendors/{category}")
def get_vendors_by_category(category: str):

    sql = "SELECT * FROM vendors WHERE category = %s"
    cursor.execute(sql, (category,))
    rows = cursor.fetchall()

    vendors = []

    for row in rows:
        vendors.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "city": row[3],
            "phone": row[4],
            "description": row[5],
            "fees": row[6],
            "morning_batch": row[7],
            "evening_batch": row[8],
            "address": row[9],
            "rating": row[10],
            "image": row[11]
        })

    return vendors