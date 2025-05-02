# gallery.py
import matplotlib.pyplot as plt
import numpy as np
import base64
from tinydb import TinyDB
import math

def decode_numpy_array(encoded_str, shape=(80, 80), dtype=np.float64):
    decoded_bytes = base64.b64decode(encoded_str.encode('utf-8'))
    return np.frombuffer(decoded_bytes, dtype=dtype).reshape(shape)

def show_gallery():
    db = TinyDB("drawings_db.json")
    entries = db.all()

    if not entries:
        print(" We dont have any data atm :( maybe you would help us with your masterpieces! ")
        return

    n = len(entries)
    cols = 3
    rows = math.ceil(n / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(12, 4 * rows))

    for idx, entry in enumerate(entries):
        row, col = divmod(idx, cols)
        ax = axes[row, col] if rows > 1 else axes[col]

        T = decode_numpy_array(entry['matrix'])
        ax.imshow(T, cmap='hot', vmin=0, vmax=100)
        ax.set_title(f"{entry['name']}\n{entry['timestamp'][:16]}")
        ax.axis('off')


    for i in range(n, rows * cols):
        row, col = divmod(i, cols)
        ax = axes[row, col] if rows > 1 else axes[col]
        ax.axis('off')

    plt.suptitle("Saved heat diffusion arts!", fontsize=16)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    show_gallery()
