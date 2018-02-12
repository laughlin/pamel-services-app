from flask import request, Blueprint, redirect, render_template, url_for

from models.DataModel import DataModel
from models.EngineModel import EngineModel
from services import QueryService
from utils.GlobalDecorators import *
from utils.GlobalConstants import global_rs_data, global_rs_engine
from utils.available_groupings_mapping import mappings

BP_NAME = 'extract'

extract = Blueprint(BP_NAME, __name__)


@extract.route("/", methods=['GET'])
def redirect_to_table():
    return redirect(url_for(BP_NAME+'.set_table'))

@extract.route("/set-table", methods=['GET', 'POST'])
def set_table():
    if request.method == 'GET':
        table_names = QueryService.get_tables(global_rs_engine.engine, global_rs_data.schema)
        return render_template(BP_NAME+'/set_table.html', tables=list(table_names))
    if request.method == 'POST':
        global_rs_data.table = request.form['select_table']
        return redirect(url_for(BP_NAME+'.set_groupings'))


@extract.route("/set-groupings", methods=['GET', 'POST'])
def set_groupings():
    if request.method == 'GET':
        available_groupings = mappings[global_rs_data.schema][global_rs_data.table]['groupings']
        return render_template(BP_NAME+'/set_groupings.html', groupings=list(available_groupings))
    elif request.method == 'POST':
        list_of_selected_groupings = request.form.getlist('select_groupings')
        for selected in list_of_selected_groupings:
            print("Selected: ", selected)
            print("First new: ", global_rs_data.new_tableau_columns)
            mappings[global_rs_data.schema][global_rs_data.table]['groupings'][selected]()
            print("Then new: ", global_rs_data.new_tableau_columns)
            
        return redirect(url_for(BP_NAME+'.set_columns'))


@extract.route("/set-columns", methods=['GET', 'POST'])
def set_columns():
    if request.method == 'GET':
        available_columns = QueryService.get_columns(global_rs_engine.engine, global_rs_data.schema, global_rs_data.table)
        return render_template(BP_NAME+'/set_columns.html', columns=list(available_columns))
    elif request.method == 'POST':
        global_rs_data.extract_column_list = request.form.getlist('select_columns')
        return redirect(url_for(BP_NAME+'.set_dates'))

#TODO: find faster way to query the data and get the date range
@extract.route("/set-dates", methods=['GET', 'POST'])
def set_dates():
    if request.method == 'GET':
        start_date, end_date = QueryService.get_dates(
            global_rs_engine.engine, global_rs_data.schema, global_rs_data.table,
            global_rs_data.where_in_filters, global_rs_data.where_like_filters)
        return render_template(BP_NAME+'/set_dates.html', date_range="Start: "+str(start_date)+"End: "+str(end_date))
    elif request.method == 'POST':
        global_rs_data.start_date = request.form['select_start_date']
        global_rs_data.end_date = request.form['select_end_date']
        #Currently has no end
        #return flask.redirect(flask.url_for('extract.set_dates'))


# Not currently built out
@extract.route("/set-filters", methods=['GET', 'POST'])
def set_filters():
    if request.method == 'GET':
        available_filters = QueryService.get_columns(global_rs_engine.engine, global_rs_data.schema, global_rs_data.table)
        return render_template(BP_NAME+'/set_filters.html', filters=list(available_filters))
    if request.method == 'POST':
        list_of_selected_filters = request.form.getlist('select_filters')
        for selected in list_of_selected_groupings:
            print('nothing yet')
            
        return redirect(url_for(BP_NAME+'.select_client_get'))