# GENERAL INFO FOR EMISSIONS

EMISSION_TYPE = [('Car fuels', 'Car fuels',),
                 ('SF6', 'SF6'),
                 ('Refrigerants', 'Refrigerants',),
                 ('Natural gas', 'Natural gas',),
                 ('Energy Acquisition', 'Energy Acquisition'),
                 ('Business Travel', 'Business Travel'),
                 ('Waste Generated in Operations', 'Waste Generated in Operations'),
                 ('Purchased Goods and Services','Purchased Goods and Services'),
                 ('Capital Goods','Capital Goods'),
                 ('Fuel and Energy Related Activities','Fuel and Energy Related Activities'),
                 ('Upstream Transportation and Distribution','Upstream Transportation and Distribution'),
                 ('Employee Commuting','Employee Commuting'),
                 ('Upstream Leased Assets','Upstream Leased Assets'),
                 ('Downstream Transportation and Distribution','Downstream Transportation and Distribution'),
                 ('Processing of Sold Products','Processing of Sold Products'),
                 ('Use of Sold Products','Use of Sold Products'),
                 ('End of Life Treatment of Sold Products','End of Life Treatment of Sold Products'),
                 ('Downstream Leased Assets','Downstream Leased Assets'),
                 ('Franchises','Franchises'),
                 ('Investments','Investments')]

EMISSION_SCOPE = [('Scope 1', 'Scope 1'),
                  ('Scope 2', 'Scope 2'),
                  ('Scope 3', 'Scope 3')]

# FUEL EMISSIONS CONSTANTS
FUEL_TYPE = [('Diesel Fuel', 'Diesel '),
             ('Gasoline Fuel', 'Gasoline '),
             ('Biodiesel (100%) Fuel', 'Biodiesel'),
             ('Motor Gasoline Fuel', 'Motor Gasoline '),
             ('Ethanol (100%) Fuel', 'Ethanol '),
             ('Jet Fuel', 'Jet Fuel'),
             ('Aviation Fuel', 'Aviation Fuel'),
             ('Compressed Natural Gas', 'Compressed Natural Gas')]

ACTIVITY_TYPE = [('Fuel use', 'Fuel use'),
                 ('Distance Activity', 'Distance Activity'),
                 ('Custom emission factor', 'Custom emission factor')]

VEHICLE_TYPE = [('Diesel passenger cars', 'Diesel passenger cars'),
                ('Diesel light-duty trucks', 'Diesel light-duty'),
                ('Diesel medium-and-heavy-trucks', 'Diesel medium-and-heavy-trucks'),
                ('Diesel agricultural equipment', 'Diesel agricultural equipment'),
                ('Diesel ships and boats', 'Diesel ships and boats'),
                ('Diesel medium-and-heavy-duty-Vehicles', 'Diesel-medium-and-heavy-Vehicles'),
                ('Other diesel Non-Road Vehicles', 'Other diesel Non-Road Vehicles'),
                ('Gasoline passenger cars', 'Gasoline passenger cars'),
                ('Gasoline light-duty trucks', 'Gasoline light-duty'),
                ('Gasoline medium-and-heavy-trucks', 'Gasoline medium-and-heavy-trucks'),
                ('Gasoline agricultural equipment', 'Gasoline agricultural equipment'),
                ('Gasoline ships and boats', 'Gasoline ships and boats'),
                ('Gasoline medium-and-heavy-duty-Vehicles', 'Gasoline-medium-and-heavy-Vehicles'),
                ('Other gasoline Non-Road Vehicles', 'Other gasoline Non-Road Vehicles'),

                ]

POLLUTION_NORM = [('Euro 1', 'Euro 1'),
                  ('Euro 2', 'Euro 2'),
                  ('Euro 3', 'Euro 3'),
                  ('Euro 4', 'Euro 4'),
                  ('Euro 5', 'Euro 5'),
                  ('Euro 6', 'Euro 6')]

# ENERGY EMISSIONS CONSTANTS

