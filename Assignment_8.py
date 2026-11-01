def thermal_storage_analysis(hourly_loads_kW, peak_hours_indices, max_chiller_cap_kW):
    """
    Calculates required storage energy (kWh) and off-peak charging schedule.
    """
    total_daily_energy_kWh = sum(hourly_loads_kW)[cite: 281]
    
    # Peak load energy requiring off-peak displacement
    peak_energy_demand_kWh = sum([hourly_loads_kW[i] for i in peak_hours_indices])[cite: 282]
    
    # Required TES capacity assuming chiller runs capped during peak hours
    tes_capacity_required_kWh = max(0.0, peak_energy_demand_kWh - len(peak_hours_indices) * max_chiller_cap_kW)[cite: 282]
    
    return total_daily_energy_kWh, tes_capacity_required_kWh

# --- Assignment 8 Demo ---
if __name__ == "__main__":
    loads = [40, 35, 35, 40, 50, 70, 90, 120, 150, 160, 150, 140, 130, 110, 80, 60, 50, 45, 40, 40, 40, 40, 40, 40]
    peak_hours = [7, 8, 9, 10, 11, 12, 13, 14]  # 8-hour peak window
    
    total_kWh, tes_kWh = thermal_storage_analysis(loads, peak_hours, max_chiller_cap_kW=80.0)
    print("Assignment 8 Results:")
    print(f"Total Daily Cooling Load: {total_kWh:.1f} kWh")
    print(f"Required TES Ice Capacity: {tes_kWh:.1f} kWh")