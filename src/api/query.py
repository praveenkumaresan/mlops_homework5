from fastapi import APIRouter
from typing import List
from src.retriever.retriever import retrieve_similar_excerpts

router = APIRouter()

from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    query: str
    top_k: int = Field(default=5, ge=1)  # ge=1 means greater than or equal to 1

class QueryResponse(BaseModel):
    excerpts: List[str]

@router.post("/query", response_model=QueryResponse)
def query_excerpts(request: QueryRequest):
    results = retrieve_similar_excerpts(request.query, request.top_k)
    return QueryResponse(excerpts=results['prompt'].tolist())