ENERGY_LOCATIONS = [('Location 1', 'Location 1'),
                    ('Location 2', 'Location 2'),
                    ('Location 3', 'Location 3'),
                    ('Location 4', 'Location 4'),
                    ('Location 5', 'Location 5')]

NATURAL_GAS_LOCATIONS = [('Location 1', 'Location 1'),
                         ('Location 2', 'Location 2'),
                         ('Location 3', 'Location 3'),
                         ('Location 4', 'Location 4'),
                         ('Location 5', 'Location 5')]

CALCULATION_METHOD = [('Location Based', 'Location Based'),
                      ('Market Based', 'Market Based')]


CALCULATION_METHOD_FOR_SCOPE_3= [('Supplier specific method','Supplier specific method'),
                                 ('Hybrid method','Hybrid method'),
                                 ('Average data method','Average data method'),
                                 ('Spend  based method','Spend based method'),
                                 ('Waste type specific method','Waste type specific method'),
                                 ]


MONTH = [('January', 'January'),
         ('February', 'February'),
         ('March', 'March'),
         ('April', 'April'),
         ('May', 'May'),
         ('June', 'June'),
         ('July', 'July'),
         ('August', 'August'),
         ('September', 'September'),
         ('October', 'October'),
         ('November', 'November'),
         ('December', 'December')]

TAXONOMY_SECTOR_CHOICES = [('Construction and real estate activities', 'Construction and real estate activities'),
                           ('Energy', 'Energy'),
                           ('Environmental protection and restoration activities',
                            'Environmental protection and restoration activities'),
                           ('Forestry', 'Forestry'),
                           ('Information and communication', 'Information and communication'),
                           ('Manufacturing', 'Manufacturing'),
                           ('Professional, scientific and technical activities','Professional, scientific and technical activities'),
                           ('Transport','Transport'),
                           ('Water supply, sewerage, waste management and remediation','Water supply, sewerage, waste management and remediation')
                           ]

