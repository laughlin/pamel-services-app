from models.EngineModel import EngineModel
from models.DataModel import DataModel

SERVER = 'laughlin_constable.channelmix.com'
DATABASE = 'laughlin_constable'
USERNAME = 'laughlin_constable_reporting'
PASSWORD = 'gF:0=A3gOh:4W2r$Zi~7Va6-'
PORT = '5439'

global global_rs_data
global global_rs_engine

global_rs_data = DataModel()
global_rs_engine = EngineModel()
