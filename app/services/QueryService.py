"""Used to create pkl files of alight data selected.

Do this if you either want to update the data pulled in or want to select a new schema.
Pass in the schema name to the function and then run. It may take a while to
 finish pickling the file.
"""

import pandas as pd
import time
from models.DataModel import DataModel
from utils.GlobalDecorators import auto_attr_check
from utils.GlobalConstants import global_rs_data

# Service of calling queries on the redshift database
#@auto_attr_check
#class QueryService:

def get_schemas(engine):
    schemas = pd.read_sql_query('select nspname from pg_namespace', engine)
    non_temp_schemas = schemas[~schemas['nspname'].str.contains('temp')]['nspname']
    return non_temp_schemas

def get_tables(engine, schema):
    available_tables = pd.read_sql_query(
        'select table_name from laughlin_constable.INFORMATION_SCHEMA.TABLES where table_schema = %s;',
        engine, params=[schema])
    return available_tables['table_name']

def get_columns(engine, schema, table):
    query = pd.read_sql_query('SELECT TOP 1 * FROM {}.{};'.format(schema, table), engine)
    return query.columns

def get_dates(engine, schema, table, where_in_filters, where_like_filters):
    params_list = []
    filters_query_list = []
    for i in where_in_filters:
        filters_query_list.append(" "+i+' IN ('+'%s,'*(len(where_in_filters[i])-1)+'%s)')
        for j in where_in_filters[i]:
            params_list.append(j)
    where_query_string = "".join(filters_query_list)
    
    # Make into a string builder
    for i in where_like_filters:
        if where_query_string == "":
            where_query_string = " "+i+' LIKE %s'
        else:
            where_query_string += ' AND '+i+' LIKE %s'
        params_list.append(where_like_filters[i])

    if where_query_string != "":
        where_query_string = ''.join(('WHERE',where_query_string))
    query = pd.read_sql_query(
        'SELECT MIN(report_date), MAX(report_date) FROM '+schema+"."+table+
        ' '+where_query_string+';', engine, params=params_list)
    print(query)
    return query['min'][0], query['max'][0]

def get_data(engine, schema, table, columns, start_date, end_date, where_in_filters="", where_like_filters=""):
    start = time.time()

    params_list = []
    params_list.append(start_date)
    params_list.append(end_date)
    
    columns_as_string = ', '.join(columns)
    
    if where_in_filters != "":
        filters_query_list = []
    
        for i in where_in_filters:
            filters_query_list.append(' AND '+i+' IN ('+'%s,'*(len(where_in_filters[i])-1)+'%s)')
            for j in where_in_filters[i]:
                params_list.append(j)

        filters_query_string = "".join(filters_query_list)
    else: filters_query_string = ""
    
    if where_like_filters != "":
        for i in where_like_filters:
            filters_query_string += ' AND '+i+' LIKE %s'
            params_list.append(where_like_filters[i])
    
    print(columns_as_string)
    print('\n Param List: ', params_list)
    print('\nSELECT '+columns_as_string+' FROM '+schema+"."+table+
        ' WHERE report_date BETWEEN %s AND %s'+filters_query_string+';')
    
    query = pd.read_sql_query(
        'SELECT '+columns_as_string+' FROM '+schema+"."+table+
        ' WHERE report_date BETWEEN %s AND %s'+filters_query_string+';', engine, params=params_list)
    
    return query, "\n Time it took in seconds: " + str(time.time() - start)