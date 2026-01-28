# =========================================================
# Geothermal Heat Storage & CO2 Capacity Assessment
# =========================================================
# Author: Your Name
# Purpose: Self-learning / Portfolio
# =========================================================

# -------------------- Imports --------------------
import numpy as np
import matplotlib.pyplot as plt

# -------------------- Physical constants --------------------
RHO_WATER = 1000.0      # kg/m3
CP_WATER = 4186.0       # J/kg/K
RHO_CO2 = 700.0         # kg/m3 (supercritical CO2)

# =========================================================
# Step 1: Reservoir geometry
# =========================================================
A = 1e6        # m2 (1 km2)
h = 50.0       # m
phi = 0.15     # porosity (-)

V_bulk = A * h                 # m3
V_pore = V_bulk * phi          # m3

# =========================================================
# Step 2: Thermal conditions
# =========================================================
T_res = 150.0    # °C
T_min = 50.0     # °C
delta_T = T_res - T_min

# =========================================================
# Step 3: Engineering functions
# =========================================================
def heat_storage(pore_volume, rho, cp, dT):
    """
    Calculate geothermal heat storage (MJ)
    """
    Q_J = pore_volume * rho * cp * dT
    return Q_J / 1e6  # MJ


def co2_storage(pore_volume, S_co2, rho):
    """
    Calculate CO2 storage capacity (tonnes)
    """
    M_kg = pore_volume * S_co2 * rho
    return M_kg / 1000  # tonnes

# =========================================================
# Step 4: Single-reservoir results
# =========================================================
Q_total = heat_storage(V_pore, RHO_WATER, CP_WATER, delta_T)
M_CO2_total = co2_storage(V_pore, S_co2=0.6, rho=RHO_CO2)

print("========== Single Reservoir ==========")
print(f"Reservoir volume : {V_bulk:,.0f} m³")
print(f"Pore volume      : {V_pore:,.0f} m³")
print(f"Heat storage     : {Q_total:,.2f} MJ")
print(f"CO2 capacity     : {M_CO2_total:,.2f} tonnes")
print("======================================\n")

# =========================================================
# Step 5: Layer-based model
# =========================================================
layers = ['Layer 1', 'Layer 2', 'Layer 3']
pore_volumes = np.array([2.0e6, 1.5e6, 1.8e6])
S_CO2_layers = np.array([0.6, 0.5, 0.55])

heat_layers = heat_storage(pore_volumes, RHO_WATER, CP_WATER, delta_T)
co2_layers = co2_storage(pore_volumes, S_CO2_layers, RHO_CO2)

# =========================================================
# Step 6: Plot 1 – Heat storage per layer
# =========================================================
plt.figure(figsize=(8, 4))
plt.bar(
    layers,
    heat_layers,
    color='#C0392B',
    edgecolor='black',
    linewidth=0.8
)
plt.ylabel('Heat Energy (MJ)')
plt.title('Geothermal Heat Storage per Layer')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# =========================================================
# Step 7: Plot 2 – Heat vs CO2 (Dual Axis, Layer-based)
# =========================================================
x = np.arange(len(layers))
width = 0.35

fig, ax1 = plt.subplots(figsize=(9, 5))
ax2 = ax1.twinx()

ax1.bar(
    x - width/2,
    heat_layers,
    width,
    color='#E74C3C',
    edgecolor='black',
    alpha=0.85,
    label='Heat (MJ)'
)
ax2.bar(
    x + width/2,
    co2_layers,
    width,
    color='#27AE60',
    edgecolor='black',
    alpha=0.85,
    label='CO₂ (tonnes)'
)

ax1.set_ylabel('Heat (MJ)', color='#C0392B')
ax2.set_ylabel('CO₂ (tonnes)', color='#1E8449')
ax1.set_xticks(x)
ax1.set_xticklabels(layers)
plt.title('Geothermal Heat vs CO₂ Storage (Layer-based)')
ax1.grid(axis='y', linestyle='--', alpha=0.4)

# Combined legend
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc='upper left')

fig.tight_layout()
plt.show()

# =========================================================
# Step 8: Sensitivity analysis (porosity ±10%)
# =========================================================
phi_low = phi * 0.9
phi_high = phi * 1.1

V_pore_low = V_bulk * phi_low
V_pore_high = V_bulk * phi_high

heat_low = heat_storage(V_pore_low, RHO_WATER, CP_WATER, delta_T)
heat_base = heat_storage(V_pore, RHO_WATER, CP_WATER, delta_T)
heat_high = heat_storage(V_pore_high, RHO_WATER, CP_WATER, delta_T)

co2_low = co2_storage(V_pore_low, 0.6, RHO_CO2)
co2_base = co2_storage(V_pore, 0.6, RHO_CO2)
co2_high = co2_storage(V_pore_high, 0.6, RHO_CO2)

labels = ['Low φ (-10%)', 'Base case', 'High φ (+10%)']
x = np.arange(len(labels))

fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()

bars_heat = ax1.bar(
    x - width/2,
    [heat_low, heat_base, heat_high],
    width,
    color='#E74C3C',
    edgecolor='black',
    alpha=0.85,
    label='Heat Storage (MJ)'
)

bars_co2 = ax2.bar(
    x + width/2,
    [co2_low, co2_base, co2_high],
    width,
    color='#27AE60',
    edgecolor='black',
    alpha=0.85,
    label='CO₂ Storage (tonnes)'
)

ax1.set_ylabel('Heat Storage (MJ)', color='#C0392B')
ax2.set_ylabel('CO₂ Storage (tonnes)', color='#1E8449')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
plt.title('Sensitivity Analysis: Effect of Porosity on Heat & CO₂ Storage')
ax1.grid(axis='y', linestyle='--', alpha=0.4)

# ----- Value labels -----
def add_labels(bars, axis, scale=1):
    for bar in bars:
        h = bar.get_height()
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            h,
            f'{h/scale:,.1f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

add_labels(bars_heat, ax1, scale=1e6)  # MJ → million MJ
add_labels(bars_co2, ax2)

# Combined legend
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc='upper left')

fig.tight_layout()
plt.show()










