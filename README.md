# pamel-services-app

To run the application locally, have conda/mini conda installed.

Navigate the the root folder and then run the command:

`$conda env create -f requirements.txt -n PAMeLServicesApp`

This creates your virtual environment to run the application in. Next steps are to activate that environment and then run the app.

`$conda activate PAMeLServicesApp`

`$cd app`

`$python __init__.py`

This will start the app. It currently runs on localhost port 5000 which can be reached by typing __http://localhost:5000/__ in the browser.
