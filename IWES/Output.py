import matplotlib.pyplot as plt
import numpy as np
from Variable_Parameter import Total_Energy_Consumption_for_Diesel, Travelling_Time, CO2_FACTORS, FUEL_DENSITIES, Total_Energy_Consumption_for_Diesel_3, Travelling_Time_3, Total_Energy_Consumption_for_Diesel_2, Working_time_per_day, Decomissioning_wind_turbine_days, No_of_Wind_turbine, Energy_content

"Case 1: Co2 Emission from port to site"


# Extract required constants
survey_vessel_fuel_consumption = Total_Energy_Consumption_for_Diesel["Survey_Vessel"]
SPIVs_Vessel_fuel_consumption = Total_Energy_Consumption_for_Diesel["SPIVs_Vessel"]
Dive_Support_Vessel_fuel_consumption = Total_Energy_Consumption_for_Diesel[
    "Dive_Support_Vessel"]
Crew_boat_Vessel_fuel_consumption = Total_Energy_Consumption_for_Diesel["Crew_boat_Vessel"]
Work_boat_Vessel_fuel_consumption = Total_Energy_Consumption_for_Diesel["Work_boat_Vessel"]
Multicats_Vessel_fuel_consumption = Total_Energy_Consumption_for_Diesel["Multicats_Vessel"]
Cargo_Vessel_fuel_consumption = Total_Energy_Consumption_for_Diesel["Cargo_Vessel"]
Tugs_Vessel_fuel_consumption = Total_Energy_Consumption_for_Diesel["Tugs_Vessel"]


methanol_density = FUEL_DENSITIES["Methanol"]
diesel_density = FUEL_DENSITIES["Diesel"]
MGO_density = FUEL_DENSITIES["MGO"]
LNG_density = FUEL_DENSITIES["LNG"]
HFO_density = FUEL_DENSITIES["HFO"]
ammonia_density = FUEL_DENSITIES["Ammonia"]


methanol_co2_factor = CO2_FACTORS["Methanol"]
diesel_co2_factor = CO2_FACTORS["Diesel"]
MGO_co2_factor = CO2_FACTORS["MGO"]
LNG_co2_factor = CO2_FACTORS["LNG"]
HFO_co2_factor = CO2_FACTORS["HFO"]
ammonia_co2_factor = CO2_FACTORS["Ammonia"]

methanol_EC = Energy_content["Methanol"]
diesel_EC = Energy_content["Diesel"]
MGO_EC = Energy_content["MGO"]
LNG_EC = Energy_content["LNG"]
HFO_EC = Energy_content["HFO"]
ammonia_EC = Energy_content["Ammonia"]

# Calculate CO2 emission
co2_emission_survey_vessel = (
    ((survey_vessel_fuel_consumption/LNG_EC) * Travelling_Time) * methanol_density * methanol_co2_factor) / 1000

co2_emission_SPIVs_vessel = (
    ((SPIVs_Vessel_fuel_consumption/LNG_EC) * Travelling_Time) * methanol_density * methanol_co2_factor) / 1000

co2_emission_Dive_vessel = (
    ((Dive_Support_Vessel_fuel_consumption/ammonia_EC) * Travelling_Time) * ammonia_density * ammonia_co2_factor) / 1000

co2_emission_Crew_boat_vessel = (
    ((Crew_boat_Vessel_fuel_consumption/LNG_EC) * Travelling_Time) * methanol_density * methanol_co2_factor) / 1000

co2_emission_work_boat_vessel = (
    ((Work_boat_Vessel_fuel_consumption/LNG_EC) * Travelling_Time) * methanol_density * methanol_co2_factor) / 1000

co2_emission_multicats_vessel = (
    ((Multicats_Vessel_fuel_consumption/ammonia_EC) * Travelling_Time) * ammonia_density * ammonia_co2_factor) / 1000

