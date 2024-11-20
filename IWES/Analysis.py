import numpy as np
import matplotlib.pyplot as plt
from Variable_Parameter import CO2_FACTORS, Energy_content, Energy_cost, FUEL_DENSITIES


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

methanol_cost = Energy_cost["Methanol"]
diesel_cost = Energy_cost["Diesel"]
MGO_cost = Energy_cost["MGO"]
LNG_cost = Energy_cost["LNG"]
HFO_cost = Energy_cost["HFO"]
ammonia_cost = Energy_cost["Ammonia"]

methanol_density = FUEL_DENSITIES["Methanol"]
diesel_density = FUEL_DENSITIES["Diesel"]
MGO_density = FUEL_DENSITIES["MGO"]
LNG_density = FUEL_DENSITIES["LNG"]
HFO_density = FUEL_DENSITIES["HFO"]
ammonia_density = FUEL_DENSITIES["Ammonia"]


" Co2 Emission of different Fuel "


class FuelEfficiency:
    def __init__(self, Total_Energy_Consumption):
        self.Total_Energy_Consumption = Total_Energy_Consumption

    #  HFO
    def HFO(self):
        HFO_co2 = ((self.Total_Energy_Consumption/HFO_EC) * HFO_co2_factor *
                   HFO_density)/1000  # [kg co2]
        HFO_total_cost = (self.Total_Energy_Consumption/HFO_EC) * HFO_cost
        return HFO_co2, HFO_total_cost

    # diesel

    def diesel(self):
        diesel_co2 = ((self.Total_Energy_Consumption/diesel_EC) *
                      diesel_co2_factor * diesel_density)/1000
        diesel_total_cost = (
            self.Total_Energy_Consumption/diesel_EC) * diesel_cost
        return diesel_co2, diesel_total_cost

    #  MGO
    def MGO(self):
        MGO_co2 = ((self.Total_Energy_Consumption/MGO_EC)
                   * MGO_co2_factor * MGO_density)/1000
        MGO_total_cost = (self.Total_Energy_Consumption/MGO_EC) * MGO_cost
        return MGO_co2, MGO_total_cost

    # LNG
    def LNG(self):
        LNG_co2 = ((self.Total_Energy_Consumption/LNG_EC)
                   * LNG_co2_factor * LNG_density)/1000
        LNG_total_cost = (self.Total_Energy_Consumption/LNG_EC) * LNG_cost
        return LNG_co2, LNG_total_cost

    #  Methanol
    def methanol(self):
        methanol_co2 = ((self.Total_Energy_Consumption/methanol_EC) *
                        methanol_co2_factor * methanol_density)/1000
        methanol_total_cost = (
            self.Total_Energy_Consumption/methanol_EC) * methanol_cost
        return methanol_co2, methanol_total_cost

    # Ammonia
    def ammonia(self):
        ammonia_co2 = ((self.Total_Energy_Consumption/ammonia_EC) *
                       ammonia_co2_factor * ammonia_density)/1000
        ammonia_total_cost = (
            self.Total_Energy_Consumption/ammonia_EC) * ammonia_cost
        return ammonia_co2, ammonia_total_cost


# Example amounts of fuel in tons
Total_Energy_Consumption = 2000  # [kwh]  # Example value

# Initialize the TechnologyEfficiency object
efficiency = FuelEfficiency(Total_Energy_Consumption)

# Calculate CO2 emissions for different fuels
fuels = ['HFO', 'Diesel', 'MGO', 'LNG', 'Methanol', 'Ammonia']
emissions = [
    efficiency.HFO()[0],
    efficiency.diesel()[0],
    efficiency.MGO()[0],
    efficiency.LNG()[0],
    efficiency.methanol()[0],
    efficiency.ammonia()[0]
]

# Calculate CO2 emissions for different fuels
fuels = ['HFO', 'Diesel', 'MGO', 'LNG', 'Methanol', 'Ammonia']
Cost_USD = [
    efficiency.HFO()[1],
    efficiency.diesel()[1],
    efficiency.MGO()[1],
    efficiency.LNG()[1],
    efficiency.methanol()[1],
    efficiency.ammonia()[1]
]

# Graph (Fueltype Vs Co2)
plt.figure(figsize=(10, 6))
plt.plot(fuels, emissions, marker='o', color='r', label='CO2 Emissions')
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('CO2 Emissions [kg co2]', fontsize=12)
plt.title(
    f'CO2 Emissions for {Total_Energy_Consumption} [kwh] energy consumption', fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

# Graph (Fuel type Vs cost)
plt.figure(figsize=(10, 6))
plt.plot(fuels, Cost_USD, marker='o', color='b', label='Cost [USD]')
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Cost [USD]', fontsize=12)
plt.title(
    f'Cost [USD] for {Total_Energy_Consumption} [kwh] energy consumption', fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()
