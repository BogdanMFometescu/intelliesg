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

TEST_DICT = {
    'fuel_type': {'diesel': [('Diesel passenger cars', 'Diesel passenger cars')],
                  'gasoline': [('Gasoline cars', 'Gasoline cars')]}

}
