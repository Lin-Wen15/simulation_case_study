from fastapi import FastAPI
from simulations.dynamical_simulation import router

app = FastAPI()

app.include_router(router, prefix="/simulations", tags=["simulations"])