co2_emission_tugs_vessel = (
    ((Tugs_Vessel_fuel_consumption/ammonia_EC) * Travelling_Time) * ammonia_density * ammonia_co2_factor) / 1000

co2_emission_cargo_vessel = (
    ((Cargo_Vessel_fuel_consumption/ammonia_EC) * Travelling_Time) * ammonia_density * ammonia_co2_factor) / 1000

# Total Emission in Case 1
Total_Co2_emission_in_case_1 = co2_emission_survey_vessel + co2_emission_SPIVs_vessel + co2_emission_Dive_vessel + co2_emission_Crew_boat_vessel + \
    co2_emission_work_boat_vessel + co2_emission_multicats_vessel + \
    co2_emission_tugs_vessel + co2_emission_cargo_vessel

# Print the result
print(
    f"CASE 1: Co2 Emission\n"
    f"CO2 Emission of Survey Vessel: {co2_emission_survey_vessel:.4f} kg CO2\n"
    f"CO2 Emission of SPIVs Vessel: {co2_emission_SPIVs_vessel:.4f} kg CO2\n"
    f"CO2 Emission of Dive Vessel: {co2_emission_Dive_vessel:.4f} kg CO2\n"
    f"CO2 Emission of Crew boat Vessel: {co2_emission_Crew_boat_vessel:.4f} kg CO2\n"
    f"CO2 Emission of work boat Vessel: {co2_emission_work_boat_vessel:.4f} kg CO2\n"
    f"CO2 Emission of multicats Vessel: {co2_emission_multicats_vessel:.4f} kg CO2\n"
    f"CO2 Emission of tugs Vessel: {co2_emission_tugs_vessel:.4f} kg CO2\n"
    f"CO2 Emission of cargo Vessel: {co2_emission_cargo_vessel:.4f} kg CO2\n"
    f"Total CO2 Emission in Case 1 : {Total_Co2_emission_in_case_1:.4f} kg CO2\n"
)


"Case 3: Co2 Emission from site to port"


# Extract required constants
survey_vessel_fuel_consumption_3 = Total_Energy_Consumption_for_Diesel_3["Survey_Vessel"]
SPIVs_Vessel_fuel_consumption_3 = Total_Energy_Consumption_for_Diesel_3["SPIVs_Vessel"]
Dive_Support_Vessel_fuel_consumption_3 = Total_Energy_Consumption_for_Diesel_3[
    "Dive_Support_Vessel"]
Crew_boat_Vessel_fuel_consumption_3 = Total_Energy_Consumption_for_Diesel_3[
    "Crew_boat_Vessel"]
Work_boat_Vessel_fuel_consumption_3 = Total_Energy_Consumption_for_Diesel_3[
    "Work_boat_Vessel"]
Multicats_Vessel_fuel_consumption_3 = Total_Energy_Consumption_for_Diesel_3[
    "Multicats_Vessel"]
Cargo_Vessel_fuel_consumption_3 = Total_Energy_Consumption_for_Diesel_3["Cargo_Vessel"]
Tugs_Vessel_fuel_consumption_3 = Total_Energy_Consumption_for_Diesel_3["Tugs_Vessel"]


# Calculate CO2 emission
co2_emission_survey_vessel_3 = (
    ((survey_vessel_fuel_consumption_3/LNG_EC) * Travelling_Time_3) * methanol_density * methanol_co2_factor) / 1000

co2_emission_SPIVs_vessel_3 = (
    ((SPIVs_Vessel_fuel_consumption_3/LNG_EC) * Travelling_Time_3) * methanol_density * methanol_co2_factor) / 1000

co2_emission_Dive_vessel_3 = (
    ((Dive_Support_Vessel_fuel_consumption_3/ammonia_EC) * Travelling_Time_3) * ammonia_density * ammonia_co2_factor) / 1000

co2_emission_Crew_boat_vessel_3 = (
    ((Crew_boat_Vessel_fuel_consumption_3/LNG_EC) * Travelling_Time_3) * methanol_density * methanol_co2_factor) / 1000

