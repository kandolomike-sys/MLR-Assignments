def vapour_compression_analysis(h1, h2, h3, h4, mass_flow_rate_kg_s, clearance_vol_ratio=0.05, v_inlet=0.035, v_outlet=0.010):
    """
    Analyzes thermodynamic cycle performance and compressor volumetric efficiency.
    h1: Evaporator exit enthalpy [kJ/kg]
    h2: Compressor exit enthalpy [kJ/kg]
    h3: Condenser exit enthalpy  [kJ/kg]
    h4: Expansion valve exit enthalpy [kJ/kg]
    """
    # Specific heat quantities
    q_evap = h1 - h4   # kJ/kg[cite: 284]
    w_comp = h2 - h1   # kJ/kg[cite: 284]
    
    # Capacity & Power
    Q_dot_cool_kW = mass_flow_rate_kg_s * q_evap[cite: 284]
    W_dot_comp_kW = mass_flow_rate_kg_s * w_comp[cite: 284]
    COP = Q_dot_cool_kW / W_dot_comp_kW if W_dot_comp_kW > 0 else 0[cite: 284]
    
    # Clearance Volumetric Efficiency calculation
    eta_vol = 1.0 - clearance_vol_ratio * ((v_inlet / v_outlet) - 1.0)[cite: 266]
    
    return COP, Q_dot_cool_kW, W_dot_comp_kW, eta_vol

# --- Assignment 9 Demo ---
if __name__ == "__main__":
    # Example state parameters for standard VCRS
    cop, Q_cool, W_comp, eta_v = vapour_compression_analysis(
        h1=400.0, h2=435.0, h3=250.0, h4=250.0, mass_flow_rate_kg_s=0.45
    )
    print("Assignment 9 Results:")
    print(f"COP: {cop:.2f} | Capacity: {Q_cool:.2f} kW | Power: {W_comp:.2f} kW")
    print(f"Compressor Volumetric Efficiency: {eta_v * 100:.1f}%")