from flask import Blueprint
from flask import request, jsonify
import logic as object

object_page = Blueprint('object_page', __name__, template_folder='templates')

@object_page.route("/<object_type>", methods=["GET"])
def get_object(object_type):
	if not object.check_object(object_type):
		return jsonify(f"Invalid path: /{object_type}"), 404
	object_id = request.args.get(f"{object_type}_id")
	if not object_id:
		return(f"no {object_type} id was provided. (add {object_type}_id argument)"), 400
	try:
		object_obj = object.get_object(object_type, object_id)
		if object_obj:
			return jsonify(object_obj), 200
		else:
			return jsonify("object not found"), 400
	except Exception as e:
		return jsonify("object not found"), 400
	
@object_page.route("/<object_type>", methods=["POST"])
def create_object(object_type):
	if not object.check_object(object_type):
		return jsonify(f"Invalid path: /{object_type}"), 404
	data = request.json
	if not object_type in data:
		return jsonify(f"missing {object_type} info. (add {object_type} object in body)"), 400
	object_info = data[object_type]
	object_id = object.create_object(object_type, object_info)
	if object_id:
		return jsonify({"objectId": object_id}), 201
	else:
		return jsonify("error occured while creating object"), 500
	
@object_page.route("/<object_type>", methods=["PUT"])
def update_object(object_type):
	if not object.check_object(object_type):
		return jsonify(f"Invalid path: /{object_type}"), 404
	object_id = request.args.get(f"{object_type}_id")
	data = request.json
	if not object_type in data:
		return jsonify(f"missing {object_type} info to change. (add {object_type} object in body)"), 400
	object_info = data[object_type]
	object.update_object(object_type, object_id, object_info)
	return jsonify(f"Successfully updated {object_type} with id: {object_id}"), 200

@object_page.route("/<object_type>", methods=["DELETE"])
def delete_object(object_type):
	if not object.check_object(object_type):
		return jsonify(f"Invalid path: /{object_type}"), 404
	object_id = request.args.get(f"{object_type}_id")
	object.delete_object(object_type, object_id)
	return jsonify(f"Successfully deleted {object_type} with id: {object_id}"), 204