co2_emission_work_boat_vessel_3 = (
    ((Work_boat_Vessel_fuel_consumption_3/LNG_EC) * Travelling_Time_3) * methanol_density * methanol_co2_factor) / 1000

co2_emission_multicats_vessel_3 = (
    ((Multicats_Vessel_fuel_consumption_3/ammonia_EC) * Travelling_Time_3) * ammonia_density * ammonia_co2_factor) / 1000

co2_emission_tugs_vessel_3 = (
    ((Tugs_Vessel_fuel_consumption_3/ammonia_EC) * Travelling_Time_3) * ammonia_density * ammonia_co2_factor) / 1000

co2_emission_cargo_vessel_3 = (
    ((Cargo_Vessel_fuel_consumption_3/ammonia_EC) * Travelling_Time_3) * ammonia_density * ammonia_co2_factor) / 1000

# Total Emission in Case 1
Total_Co2_emission_in_case_3 = co2_emission_survey_vessel_3 + co2_emission_SPIVs_vessel_3 + co2_emission_Dive_vessel_3 + co2_emission_Crew_boat_vessel_3 + \
    co2_emission_work_boat_vessel_3 + co2_emission_multicats_vessel_3 + \
    co2_emission_tugs_vessel_3 + co2_emission_cargo_vessel_3

# Print the result
print(
    f"Case 3: Co2 Emission\n"
    f"CO2 Emission of Survey Vessel: {co2_emission_survey_vessel_3:.4f} kg CO2\n"
    f"CO2 Emission of SPIVs Vessel: {co2_emission_SPIVs_vessel_3:.4f} kg CO2\n"
    f"CO2 Emission of Dive Vessel: {co2_emission_Dive_vessel_3:.4f} kg CO2\n"
    f"CO2 Emission of Crew boat Vessel: {co2_emission_Crew_boat_vessel_3:.4f} kg CO2\n"
    f"CO2 Emission of work boat Vessel: {co2_emission_work_boat_vessel_3:.4f} kg CO2\n"
    f"CO2 Emission of multicats Vessel: {co2_emission_multicats_vessel_3:.4f} kg CO2\n"
    f"CO2 Emission of tugs Vessel: {co2_emission_tugs_vessel_3:.4f} kg CO2\n"
    f"CO2 Emission of cargo Vessel: {co2_emission_cargo_vessel_3:.4f} kg CO2\n"
    f"Total CO2 Emission in Case 3 : {Total_Co2_emission_in_case_3:.4f} kg CO2\n"
)


"Case 2: Co2 Emission on Site"


# Extract required constants
survey_vessel_fuel_consumption_2 = Total_Energy_Consumption_for_Diesel_2["Survey_Vessel"]
SPIVs_Vessel_fuel_consumption_2 = Total_Energy_Consumption_for_Diesel_2["SPIVs_Vessel"]
Dive_Support_Vessel_fuel_consumption_2 = Total_Energy_Consumption_for_Diesel_2[
    "Dive_Support_Vessel"]
Crew_boat_Vessel_fuel_consumption_2 = Total_Energy_Consumption_for_Diesel_2[
    "Crew_boat_Vessel"]
Work_boat_Vessel_fuel_consumption_2 = Total_Energy_Consumption_for_Diesel_2[
    "Work_boat_Vessel"]
Multicats_Vessel_fuel_consumption_2 = Total_Energy_Consumption_for_Diesel_2[
    "Multicats_Vessel"]
Cargo_Vessel_fuel_consumption_2 = Total_Energy_Consumption_for_Diesel_2["Cargo_Vessel"]
Tugs_Vessel_fuel_consumption_2 = Total_Energy_Consumption_for_Diesel_2["Tugs_Vessel"]


