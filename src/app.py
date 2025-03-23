from flask import Flask, request

from src.constants import HEALTH_MSG

app = Flask(__name__)

todos = [
    {"title": "Coder l'application", "description": "Todo list", "completed": False}
]


@app.get("/todos")
def get_todos():
    return {"todos": todos}


@app.post("/todos")
def create_todo():
    request_data = request.get_json()
    new_todo = {
        "title": request_data["title"],
        "description": request_data["description"],
        "completed": False,
    }
    todos.append(new_todo)
    return new_todo, 201


# def create_app(config):
#     app = Flask(__name__)
#     app.config.from_object(config)
#
#     @app.route("/health")
#     def api_health():
#         return HEALTH_MSG
#
#     return app
