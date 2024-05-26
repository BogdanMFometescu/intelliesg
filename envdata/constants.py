# GENERAL INFO FOR EMISSIONS

EMISSION_TYPE = [('Car fuels', 'Car fuels',),
                 ('SF6', 'SF6'),
                 ('Refrigerants', 'Refrigerants',),
                 ('Natural gas', 'Natural gas',),
                 ('Energy Acquisition', 'Energy Acquisition'),
                 ('Travel', 'Travel'),
                 ('Waste', 'Waste')]

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

TAXONOMY_SECTOR_CHOICES = [('Accommodation activities', 'Accommodation activities'),
                           ('Arts, entertainment and recreation', 'Arts, entertainment and recreation')]

TAXONOMY_ACTIVITY_CHOICES = [
    ('Transmission and distribution of electricity', 'Transmission and distribution of electricity')]

TAXONOMY_ACTIVITY_TYPE_CHOICES = [
    ('Eligible', 'Eligible'),
    ('Aligned', 'Aligned'),
    ('Not Aligned', 'Not Aligned')

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
