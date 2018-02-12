from flask import request, Blueprint, redirect, render_template, url_for

BP_NAME='anomalies'
anomalies = Blueprint(BP_NAME, __name__)

@anomalies.route("", methods=['GET'])
def home():
    return render_template(BP_NAME+'/home.html')