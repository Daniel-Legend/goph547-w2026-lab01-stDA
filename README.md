# GOPH 547 Lab 1

*Semester:* W2026

*Instructor:* B. Karchewski

*Author(s):* Daniel Afolabi```
git clone https://github.com/Daniel-Legend/goph547-w2026-lab01-stDA

A repository for GOPH 547 Lab 1.
Includes functions for computing gravity potential
and gravity effect for point masses.
Includes examples generating contour plots
simulating corrected gravity data for mass anomalies.
Loads a data file containing density data and generates
synthetic corrected survey data.

## Installation

You can download this repo by making a clone using git:

```
git clone https://github.com/Daniel-Legend/goph547-w2026-lab01-stDA
```

Then navigate into the repo, make a virtual environment

```
cd /path/to/repo/goph547-lab01-stBK
virtualenv .venv
source .venv/bin/activate  # (or ./.venv/Scripts/activate on Windows)
pip install -e .
```

## Usage

You can run the examples using the driver scripts:

```
python examples/driver_single_mass.py
python examples/driver_multi_mass.py
python examples/driver_mass_anomaly.py
```
This will generate several contour plots of synthetic gravity survey data saved as image files.

```
