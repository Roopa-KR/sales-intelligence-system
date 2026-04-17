from flask import Blueprint, request, jsonify
import pandas as pd
from services.data_cleaning import clean_data
from services.db_service import insert_data

sales_bp = Blueprint('sales', __name__)

@sales_bp.route('/upload-sales', methods=['POST'])
def upload_sales():
    file = request.files['file']
    df = pd.read_csv(file)

    df = clean_data(df)
    insert_data(df)

    return jsonify({"message": "Data uploaded successfully"})