# EWorking time per day vessel
survey_vessel_working_time_2 = Working_time_per_day["Survey_Vessel"]
SPIVs_Vessel_working_time_2 = Working_time_per_day["SPIVs_Vessel"]
Dive_Support_Vessel_working_time_2 = Working_time_per_day["Dive_Support_Vessel"]
Crew_boat_Vessel_working_time_2 = Working_time_per_day["Crew_boat_Vessel"]
Work_boat_Vessel_working_time_2 = Working_time_per_day["Work_boat_Vessel"]
Multicats_Vessel_working_time_2 = Working_time_per_day["Multicats_Vessel"]
Cargo_Vessel_working_time_2 = Working_time_per_day["Cargo_Vessel"]
Tugs_Vessel_working_time_2 = Working_time_per_day["Tugs_Vessel"]

# Calculate CO2 emission
co2_emission_survey_vessel_2 = ((survey_vessel_fuel_consumption_2/LNG_EC) * methanol_density * survey_vessel_working_time_2 *
                                Decomissioning_wind_turbine_days * No_of_Wind_turbine*methanol_co2_factor) / 1000

co2_emission_SPIVs_vessel_2 = ((SPIVs_Vessel_fuel_consumption_2/LNG_EC) * methanol_density * SPIVs_Vessel_working_time_2 *
                               Decomissioning_wind_turbine_days * No_of_Wind_turbine*methanol_co2_factor) / 1000

co2_emission_Dive_vessel_2 = ((Dive_Support_Vessel_fuel_consumption_2/ammonia_EC) * ammonia_density * Dive_Support_Vessel_working_time_2 *
                              Decomissioning_wind_turbine_days * No_of_Wind_turbine*ammonia_co2_factor) / 1000

co2_emission_Crew_boat_vessel_2 = ((Crew_boat_Vessel_fuel_consumption_2/LNG_EC) * methanol_density * Dive_Support_Vessel_working_time_2 *
                                   Decomissioning_wind_turbine_days * No_of_Wind_turbine*methanol_co2_factor) / 1000

co2_emission_work_boat_vessel_2 = ((Work_boat_Vessel_fuel_consumption_2/LNG_EC) * methanol_density * Work_boat_Vessel_working_time_2 *
                                   Decomissioning_wind_turbine_days * No_of_Wind_turbine*methanol_co2_factor) / 1000

co2_emission_multicats_vessel_2 = ((Multicats_Vessel_fuel_consumption_2/ammonia_EC) * ammonia_density * Multicats_Vessel_working_time_2 *
                                   Decomissioning_wind_turbine_days * No_of_Wind_turbine*ammonia_co2_factor) / 1000

co2_emission_tugs_vessel_2 = ((Tugs_Vessel_fuel_consumption_2/ammonia_EC) * ammonia_density * Tugs_Vessel_working_time_2 *
                              Decomissioning_wind_turbine_days * No_of_Wind_turbine*ammonia_co2_factor) / 1000

co2_emission_cargo_vessel_2 = ((Cargo_Vessel_fuel_consumption_2/ammonia_EC) * ammonia_density * Cargo_Vessel_working_time_2 *
                               Decomissioning_wind_turbine_days * No_of_Wind_turbine*ammonia_co2_factor) / 1000

# Total Emission in Case 2
Total_Co2_emission_in_case_2 = co2_emission_survey_vessel_2 + co2_emission_SPIVs_vessel_2 + co2_emission_Dive_vessel_2 + co2_emission_Crew_boat_vessel_2 + \
    co2_emission_work_boat_vessel_2 + co2_emission_multicats_vessel_2 + \
    co2_emission_tugs_vessel_2 + co2_emission_cargo_vessel_2

