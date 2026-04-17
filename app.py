from flask import Flask
from routes.sales_routes import sales_bp

app = Flask(__name__)
app.register_blueprint(sales_bp)

if __name__ == "__main__":
    app.run(debug=True)