from tinydb import TinyDB, Query
from datetime import datetime
import base64
import numpy as np

db = TinyDB("drawings_db.json")

def encode_numpy_array(array):
    return base64.b64encode(array.tobytes()).decode('utf-8')

def save_drawing_to_db(name, matrix):
    encoded_matrix = encode_numpy_array(matrix)
    db.insert({
        'name': name,
        'timestamp': datetime.now().isoformat(),
        'matrix': encoded_matrix
    })
    print(f"✅ Saved to database as '{name}'")
