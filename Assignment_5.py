def heat_exchanger_ntu(m_dot_h, cp_h, T_hi, m_dot_c, cp_c, T_ci, UA):
    """
    Calculates thermal duty and outlet temperatures using effectiveness-NTU method.
    """
    C_h = m_dot_h * cp_h
    C_c = m_dot_c * cp_c
    
    C_min = min(C_h, C_c)
    C_max = max(C_h, C_c)
    C_r = C_min / C_max
    
    NTU = UA / C_min
    
    # Counter-flow effectiveness equation
    if C_r < 1.0:
        eff = (1 - np.exp(-NTU * (1 - C_r))) / (1 - C_r * np.exp(-NTU * (1 - C_r)))
    else:
        eff = NTU / (1 + NTU)
        
    Q_max = C_min * (T_hi - T_ci)
    Q_actual = eff * Q_max
    
    T_ho = T_hi - (Q_actual / C_h)
    T_co = T_ci + (Q_actual / C_c)
    
    return eff, NTU, Q_actual / 1000.0, T_ho, T_co

# --- Assignment 5 Demo ---
if __name__ == "__main__":
    eff, ntu, Q_kW, T_ho, T_co = heat_exchanger_ntu(
        m_dot_h=1.2, cp_h=4.18, T_hi=45.0, m_dot_c=2.0, cp_c=1.006, T_ci=15.0, UA=2500.0
    )
    print("Assignment 5 Results:")
    print(f"NTU: {ntu:.3f} | Effectiveness: {eff*100:.1f}% | Heat Duty: {Q_kW:.2f} kW")