from fastapi import FastAPI, Body
import uvicorn


app = FastAPI()

data={}
@app.post("/classify")
def read_root():
    return data

@app.post("/create_data" )
async def create_data(doc: dict = Body(...)):
    global data
    data=doc
    return doc

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)