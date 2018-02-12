import flask
from flask import request, Blueprint, render_template, redirect, url_for

from services import QueryService
from models.DataModel import DataModel
from models.EngineModel import EngineModel

from utils.GlobalConstants import global_rs_engine, global_rs_data

BP_NAME='common'
common = Blueprint(BP_NAME, __name__)


@common.route("/", methods=['GET','POST'])
def check_login():
    global global_rs_engine, global_rs_data
    if request.method == 'GET':
        if global_rs_engine.engine == "":
            return redirect(url_for(BP_NAME+'.login_redshift'))
        else:
            return render_template(BP_NAME+'/logout_or_continue.html',
                server=global_rs_engine.server, database=global_rs_engine.database, username=global_rs_engine.username)
    elif request.method == 'POST':
        if request.form['logout_submit']:
            global_rs_data = DataModel()
            global_rs_engine = EngineModel()
            return redirect(url_for(BP_NAME+'.login_redshift'))
        else:
            if global_rs_data.schema == "":
                return redirect(url_for(BP_NAME+'.set_schema'))
            else: return redirect(url_for(BP_NAME+'.services'))

@common.route("/login", methods=['GET', 'POST'])
def login_redshift():
    if request.method == 'GET':
        return flask.render_template(BP_NAME+'/server_login.html')
    elif request.method == 'POST':
        global_rs_engine.server = request.form['select_server']
        global_rs_engine.database = request.form['select_db']
        global_rs_engine.username = request.form['select_username']
        global_rs_engine.password = request.form['select_password']
        global_rs_engine.port = request.form['select_port']

        global_rs_engine.set_engine()
        return redirect(url_for(BP_NAME+'.set_schema'))


@common.route("/set-schema", methods=['GET', 'POST'])
def set_schema():
    if request.method == 'GET':
        schema_names = QueryService.get_schemas(global_rs_engine.engine)
        return flask.render_template(BP_NAME+'/set_schema.html', schemas=list(schema_names))
    elif request.method == 'POST':
        global_rs_data.schema = request.form['select_schema']
        return redirect(url_for(BP_NAME+'.services'))

@common.route("/services", methods=['GET'])
def services():
    if request.method == 'GET':
        return render_template(BP_NAME+'/services.html')




'''
@errorhandler(404)
def page_not_found(error):
    return flask.render_template('page_not_found.html'), 404
'''
