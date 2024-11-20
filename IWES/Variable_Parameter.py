"Calculate total Co2 Emission"

""""""""
"Case 1: Port to Site"
""""""""

Total_Energy_Consumption_for_Diesel = {
    "Survey_Vessel": 250 * 10,         # [kwh]
    "SPIVs_Vessel": 250 * 10,
    "Dive_Support_Vessel": 400 * 10,
    "Crew_boat_Vessel": 150 * 10,
    "Work_boat_Vessel": 300 * 10,
    "Multicats_Vessel": 400 * 10,
    "Tugs_Vessel": 400 * 10,
    "Cargo_Vessel": 700 * 10
}

Travelling_Time = 4.0  # [3.63 + 0.37 for safe side]  [Distance/speed]

"Co2 Emission Factor [gCO2/g Fuel]"
CO2_FACTORS = {
    "HFO": 3.114,
    "Diesel": 3.206,
    "MGO": 3.206,
    "LNG": 2.750,
    "Methanol": 1.375,
    "Ammonia": 0,
    "Electricity": 0
}

" Fuel Densities [grams/litre]"

FUEL_DENSITIES = {
    "HFO": 950,
    "Diesel": 850,
    "MGO": 870,
    "LNG": 450,
    "Methanol": 790,
    "Ammonia": 682
}


" Energy Content [kWh/litres]"

Energy_content = {
    "HFO": 9.6,
    "Diesel": 10,
    "MGO": 9.8,
    "LNG": 9,
    "Methanol": 6,
    "Ammonia": 4.5
}


" Energy Cost [USD/kWh]"

Energy_cost = {
    "HFO": 0.043432836,
    "Diesel": 0.06618267,
    "MGO": 0.066,
    "LNG": 0.0423,
    "Methanol": 0.055175879,
    "Ammonia": 0.123870968
}

""""""""
"Case 3: Site to port"
""""""""

Total_Energy_Consumption_for_Diesel_3 = {
    "Survey_Vessel": 250 * 10,         # [litres/h]
    "SPIVs_Vessel": 300 * 10,          # [litres/h]
    "Dive_Support_Vessel": 400 * 10,   # [litres/h]
    "Crew_boat_Vessel": 150 * 10,      # [litres/h]
    "Work_boat_Vessel": 300 * 10,      # [litres/h]
    "Multicats_Vessel": 400 * 10,      # [litres/h]
    "Tugs_Vessel": 400 * 10,           # [litres/h]
    "Cargo_Vessel": 1000 * 10          # [litres/h]
}

Travelling_Time_3 = 4.5  # [3.63 + 0.37 for safe side] [Distance/speed]

""""""""
"Case 2: In Site"
""""""""

Total_Energy_Consumption_for_Diesel_2 = {
    "Survey_Vessel": 200 * 10,         # [litres/h]
    "SPIVs_Vessel": 200 * 10,          # [litres/h]
    "Dive_Support_Vessel": 300 * 10,   # [litres/h]
    "Crew_boat_Vessel": 100 * 10,      # [litres/h]
    "Work_boat_Vessel": 200 * 10,      # [litres/h]
    "Multicats_Vessel": 300 * 10,      # [litres/h]
    "Tugs_Vessel": 300 * 10,           # [litres/h]
    "Cargo_Vessel": 500 * 10         # [litres/h]
}

Working_time_per_day = {
    "Survey_Vessel": 12,         # [hours/day]
    "SPIVs_Vessel": 12,          # [hours/day]
    "Dive_Support_Vessel": 12,   # [hours/day]
    "Crew_boat_Vessel": 6,      # [hours/day]
    "Work_boat_Vessel": 12,      # [hours/day]
    "Multicats_Vessel": 9,      # [hours/day]
    "Tugs_Vessel": 9,           # [hours/day]
    "Cargo_Vessel": 9           # [hours/day]
}

# [days/wind turbine] 8MW wind turbine Assuming times
Decomissioning_wind_turbine_days = 15
No_of_Wind_turbine = 8
