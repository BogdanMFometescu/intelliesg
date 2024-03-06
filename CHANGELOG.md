# intelliesg

- Changelog for the intelliesg app

[06.03.2024]

Version 0.2.6
-
- added a target model in models.py
- updated constants
- added month and year fields in models.py




[03.03.2024]

Version 0.2.5
-
- refactored the navbar
- updated companies html template


[03.03.2024]

Version 0.2.4
-
- refactored the navbar
- created methods in models for envdata to sum up values per company



[02.03.2024]

Version 0.2.3
-
- created the html for the envdata forms


[01.03.2024]

Version 0.2.2
-
- drafted the html templates for each emission type


[29.02.2024]

Version 0.2.1
-
- changed uikit
- updated navbar and some html templates



[27.02.2024]

Version 0.2.0
-
- added uikit
- created html templates for navbar, base
- refactored the forms from envdata app to display css formats
- updated urls from envdata app




[26.02.2024]

Version 0.1.2
-
- finished the views for envdata app (added python package)
- added html templates for each view
- updated urls for envdata app



[25.02.2024]

Version 0.1.1
-
- refactored the models for envdata app
- added bootstrap to the base.html
- added new emission type to constants.py: travel 
- small refactoring of the html templates
- added new model : company in envdata app
- updated urls in envdata app
- created a views package to keep the code clean and maintainable
- deletes emissions model 



[24.02.2024]

Version 0.1.0
-
-modified admin.py for envdata app 


[19.01.2024]

Version 0.0.9
-
- switching from FBV to CBV : views.py and urls.py finished.


[18.01.2024]

Version 0.0.8
-
- switching from FBV to CBV



[17.01.2024]

Version 0.0.7
-
- added new model in envdata/models.py for waste
- created two methods for the waste model
- added flake8 as dependency 

[16.01.2024]

Version 0.0.6
-
- added methods in envdata/views.py for DistanceCalculation model
- added url paths for DistanceCalculation model
- added forms, html templates for DistanceCalculation model


[14.01.2024]

Version 0.0.5
-
- added methods for CRUD in envdata/views.py for Sf6Emissions,RefrigerantsEmissions,EnergyAcquisition
- added modelform for Sf6Emissions,RefrigerantsEmissions,EnergyAcquisition in envdata/forms.py
- added html templates for Sf6Emissions,RefrigerantsEmissions,EnergyAcquisition
- updated envdata/urls.py with Sf6Emissions,RefrigerantsEmissions,EnergyAcquisition paths
- created new app :socialdata
- added requests package
- created new model in envdata/models.py :DistanceCalculation
- created forms.py for emissions and fuel emissions
- created url paths for emissions and fuel emissions
- filled in the form-emissions.html




[13.01.2024]

Version 0.0.4
-
- refactored classes from envdata/model.py
- created envdata/constants.py
- created envdata/forms.py




[11.01.2024]

Version 0.0.3
-
-created draft classes for envdata/models.py  


[10.01.2024]

Version 0.0.2
-
- created poetry environment
- created django project : intelliesg
- created django app : envdata
- created db connection: postgresql
- created the dotenv file
- added whitenoise for staticfiles management
- finished configuring settings.py 


Version 0.0.1
-
- initial commit








