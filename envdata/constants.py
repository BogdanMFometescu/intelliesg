# GENERAL INFO FOR EMISSIONS

EMISSION_TYPE = [('Car fuels', 'Car fuels',),
                 ('SF6', 'SF6'),
                 ('Refrigerants', 'Refrigerants',),
                 ('Energy Acquisition', 'Energy Acquisition')]

EMISSION_SCOPE = [('Scope 1', 'Scope 1'),
                  ('Scope 2', 'Scope 2'),
                  ('Scope 3', 'Scope 3')]

CALCULATION_METHOD = [('Sales Approach (Product)', 'Sales Approach (Product)'),
                      ('Sales Approach (User)', 'Sales Approach (User'),
                      ('LifeCycle Stage Approach', 'LifeCycle Stage Approach')]

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
                ('Other diesel Non-Road Vehicles', 'Other diesel Non-Road Vehicles')]

POLLUTION_NORM = [('Euro 1', 'Euro 1'),
                  ('Euro 2', 'Euro 2'),
                  ('Euro 3', 'Euro 3'),
                  ('Euro 4', 'Euro 4'),
                  ('Euro 5', 'Euro 5'),
                  ('Euro 6', 'Euro 6')]

TEST_DICT = {
    'fuel_type': {'diesel': [('Diesel passenger cars', 'Diesel passenger cars')],
                  'gasoline': [('Gasoline cars', 'Gasoline cars')]}

}
