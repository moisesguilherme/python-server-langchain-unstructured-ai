from flask import Flask, jsonify
from service import process_file
import numpy as np
import pandas as pd
from langchain_unstructured import __version__ as langchain_version

app = Flask(__name__)

@app.route('/ola', methods=['GET'])
def ola():
    versions = {
        "message": "Olá, bem-vindo à API!",
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
        "langchain_unstructured_version": langchain_version
    }
    return jsonify(versions)

@app.route('/process', methods=['GET'])
def process():
    result = process_file()
    return jsonify({"data": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
