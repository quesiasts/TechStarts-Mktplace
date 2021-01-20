from flask import Flask, render_template

from frontend.category_web import category_bp
from frontend.log_web import log_bp
from frontend.marketplace_web import marketplace_bp
from frontend.product_web import product_bp
from frontend.seller_web import seller_bp

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.register_blueprint(marketplace_bp)
app.register_blueprint(category_bp)
app.register_blueprint(product_bp)
app.register_blueprint(seller_bp)
app.register_blueprint(log_bp)


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
