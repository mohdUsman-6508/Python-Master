from fastapi import FastAPI, UploadFile

app=FastAPI()

@app.get("/")
def home():
  return {'data':'Welcome home'}

@app.get("/contact")
def contact():
  return {"data":"Thanks for contacting me"}


@app.post("/upload")
def handleImage(files:list[UploadFile]):
  print(files)
  return {"status":'got the files'}


# ye lo ban gaya server

import uvicorn
uvicorn.run(app)
