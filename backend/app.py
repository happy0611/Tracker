from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_data():
    data = {"img": "images\71QnzJ5ujAL._AC_UL600_SR600,400_.jpg"}
    return data

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder,path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    app.run(debug=True)