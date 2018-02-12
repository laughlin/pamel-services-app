from flask import Flask
from views.extract import extract
from views.common import common
from views.user_segmentation import user_segmentation
from views.anomalies import anomalies

app = Flask(__name__)
app.register_blueprint(common)
app.register_blueprint(extract, url_prefix='/extract')
app.register_blueprint(user_segmentation, url_prefix='/user-segmentation')
app.register_blueprint(anomalies, url_prefix='/anomalies')

if __name__ == "__main__":
    app.run()
    