def calculate_building_load(area_walls, U_wall, T_out, T_in, solar_radiation, SHGC, window_area, internal_gains_W):
    """
    Calculates sensible cooling load for a single zone.
    """
    # Conduction heat gain through walls/roofs
    Q_conduction = U_wall * area_walls * (T_out - T_in)
    
    # Solar heat gain through fenestration
    Q_solar = window_area * solar_radiation * SHGC
    
    # Total Sensible Load
    Q_total_W = Q_conduction + Q_solar + internal_gains_W
    Q_total_kW = Q_total_W / 1000.0
    
    return Q_conduction / 1000.0, Q_solar / 1000.0, Q_total_kW

# --- Assignment 2 Demo ---
if __name__ == "__main__":
    Q_cond, Q_sol, Q_tot = calculate_building_load(
        area_walls=120, U_wall=0.45, T_out=35.0, T_in=24.0,
        solar_radiation=600, SHGC=0.7, window_area=15, internal_gains_W=1200
    )
    print("Assignment 2 Results:")
    print(f"Conduction Gain: {Q_cond:.2f} kW | Solar Gain: {Q_sol:.2f} kW | Total Load: {Q_tot:.2f} kW")