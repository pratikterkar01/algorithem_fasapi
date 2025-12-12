from fastapi import APIRouter, HTTPException
from Algorithems import dsa_week_1_1

router = APIRouter()

@router.get("/timer")
def hello_world():
    s = dsa_week_1_1.NumberUtils()
    t = s.test_timer()
    return t


@router.get("/factor/{int}")
def number_factor(int: int):
    week1 = dsa_week_1_1.NumberUtils()
    factorlist = week1.factor(int)
    return factorlist
