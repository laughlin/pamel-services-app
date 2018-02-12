from flask import request, Blueprint, redirect, render_template, url_for
from functions.clustering import kmeans_quick

BP_NAME = 'user_segmentation'

user_segmentation = Blueprint(BP_NAME, __name__)


@user_segmentation.route("", methods=['GET'])
def home():
    return render_template(BP_NAME+'/home.html')

@user_segmentation.route("/previous-report", methods=['GET'])
def previous_report():
    # Here, will extract previous reports from folder structure
    return print("Nothing yet")

@user_segmentation.route("/new-report", methods=['GET'])
def new_report():
    # Will update reports with predictions of data
    # Will read from stored model
    # These should be easy to predict base on that old model
    # Then just fill it in with the old template
    
    return print("Nothing yet")

@user_segmentation.route("/refresh-model", methods=['GET'])
def refresh_model():
    # HTML should have indication next to it indicating how long it's been since a refresh
    # But, as a warning, refreshing the model will make changes to analytics

    #Will rerun the model with previous parameters, output changes from predicted to new predicted?
    # Provide parameters on success compared with the model's previous parameters of success
    # This gives you a way to see if you in fact need to retune the model rather than refresh
    return print("Nothing yet")

@user_segmentation.route("/new-model", methods=['GET'])
def new_model():
    # Will need an initial loading screen while the model compiles and runs metrics
    # Person will be given metrics on the data columns selected
    # So, they really only need to select parameters of the model
    # Once model is selected, should have an option to gp back to a previous model
    # Some version control element
    data_with_labels = kmeans_quick(get_data_from_db, etc, etc, etc)
    return print("Nothing yet")