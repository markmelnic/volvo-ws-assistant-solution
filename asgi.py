from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI


app: FastAPI = FastAPI()

from routers import server_router, staff_router, vehicle_router, customer_router

app.include_router(server_router)
app.include_router(staff_router)
app.include_router(vehicle_router)
app.include_router(customer_router)


if __name__ == "__main__":
    import uvicorn, psycopg2

    uvicorn.run(
        "asgi:app", host="127.0.0.1", port=8000, reload=True
    )  # alternatively host='0.0.0.0'
