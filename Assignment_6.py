def cooling_tower_merkel(T_in, T_out, T_wb, L_G_ratio, c_w=4.184):
    """
    Calculates Cooling Tower Range, Approach, and Merkel NTU integral approximation.
    T_in : Inlet water temperature [°C]
    T_out: Outlet water temperature [°C]
    T_wb : Ambient wet-bulb temperature [°C]
    """
    Range = T_in - T_out[cite: 233]
    Approach = T_out - T_wb[cite: 233]
    
    # 4-point Chebyshev numerical integration for Merkel's integral
    T_pts = [T_out + 0.1*(T_in - T_out), T_out + 0.4*(T_in - T_out), 
             T_out + 0.6*(T_in - T_out), T_out + 0.9*(T_in - T_out)]
    
    # Simplified enthalpy difference evaluation
    dh_sum = 0
    for T in T_pts:
        h_sw = 1.006 * T + (0.622 * (0.61078 * np.exp((17.27 * T)/(T + 237.3))) / 95.0) * 2501.0
        h_a = 40.0 + (T - T_out) * L_G_ratio * c_w  # Approximate air enthalpy profile
        dh_sum += 1.0 / max(0.1, (h_sw - h_a))
        
    NTU = c_w * (T_in - T_out) * (dh_sum / 4.0)[cite: 228]
    
    return Range, Approach, NTU

# --- Assignment 6 Demo ---
if __name__ == "__main__":
    r, a, ntu = cooling_tower_merkel(T_in=36.0, T_out=29.0, T_wb=22.0, L_G_ratio=1.1)
    print("Assignment 6 Results:")
    print(f"Range: {r:.1f} °C | Approach: {a:.1f} °C | Calculated NTU: {ntu:.3f}")