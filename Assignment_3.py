def cooling_coil_analysis(Q_sensible_kW, Q_latent_kW, T_room, w_room, BF=0.1):
    """
    Calculates supply air parameters and required coil apparatus dew point (ADP).
    """
    c_p_air = 1.006  # kJ/kg K
    h_fg = 2501.0    # kJ/kg
    
    # Sensible Heat Ratio
    SHR = Q_sensible_kW / (Q_sensible_kW + Q_latent_kW)
    
    # Supply air delta T assumption (e.g., 10°C below room temperature)
    dT_supply = 10.0
    T_supply = T_room - dT_supply
    
    # Required mass flow rate of dry air
    m_dot_da = Q_sensible_kW / (c_p_air * dT_supply)  # kg/s
    
    # Supply air humidity ratio
    w_supply = w_room - (Q_latent_kW / (m_dot_da * h_fg))
    
    # ADP estimation considering coil Bypass Factor (BF)
    # T_supply = T_ADP + BF * (T_on_coil - T_ADP)
    T_ADP = (T_supply - BF * T_room) / (1.0 - BF)
    
    return SHR, m_dot_da, T_supply, w_supply, T_ADP

# --- Assignment 3 Demo ---
if __name__ == "__main__":
    shr, m_dot, T_sup, w_sup, ADP = cooling_coil_analysis(Q_sensible_kW=20.0, Q_latent_kW=5.0, T_room=24.0, w_room=0.0095)
    print("Assignment 3 Results:")
    print(f"SHR: {shr:.2f} | Airflow: {m_dot:.3f} kg/s | Supply Temp: {T_sup:.1f} °C | Coil ADP: {ADP:.2f} °C")