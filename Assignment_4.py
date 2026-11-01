def fan_laws(N1, Q1, P1, W1, N2):
    """
    Applies fan affinity laws for speed changes (N1 -> N2).
    """
    # Flow rate proportional to speed
    Q2 = Q1 * (N2 / N1)
    # Static pressure proportional to speed squared
    P2 = P1 * (N2 / N1)**2
    # Shaft power proportional to speed cubed
    W2 = W1 * (N2 / N1)**3
    
    return Q2, P2, W2

# --- Assignment 4 Demo ---
if __name__ == "__main__":
    Q2, P2, W2 = fan_laws(N1=1450, Q1=3.5, P1=450, W1=2.2, N2=1150)
    print("Assignment 4 Results:")
    print(f"New Airflow: {Q2:.2f} m^3/s | New Pressure: {P2:.1f} Pa | New Power: {W2:.2f} kW")