from services.groupings_services.grouping_interface import grouping_interface
from utils.GlobalConstants import *
class nm_groupings(grouping_interface):

    def get_groupings():
        return print('hey')
    
    def care_and_conditions():
        global_rs_data.where_like_filters['pagepath_clean'].add('/conditions-and-care-areas%')
        global_rs_data.groupings_column_list.append('pagepath_clean')
        global_rs_data.new_tableau_columns.append("CAC first level grouping")

    def service_lines():
        global_rs_data.groupings_column_list.append('pagepath_clean')
        global_rs_data.new_tableau_columns.append("service lines")

    def regions():
        region_application_display_name_filters = [
            'NM Northwestern Medicine - UA (filtered) (87477211) - Segment: NM Outside Regions',
            'NM Northwestern Medicine - UA (filtered) (87477211) - Segment: NM Central Region',
            'NM Northwestern Medicine - UA (filtered) (87477211) - Segment: NM North Region',
            'NM Northwestern Medicine - UA (filtered) (87477211) - Segment: NM Northwest Region',
            'NM Northwestern Medicine - UA (filtered) (87477211) - Segment: NM - Exclude Login Sessions',
            'NM Northwestern Medicine - UA (filtered) (87477211) - Segment: NM South Region',
            'NM Northwestern Medicine - UA (filtered) (87477211) - Segment: NM West Region',
            'NM Northwestern Medicine - UA (filtered) (87477211) - Segment: NM Outside IL',]

        global_rs_data.groupings_column_list.append('application_display_name')

        global_rs_data.where_in_filters['application_display_name'].update(region_application_display_name_filters)