python
import pandas as pd
import json

# Load datasets
transport_data = pd.read_csv('Public_Transport_Ridership_Data.csv')
energy_data = pd.read_json('Renewable_Energy_Production_Data.json')
healthcare_data = pd.read_excel('Healthcare_Facility_Utilization_Data.xlsx')

# Example analysis: Calculate peak usage times for public transport
peak_usage = transport_data.groupby(['Hour']).agg({'Ridership': 'sum'}).sort_values(by='Ridership', ascending=False)

# Example analysis: Calculate total renewable energy production
total_energy_production = energy_data['Production'].sum()

# Example analysis: Calculate average bed occupancy rate in healthcare facilities
average_bed_occupancy = healthcare_data['Bed Occupancy Rate'].mean()

# Output the results
print(f'Peak Transport Usage Times:\n{peak_usage.head()}')
print(f'Total Renewable Energy Production: {total_energy_production} MWh')
print(f'Average Bed Occupancy Rate: {average_bed_occupancy}%')
