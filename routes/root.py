from fastapi import APIRouter

ROOT = APIRouter()


@ROOT.get("/")
def root():
    return "Back-end Challenge 2021 🏅 - Space Flight News"
