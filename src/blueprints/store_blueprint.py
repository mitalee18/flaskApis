from flask import Blueprint, jsonify, request
from controller.store_controller import StoreController

store_api = Blueprint('store_api', __name__, url_prefix='/api/store')
store_controller = StoreController()
@store_api.route('/')
def hello():
    return "Hello World"

@store_api.route('/getStores', methods = ["GET"])
def get_stores():
    data = {
        "store": store_controller.get_all_stores()
    }
    return jsonify(data), 200

@store_api.route('/addStore', methods = ["POST"])
def add_store():
    data = request.get_json()
    new_store = {
        "name": data["name"],
        "items": []
    }
    store_controller.add_store(new_store)
    return jsonify(data), 201

@store_api.route("/addStore/<name>/item", methods=["POST"])
def create_item(name):
    data = request.get_json()
    if store_controller.is_store_present(name):
        new_item = {
            "name": data["name"],
            "price": data["price"]
        }
        try:
            return jsonify(store_controller.add_item(new_item, name)), 201
        except Exception as e:
            return handle_error(e, f"Error[{type(e)}]{str(e)}", "'/api/store/addStore")
    return {"message":"Store not found"}, 404

@store_api.route("/getStore/<name>", methods=["GET"])
def get_store(name):
    if store_controller.is_store_present(name):
        try:
            return jsonify(store_controller.get_store(name)), 200
        except Exception as e:
            return handle_error(e, f"Error[{type(e)}]{str(e)}", "'/api/store/addStore")
    return {"message":"Store not found"}, 404


@store_api.app_errorhandler(Exception)
def handle_error(error, messg="Unknown Error", api_name="/store_api", code=500):
    response = {
        'status': code,
        'api': api_name,
        'error': {
            'type': error.__class__.__name__,
            'message': messg
        }
    }
    return jsonify(response), code


