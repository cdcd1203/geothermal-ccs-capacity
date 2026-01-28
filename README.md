# Geothermal Heat & CO₂ Storage Capacity Assessment
Geothermal heat and CO2 storage capacity assessment using Python
# Geothermal Heat Storage & CO₂ Capacity Assessment
## Code Documentation
- 📄 [CODEX – Code Walkthrough](./CODEX.md)
## Overview
This repository contains a **Python-based engineering model** for estimating:

- **Geothermal heat storage potential**
- **Geological CO₂ storage capacity**

in porous subsurface reservoirs.

The project is developed as a **technical portfolio** demonstrating how
**petroleum reservoir engineering concepts** can be applied to
**geothermal energy, CCS, and geo-energy transition projects**.

---

## Engineering Motivation
Subsurface energy projects—whether petroleum, geothermal, or CCS—share a common foundation:

> **Reservoir geometry, pore volume, and uncertainty control feasibility.**

This project focuses on **capacity-based assessment** as a first-order screening tool,
prior to detailed flow or coupled simulations.

---

## Key Objectives
- Estimate **static geothermal heat storage capacity**
- Quantify **CO₂ storage capacity** under supercritical conditions
- Compare **single-reservoir and multi-layer reservoir models**
- Visualize **heat vs. CO₂ storage trade-offs**
- Evaluate **porosity sensitivity** and uncertainty impacts

---

## Engineering Assumptions
To maintain clarity and transparency, the model assumes:

- Homogeneous properties within each layer
- Static thermal conditions (no heat loss over time)
- Water-filled pore space for geothermal heat estimation
- Constant-density supercritical CO₂
- No flow or injectivity simulation (capacity-focused)

These assumptions are **intentional** and reflect early-stage feasibility analysis.

---

## Methodology Summary

### Reservoir Geometry
Reservoir volume is defined by area and thickness, with pore volume calculated as:

V_pore = V_bulk × φ

---

### Geothermal Heat Storage
Thermal energy stored in the pore fluid is estimated using:

Q = V_pore · ρ · Cp · ΔT

Results are reported in **MJ**.

---

### CO₂ Storage Capacity
CO₂ storage capacity is estimated as:

M_CO2 = V_pore · S_CO2 · ρ_CO2

Results are reported in **tonnes**.

---

### Layer-Based Reservoir Model
The reservoir is divided into multiple layers, each with:

- Independent pore volume
- Independent CO₂ saturation

All calculations are performed using **vectorized NumPy operations** to preserve
clear alignment between geological layers and engineering results.

---

### Sensitivity Analysis
A ±10% porosity sensitivity analysis is conducted to demonstrate:

- Linear control of porosity on storage capacity
- The importance of uncertainty awareness in subsurface projects

---

## Results & Interpretation
- Storage capacity scales linearly with pore volume
- Layer-based results highlight geological heterogeneity
- Sensitivity analysis reinforces the role of uncertainty in early-stage decisions

The results provide **order-of-magnitude estimates** suitable for screening and comparison.

---

## Technologies Used
- **Python**
- **NumPy** – vectorized numerical computation
- **Matplotlib** – engineering visualization

All calculations are transparent and reproducible, avoiding black-box simulators.

---

## Repository Structure
```
.
├── Geothermal Heat Storage and CO2 Capacity Assessment.py
└── README.md
```

---

## Applications
- Petroleum reservoir screening and redevelopment studies
- Geothermal energy feasibility assessment
- CO₂ geological storage capacity evaluation
- Integrated geo-energy and energy transition projects

---

## Future Extensions
- Pressure- and temperature-dependent CO₂ properties
- Heat recovery efficiency factors
- Permeability and injectivity constraints
- Coupled thermal–hydraulic simulations
- Monte Carlo uncertainty analysis

---

## Author
**TROY**  
Focus: Petroleum Engineering / Geo-Energy / CCS  
Purpose: Technical portfolio and interview demonstration

---

## Notes
This project emphasizes **engineering insight, clarity, and explainability**
rather than numerical complexity, making it suitable for technical interviews
and early-stage project evaluation.
