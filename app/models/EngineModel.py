import pandas as pd
import sys
import datetime
from sqlalchemy import create_engine

class EngineModel():
    def __init__(self):
        self.server = ""
        self.database = ""
        self.username = ""
        self.password = ""
        self.port = ""

        self.engine = ""

    # if you want to se the engine based on already set variables
    def set_engine(self):
        try:
            self.engine = create_engine(
                'postgresql://'+self.username+':'+self.password+'@'+self.server+':'+self.port+'/'+self.database)
        except:
            print("Engine could not be set. Make sure all aspects are correct before continuing. The current values of the variables are:")
            print("Server: " + self.server)
            print("Database: " + self.database)
            print("Username: " + self.username)
            print("Password: " + self.password)
            print("Port: " + self.port)

    # Set a new engine with fresh variables
    def set_engine2(self, server, database, username, password, port):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.port = port
        try:
            self.engine = create_engine(
                'postgresql://'+username+':'+password+'@'+server+':'+port+'/'+database)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
