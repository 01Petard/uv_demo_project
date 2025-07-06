from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
async def hello():
    return JSONResponse(content={"message": "Hello，FastAPI"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
