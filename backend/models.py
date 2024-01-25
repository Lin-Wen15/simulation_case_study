DEFAULT_NUMBER_OF_STEPS = 20

from typing import List

from pydantic import BaseModel


class SimulationRequest(BaseModel):
    """

    Represents the input parameters for simulating a dynamical system.

    Parameters:
    - x0, y0, z0: Initial conditions in three-dimensional space.
    - sigma, rho, beta: Parameters affecting the system's behavior.
    - delta_t: Discrete time step size.
    - n: Number of time steps to simulate, defaulting to 20.

    """

    x0: float
    y0: float
    z0: float
    sigma: float
    rho: float
    beta: float
    delta_t: float
    n: int = DEFAULT_NUMBER_OF_STEPS


class SimulationResponseRow(BaseModel):

    """
    Represents a single row in the simulation response.

    Attributes:
    - x: x-coordinate of the system state.
    - y: y-coordinate of the system state.
    - z: z-coordinate of the system state.
    - n: Time step index.

    """

    x: float
    y: float
    z: float
    n: int


class SimulationResponse(BaseModel):

    """
    Represents the response containing the simulation results.

    Attributes:
    - rows: List of SimulationResponseRow objects representing the system state at each time step.

    """

    rows: List[SimulationResponseRow]
