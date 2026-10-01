import os
import json
from flask import Flask, render_template, jsonify, request
# import the functions from uninformed and informed
from uninformed import bfs,dfs,ucs,ids
from informed import greedy_best_first,a_star

app = Flask(__name__)


MAP_DATA_FILE = "map_data.json"
ALGORITHMS = {
    "bfs": bfs,
    "dfs": dfs,
    "ucs": ucs,
    "ids": ids,
    "greedy": greedy_best_first,
    "astar": a_star
}

def load_map_data():
    """Load graph and location data from map_data.json if available."""
    if os.path.exists(MAP_DATA_FILE):
        try:
            with open(MAP_DATA_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {MAP_DATA_FILE}: {e}")
    return {
        "region": "State / Metro Area",
        "total_cities": 0,
        "total_edges": 0,
        "locations": {},
        "graph": {}
    }


@app.route("/")
def index():
    """Renders the main deployment webpage."""
    return render_template("index.html")


@app.route("/api/map", methods=["GET"])
def get_map():
    """Returns map locations and graph connections."""
    data = load_map_data()
    return jsonify(data)


@app.route("/api/search", methods=["POST"])
def search():
    payload = request.get_json() or {}

    start = payload.get("start", "")
    goal = payload.get("goal", "")
    algorithm = payload.get("algorithm", "")

    data = load_map_data()
    graph = data["graph"]
    locations = data["locations"]

    if start not in graph:
        return jsonify({
            "status": "error",
            "message": f"Unknown start city: {start}"
        }), 400

    if goal not in graph:
        return jsonify({
            "status": "error",
            "message": f"Unknown goal city: {goal}"
        }), 400

    if algorithm not in ALGORITHMS:
        return jsonify({
            "status": "error",
            "message": f"Unknown algorithm: {algorithm}"
        }), 400

    search_algorithm = ALGORITHMS[algorithm]

    if algorithm in ["greedy", "astar"]:
        result = search_algorithm(
            graph,
            locations,
            start,
            goal
        )
    else:
        result = search_algorithm(
            graph,
            start,
            goal
        )

    return jsonify({
        "status": "success",
        "message": f"{algorithm} search completed.",
        "path": result["path"],
        "cost": result["cost"],
        "nodes_expanded": result["nodes_expanded"]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
