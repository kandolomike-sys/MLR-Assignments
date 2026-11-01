import numpy as np

def psychrometric_properties(T_db, phi, P_atm=101.325):
    """
    Calculates psychrometric properties of moist air.
    T_db : Dry-bulb temperature [°C]
    phi  : Relative humidity [0.0 to 1.0]
    P_atm: Atmospheric pressure [kPa]
    """
    # Saturation pressure (Tetens / Antoine approximation) [kPa]
    P_sat = 0.61078 * np.exp((17.27 * T_db) / (T_db + 237.3))
    
    # Partial pressure of water vapor
    P_v = phi * P_sat
    
    # Specific humidity (humidity ratio) [kg w / kg da]
    w = 0.622 * (P_v / (P_atm - P_v))
    
    # Specific enthalpy [kJ/kg da]
    h = 1.006 * T_db + w * (2501 + 1.86 * T_db)
    
    # Dew point temperature [°C]
    alpha = np.log(P_v / 0.61078)
    T_dp = (237.3 * alpha) / (17.27 - alpha)
    
    return {'P_sat_kPa': P_sat, 'w_kg_kg': w, 'h_kJ_kg': h, 'T_dp_C': T_dp}

def adiabatic_mixing(m_dot1, T1, w1, m_dot2, T2, w2):
    """Calculates mixed airstream conditions for two combined flows."""
    m_dot_total = m_dot1 + m_dot2
    w_mix = (m_dot1 * w1 + m_dot2 * w2) / m_dot_total
    T_mix = (m_dot1 * T1 + m_dot2 * T2) / m_dot_total
    return T_mix, w_mix

# --- Assignment 1 Demo ---
if __name__ == "__main__":
    props = psychrometric_properties(T_db=25.0, phi=0.50)
    print("Assignment 1 Results:")
    print(f"Humidity Ratio: {props['w_kg_kg']:.5f} kg/kg da")
    print(f"Specific Enthalpy: {props['h_kJ_kg']:.2f} kJ/kg")
    print(f"Dew Point: {props['T_dp_C']:.2f} °C")