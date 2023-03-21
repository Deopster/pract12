from fastapi import FastAPI,HTTPException
app = FastAPI()

@app.get("/fir_hello")
def read_root():
    return {"output": "hello from first"}

@app.get("/fir_bye")
def read_root():
    return {"output": "bye from first"}
@app.get("/health")
def health():
    return