from fastapi import FastAPI, HTTPException
from pipeline import RAGPipeline
from model_selector import ModelSelector

app = FastAPI()
pipeline = RAGPipeline()

@app.post("/ingest/")
async def ingest_document(file_path: str):
    pipeline.load_pdf(file_path)
    return {"status": "Document ingested"}

@app.post("/select_model/")
async def select_model(model_name: str):
    model = ModelSelector.select(model_name)
    return {"status": f"Model {model_name} selected"}

@app.post("/run/")
async def run_pipeline():
    result = pipeline.run()
    return {"result": result}
