def duct_design_equal_friction(Q_m3s, friction_loss_Pa_m=1.0, rho=1.2, f=0.018):
    """
    Calculates required duct diameter and actual air velocity for given pressure drop limit.
    """
    # Circular duct diameter formula derived from Darcy-Weisbach
    # Delta P / L = (f / D) * (rho * V^2 / 2), and V = 4*Q / (pi * D^2)
    D = ((8 * f * rho * Q_m3s**2) / (np.pi**2 * friction_loss_Pa_m)) ** (1.0 / 5.0)[cite: 239]
    Area = (np.pi / 4.0) * D**2
    Velocity = Q_m3s / Area
    
    return D, Velocity

def static_regain(V1, static_regain_factor=0.75, rho=1.2):
    """
    Calculates downstream velocity V2 needed to regain static pressure across a branch junction.
    """
    # Delta P_s = R * (rho / 2) * (V1^2 - V2^2)
    # Assuming full regain of fitting losses
    V2 = V1 * np.sqrt(1.0 - static_regain_factor)[cite: 247]
    return V2

# --- Assignment 7 Demo ---
if __name__ == "__main__":
    D_m, V = duct_design_equal_friction(Q_m3s=1.8, friction_loss_Pa_m=0.8)
    V_next = static_regain(V1=V)
    print("Assignment 7 Results:")
    print(f"Duct Diameter: {D_m * 1000:.1f} mm | Velocity: {V:.2f} m/s")
    print(f"Target Downstream Velocity (Static Regain): {V_next:.2f} m/s")