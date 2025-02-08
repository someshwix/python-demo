from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

fake_data = [
    {'id': 1, 'name': 'item1', 'price': 100},
    {'id': 2, 'name': 'item2', 'price': 200},
    {'id': 3, 'name': 'item3', 'price': 300},
]

class Item(Resource):
    def get(self, item_id):
        item = next((item for item in fake_data if item['id'] == item_id), None)
        if item:
            return jsonify(item)
        return {'message': 'Item not found'}, 404

    def post(self):
        new_item = request.get_json()
        fake_data.append(new_item)
        return jsonify(new_item), 201

    def put(self, item_id):
        item = next((item for item in fake_data if item['id'] == item_id), None)
        if item:
            data = request.get_json()
            item.update(data)
            return jsonify(item)
        return {'message': 'Item not found'}, 404

    def delete(self, item_id):
        global fake_data
        fake_data = [item for item in fake_data if item['id'] != item_id]
        return {'message': 'Item deleted'}

api.add_resource(Item, '/item', '/item/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)