TAXONOMY_ACTIVITY_CHOICES = [
    ('Acquisition and ownership of buildings', 'Acquisition and ownership of buildings'),
    ('Construction of new buildings','Construction of new buildings'),
    ('Installation, maintenance and repair of charging stations for electric vehicles in buildings (and parking spaces attached to buildings)',
     'Installation, maintenance and repair of charging stations for electric vehicles in buildings (and parking spaces attached to buildings)'),
    ('Installation, maintenance and repair of energy efficiency equipment','Installation, maintenance and repair of energy efficiency equipment'),
    ('Installation, maintenance and repair of instruments and devices for measuring, regulation and controlling energy performance of buildings',
     'Installation, maintenance and repair of instruments and devices for measuring, regulation and controlling energy performance of buildings'),
    ('Installation, maintenance and repair of renewable energy technologies', 'Installation, maintenance and repair of renewable energy technologies'),
    ('Renovation of existing buildings', 'Renovation of existing buildings'),
    ('Cogeneration of heat/cool and power from bioenergy', 'Cogeneration of heat/cool and power from bioenergy'),
    ('Cogeneration of heat/cool and power from geothermal energy', 'Cogeneration of heat/cool and power from geothermal energy'),
    ('Cogeneration of heat/cool and power from renewable non-fossil gaseous and liquid fuels',
     'Cogeneration of heat/cool and power from renewable non-fossil gaseous and liquid fuels'),
    ('Cogeneration of heat/cool and power from solar energy', 'Cogeneration of heat/cool and power from solar energy'),
    ('Construction and safe operation of new nuclear power plants, for the generation of electricity and/or heat, including for hydrogen production, using best-available technologies',
     'Construction and safe operation of new nuclear power plants, for the generation of electricity and/or heat, including for hydrogen production, using best-available technologies'),
    ('District heating/cooling distribution', 'District heating/cooling distribution'),
    ('Electricity generation from bioenergy', 'Electricity generation from bioenergy'),
    ('Electricity generation from fossil gaseous fuels', 'Electricity generation from fossil gaseous fuels'),
    ('Electricity generation from geothermal energy', 'Electricity generation from geothermal energy'),
    ('Electricity generation from geothermal energy', 'Electricity generation from geothermal energy'),
    ('Electricity generation from hydropower', 'Electricity generation from hydropower'),
    ('Electricity generation from nuclear energy in existing installations', 'Electricity generation from nuclear energy in existing installations'),
    ('Electricity generation from ocean energy technologies', 'Electricity generation from ocean energy technologies'),
    ('Electricity generation from renewable non-fossil gaseous and liquid fuels', 'Electricity generation from renewable non-fossil gaseous and liquid fuels'),
    ('Electricity generation from wind power', 'Electricity generation from wind power'),
    ('Electricity generation using concentrated solar power (CSP) technology', 'Electricity generation using concentrated solar power (CSP) technology'),
    ('Electricity generation using solar photovoltaic technology', 'Electricity generation using solar photovoltaic technology'),
    ('High-efficiency co-generation of heat/cool and power from fossil gaseous fuels', 'High-efficiency co-generation of heat/cool and power from fossil gaseous fuels'),
    ('Installation and operation of electric heat pumps', 'Installation and operation of electric heat pumps'),
    ('Manufacture of biogas and biofuels for use in transport and of bioliquids', 'Manufacture of biogas and biofuels for use in transport and of bioliquids'),
    ('Pre-commercial stages of advanced technologies to produce energy from nuclear processes with minimal waste from the fuel cycle',
     'Pre-commercial stages of advanced technologies to produce energy from nuclear processes with minimal waste from the fuel cycle'),
    ('Production of heat/cool from bioenergy', 'Production of heat/cool from bioenergy'),
    ('Production of heat/cool from fossil gaseous fuels in an efficient district heating and cooling system',
     'Production of heat/cool from fossil gaseous fuels in an efficient district heating and cooling system'),
    ('Production of heat/cool from geothermal energy', 'Production of heat/cool from geothermal energy'),
    ('Production of heat/cool from renewable non-fossil gaseous and liquid fuels', 'Production of heat/cool from renewable non-fossil gaseous and liquid fuels'),
    ('Production of heat/cool from solar thermal heating', 'Production of heat/cool from solar thermal heating'),
    ('Production of heat/cool using waste heat', 'Production of heat/cool using waste heat'),
    ('Storage of electricity', 'Storage of electricity'),
    ('Storage of hydrogen', 'Storage of hydrogen'),
    ('Storage of thermal energy', 'Storage of thermal energy'),
    ('Transmission and distribution networks for renewable and low-carbon gases', 'Transmission and distribution networks for renewable and low-carbon gases'),
    ('Transmission and distribution of electricity', 'Transmission and distribution of electricity'),
]

TAXONOMY_ACTIVITY_TYPE_CHOICES = [
    ('Eligible', 'Eligible'),
    ('Aligned', 'Aligned'),
    ('Non-Eligible', 'Non-Eligible')

]

CURRENCY_CHOICES = [('EUR', 'EUR'), ('USD', 'USD'), ('RON', 'RON')]

DNSH_CHOICES = [('Yes', 'Yes'),
                ('No', 'No')]

CLIMATE_CHANGE_CHOICES = [('Yes', 'Yes'),
                          ('No', 'No')]

DNSH_CRITERIA_CHOICES = [
    ('Climate change adaptation', 'Climate change adaptation'),
    ('Sustainable use and protection of water and marine resources',
     'Sustainable use and protection of water and marine resources'),
    ('Transition to a circular economy', 'Transition to a circular economy'),
    ('Pollution prevention and control', 'Pollution prevention and control'),
    ('Protection and restoration of biodiversity and ecosystems',
     'Protection and restoration of biodiversity and ecosystems')

]


COUNTY_CHOICES = [('Arges', 'Arges'),
                  ('Dolj', 'Dolj'),
                  ('Gorj', 'Gorj'),
                  ('Olt', 'Olt'),
                  ('Mehedinti', 'Mehedinti'),
                  ('Teleorman', 'Teleorman'),
                  ('Valcea', 'Valcea')]
