import datetime
import time
from collections import defaultdict

class DataModel:
    def __init__(self):
        self.schema = ""
        self.table = ""
        self.groupings_column_list = []

        self.where_in_filters = defaultdict(set)
        self.where_like_filters = defaultdict(set)

        self.extract_columns_list = []
        self.start_date = datetime.time(0, 0, 0)
        self.end_date = datetime.time(0,0,0)
        self.update_daily = False

        

        self.new_tableau_columns = []