# Blackrock Case Study Project # 

This repository contains a FastAPI application that exposes an API endpoint for simulating the discrete time dynamical system to approximate the point's position.  The simulation parameters are provided in the request payload.

## Installation

### Pre-Installation:
Before installing the simulation application, you need to have the following installed: 

1. Python 3.7 or above - check by typing `python -V`. If the output does not start with `3.7` or greater, you need to install a later version of Python. Using [pyenv](https://github.com/pyenv/pyenv) is highly recommended!

2. [Homebrew](https://brew.sh) if you are developing on a Mac.

3. The AWS Command Line Interface - check by typing `aws --version`. The output should start with `aws-cli/2.4.2` - if it does not, you need to install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

### Installation: Clone the Repo:
```bash
$ git clone https://github.com/Lin-Wen15/simulation_case_study.git
$ cd simulation_case_study/backend
$ python -m venv .br-venv
$ source .br-venv/bin/activate (On Windows: `.venv\Scripts\activate`)
$ pip install -r requirements.txt
$ pip install fastapi
```

## Usage:
   - Navigate to the `backend/` directory: `cd simulation_case_study-root/backend`
   - Run the simulation application on the local server: `uvicorn main:app --reload`
   - On a new terminal, submit your POST request. Here's an example curl command with input parameters, you can change the parameters with the same JSON playload: 
   ```bash
   curl -X POST "http://127.0.0.1:8000/simulations/simulate" -H "Content-Type: application/json" -d '{"x0": 1.0, "y0": 2.0, "z0": 3.0, "sigma": 0.5, "rho": 0.8, "beta": 0.2, "delta_t": 0.01, "n": 20}'
   ```
   - You can check the detailed information about the available endpoints, request parameters, and response formats at http://127.0.0.1:8000/docs while the server is running.

## Infrastructure and Deploy Application on ECS:

   - Navigate to the `infrastructure/` directory.
   - Install Terraform and AWS CLI: `brew install terraform`  (On Windows: `choco install terraform`)
   - Run the Terraform Commands:
   ```bash
   terraform init
   terraform plan -var="aws_access_key=your-access-key" -var="aws_secret_key=your-secret-key"
   terraform apply -var="aws_access_key=your-access-key" -var="aws_secret_key=your-secret-key"
   ```

## Run unittests:
```bash
cd simulation_case_study/backend
python -m unittest tests.test_simulation
```

### Notes:
- The simulate_system function in dynamical_simulation.py contains the logic for simulating the dynamical system.