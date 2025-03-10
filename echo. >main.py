from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Bine ai venit la API-ul nostru"}
  
