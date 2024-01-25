NUMBER_OF_STEPS = 20

import logging

from fastapi import APIRouter, Depends, HTTPException
from models import SimulationRequest, SimulationResponse, SimulationResponseRow

router = APIRouter()


# Dependency for Logging
def get_logger():
    return logger


# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.post("/simulate", response_model=SimulationResponse)
def simulate_system(
    simulation_request: SimulationRequest, logger: logging.Logger = Depends(get_logger)
) -> SimulationResponse:
    """
    Simulates the time-discrete dynamical system.

    The system's state is updated iteratively for N time steps.

    The function takes a SimulationRequest object containing the initial conditions and parameters
    of the dynamical system. The system's state is updated iteratively for N time steps.

    Parameters:
    - simulation_request: A SimulationRequest object containing the input parameters for the simulation.
    - logger: An optional logger for recording log messages during the simulation.

    Returns:
    - A SimulationResponse object that represents the result of the simulation.
    """
    r = simulation_request
    try:
        rows = []

        if r.delta_t <= 0:
            raise ValueError("Delta_t must be a positive value.")

        curr_x, curr_y, curr_z = (r.x0, r.y0, r.z0)

        for num in range(r.n):
            # Dynamical system equations
            x_next = curr_x + curr_z * r.sigma * (curr_y - curr_x) * r.delta_t
            y_next = curr_y + (curr_x * (r.rho - curr_z) - curr_z * curr_y) * r.delta_t
            z_next = curr_z + (curr_x * curr_y - r.beta * curr_z) * r.delta_t

            # Update the conditions for the next time step
            curr_x, curr_y, curr_z = x_next, y_next, z_next

            # Store the system state at the current time step
            rows.append(SimulationResponseRow(x=curr_x, y=curr_y, z=curr_z, n=num))

        return SimulationResponse(rows=rows)

    except ValueError as ve:
        logger.error(f"ValueError during simulation: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.exception(f"An unexpected error occurred during simulation: {e}")
        raise HTTPException(status_code=500, detail=str(e))