# Print the result
print(
    f"Case 2: Co2 Emission\n"
    f"CO2 Emission of Survey Vessel: {co2_emission_survey_vessel_2:.4f} kg CO2\n"
    f"CO2 Emission of SPIVs Vessel: {co2_emission_SPIVs_vessel_2:.4f} kg CO2\n"
    f"CO2 Emission of Dive Vessel: {co2_emission_Dive_vessel_2:.4f} kg CO2\n"
    f"CO2 Emission of Crew boat Vessel: {co2_emission_Crew_boat_vessel_2:.4f} kg CO2\n"
    f"CO2 Emission of work boat Vessel: {co2_emission_work_boat_vessel_2:.4f} kg CO2\n"
    f"CO2 Emission of multicats Vessel: {co2_emission_multicats_vessel_2:.4f} kg CO2\n"
    f"CO2 Emission of tugs Vessel: {co2_emission_tugs_vessel_2:.4f} kg CO2\n"
    f"CO2 Emission of cargo Vessel: {co2_emission_cargo_vessel_2:.4f} kg CO2\n"
    f"Total CO2 Emission in Case 2 : {Total_Co2_emission_in_case_2:.4f} kg CO2\n"
)


Total_Co2_Emission = Total_Co2_emission_in_case_1 + \
    Total_Co2_emission_in_case_2 + Total_Co2_emission_in_case_3

print(f"Total CO2 Emission: {Total_Co2_Emission:.4f} kg CO2\n")
print(f"Total CO2 Emission: {Total_Co2_Emission/1000:.4f} tonnes CO2\n")


# Data preparation
vessel_types = [
    "Survey Vessel [LNG]",
    "SPIVs Vessel [LNG]",
    "Dive Vessel [Ammonia]",
    "Crew Boat Vessel [LNG]",
    "Work Boat Vessel [LNG]",
    "Multicats Vessel [Ammonia]",
    "Tugs Vessel [Ammonia]",
    "Cargo Vessel [Ammonia]"
]

# Convert CO2 emissions to tonnes
case_1_emissions = [
    co2_emission_survey_vessel / 1000,
    co2_emission_SPIVs_vessel / 1000,
    co2_emission_Dive_vessel / 1000,
    co2_emission_Crew_boat_vessel / 1000,
    co2_emission_work_boat_vessel / 1000,
    co2_emission_multicats_vessel / 1000,
    co2_emission_tugs_vessel / 1000,
    co2_emission_cargo_vessel / 1000,
]

case_2_emissions = [
    co2_emission_survey_vessel_2 / 1000,
    co2_emission_SPIVs_vessel_2 / 1000,
    co2_emission_Dive_vessel_2 / 1000,
    co2_emission_Crew_boat_vessel_2 / 1000,
    co2_emission_work_boat_vessel_2 / 1000,
    co2_emission_multicats_vessel_2 / 1000,
    co2_emission_tugs_vessel_2 / 1000,
    co2_emission_cargo_vessel_2 / 1000,
]

case_3_emissions = [
    co2_emission_survey_vessel_3 / 1000,
    co2_emission_SPIVs_vessel_3 / 1000,
    co2_emission_Dive_vessel_3 / 1000,
    co2_emission_Crew_boat_vessel_3 / 1000,
    co2_emission_work_boat_vessel_3 / 1000,
    co2_emission_multicats_vessel_3 / 1000,
    co2_emission_tugs_vessel_3 / 1000,
    co2_emission_cargo_vessel_3 / 1000,
]

# Bar width and positions
x = np.arange(len(vessel_types))
bar_width = 0.30

# Plotting with logarithmic scale
plt.figure(figsize=(12, 6))
plt.bar(x - bar_width, case_1_emissions, width=bar_width, label="Port to site")
plt.bar(x, case_2_emissions, width=bar_width, label="On site")
plt.bar(x + bar_width, case_3_emissions, width=bar_width, label="site to port")
plt.yscale('log')

# Customizations
plt.xlabel("Vessel Types")
plt.ylabel("CO2 Emissions (per tonnes)")
plt.title("CO2 Emissions per Vessel for different case")
plt.xticks(x, vessel_types, rotation=45)
plt.legend()
plt.tight_layout()

# Display the plot
plt.show()
