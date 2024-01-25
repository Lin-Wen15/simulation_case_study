import unittest

from fastapi.testclient import TestClient
from main import app


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_simulate_valid(self):
        request_valid_input = {
            "x0": 1.00,
            "y0": 2.30,
            "z0": 3.80,
            "sigma": 0.10,
            "rho": 28.00,
            "beta": 8.00,
            "delta_t": 0.10,
        }
        response = self.client.post("/simulations/simulate", json=request_valid_input)
        assert response.status_code == 200
        assert response.json() == {
            "rows": [
                {"x": 1.0493999999999999, "y": 3.846, "z": 0.9899999999999998, "n": 0},
                {"x": 1.07708634, "y": 6.2996754, "z": 0.6015992399999999, "n": 1},
                {
                    "x": 1.1085053960932831,
                    "y": 8.871731726355492,
                    "z": 0.7988492799774035,
                    "n": 2,
                },
                {
                    "x": 1.170521873735599,
                    "y": 11.178276311489489,
                    "z": 1.1432061051311848,
                    "n": 3,
                },
                {
                    "x": 1.2849311334545384,
                    "y": 13.044015410310944,
                    "z": 1.5370829143521305,
                    "n": 4,
                },
                {
                    "x": 1.465678008758366,
                    "y": 14.439344692674958,
                    "z": 1.9834827334673568,
                    "n": 5,
                },
                {
                    "x": 1.7230084473314586,
                    "y": 15.38850932682845,
                    "z": 2.5130395443870226,
                    "n": 6,
                },
                {
                    "x": 2.0664278883717744,
                    "y": 15.912740896262008,
                    "z": 3.15406106507384,
                    "n": 7,
                },
                {
                    "x": 2.5031490559018947,
                    "y": 16.02799935910254,
                    "z": 3.919065369861756,
                    "n": 8,
                },
                {
                    "x": 3.033196780460274,
                    "y": 15.774338513926601,
                    "z": 4.7958602203457215,
                    "n": 9,
                },
                {
                    "x": 3.644244128473453,
                    "y": 15.24745846310555,
                    "z": 5.743839323502411,
                    "n": 10,
                },
                {
                    "x": 4.31071411621632,
                    "y": 14.60025159948883,
                    "z": 6.705313962532008,
                    "n": 11,
                },
                {
                    "x": 5.000659909762156,
                    "y": 13.98985487904634,
                    "z": 7.634813859529043,
                    "n": 12,
                },
                {
                    "x": 5.686968213137153,
                    "y": 13.49279807546174,
                    "z": 8.522813415609562,
                    "n": 13,
                },
                {
                    "x": 6.35224452784301,
                    "y": 13.069752128973102,
                    "z": 9.377874059264819,
                    "n": 14,
                },
                {
                    "x": 6.982203930598532,
                    "y": 12.642332944225144,
                    "z": 10.177800956006354,
                    "n": 15,
                },
                {
                    "x": 7.558280595458614,
                    "y": 12.219040933324797,
                    "z": 10.862694868711682,
                    "n": 16,
                },
                {
                    "x": 8.064564769522953,
                    "y": 11.89872569185125,
                    "z": 11.408032971888668,
                    "n": 17,
                },
                {
                    "x": 8.501967111737436,
                    "y": 11.705319465440773,
                    "z": 11.877410996049855,
                    "n": 18,
                },
                {
                    "x": 8.882442436438417,
                    "y": 11.509802599094884,
                    "z": 12.32730631196572,
                    "n": 19,
                },
            ]
        }

    def test_simulate_non_positive_delta_t(self):
        invalid_delta_t_params = {
            "x0": 2.00,
            "y0": 3.00,
            "z0": 0.00,
            "sigma": 1.00,
            "rho": 10.00,
            "beta": 5.00,
            "delta_t": -0.50,
        }
        response = self.client.post(
            "/simulations/simulate", json=invalid_delta_t_params
        )
        assert response.status_code == 400
        assert response.json() == {"detail": "Delta_t must be a positive value."}

    def test_simulate_invalid_input_type(self):
        invalid_type_params = {
            "x0": 1.37,
            "y0": 3.00,
            "z0": 2.08,
            "sigma": "apple",
            "rho": 10.00,
            "beta": 5.00,
            "delta_t": 0.20,
        }
        response = self.client.post("/simulations/simulate", json=invalid_type_params)
        assert response.status_code == 422
        assert response.json() == {
            "detail": [
                {
                    "type": "float_parsing",
                    "loc": ["body", "sigma"],
                    "msg": "Input should be a valid number, unable to parse string as a number",
                    "input": "apple",
                    "url": "https://errors.pydantic.dev/2.5/v/float_parsing",
                }
            ]
        }


if __name__ == "__main__":
    unittest.main()
