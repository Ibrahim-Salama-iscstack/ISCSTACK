[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22278861.svg)](https://doi.org/10.5281/zenodo.22278861) [![pypi package](https://img.shields.io/badge/pypi-1.0.1-blue)](https://pypi.org/project/iscstack/) [![python](https://img.shields.io/badge/python-3-blue)](https://pypi.org/project/iscstack/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**DOI:** https://doi.org/10.5281/zenodo.22278861 | **Zenodo:** https://zenodo.org/records/22278861 | **Website:** https://iscstack.com
[![PyPI version](https://badge.fury.io/py/iscstack.svg)](https://pypi.org/project/iscstack/)
[![Python Version](https://img.shields.io/pypi/pyversions/iscstack.svg)](https://pypi.org/project/iscstack/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

```bash
pip install iscstack==1.0.1
# ISCStack™ - The Intelligent Systems Control Stack

Official Reference Implementation
Founder: Ibrahim Salama
Website: https://iscstack.com

## Constitution
Authority is a Runtime Property - verified at execution boundary.

## Layers
- MLVer: Semantic Verification
- MLROI: Risk & Outcome Intelligence  
- MLAIO: Orchestration
- AIGovCore: Policy Definition
- APIRegulator: Execution Boundary Enforcement (COMMIT NODE)
- MLRegulator: Compliance Mediation

## Installation
pip install iscstack

## Quick Start
from iscstack import APIRegulator
reg = APIRegulator()
result = reg.intercept({"env": "prod", "intent": "delete_db"})
# result = BLOCKED
