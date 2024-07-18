import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()


class TextRequest(BaseModel):
    text: str


model = pipeline('text-generation', model='gpt2')


@app.post('/api/generate')
async def generate_text(request: TextRequest):
    try:
        generated = model(request.text, max_length=50)
        return {"generated_text": generated[0]['generated_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/')
async def read_root():
    return {"message": "ML API is running"}


if __name__ == "__main__":
    uvicorn.run('ml_api.app:app', host="0.0.0.0", port=8000, log_level="info", reload=True)

