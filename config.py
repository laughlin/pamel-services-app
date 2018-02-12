# This is where universsal variables go? Things lke email addresses
# Once there is a production and review level, this config turns into a folder struture
# With review and production files
# http://exploreflask.com/en/latest/configuration.html
# These can be called by calling app.config[VARIABLE_HERE] in the app
# Or app.config("config") to call the entire file.

DEBUG = False

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  