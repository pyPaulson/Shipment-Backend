from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def get_all_shipment():
    return {"message": "Hello, World!"}   


@app.get("/shipment")
def get_shipment():
    return {"Details": "This is shipment"}