from models.article import *
from errorsModel.errors import *


@app.route('/article', methods=['GET'])
def get_articles():
    # return_value = jsonify(Article.get_all_article())
    return jsonify(Article.get_all_article()), 200
    # return (return_value, status=200, mimetype='application/json')


@ app.route('/article/<int:id>', methods=['GET'])
def get_article_by_id(id):
    return_value = Article.get_article(id)
    print(return_value)
    if return_value == None:
        return jsonify('None'), 404
    else:
        return jsonify(return_value), 200
    # print(return_value)
    # if(return_value):
    #     return jsonify(return_value), 200
    # else:
    #     raise NotCreated


@ app.route('/article', methods=['POST'])
def add_article():
    request_data = request.get_json()
    return Article.add_article(request_data["name"], request_data["description"],
                               request_data["prix"]), 201
    # if(insert):
    #     print(insert)
    #     # return jsonify(insert), 201
    # else:
    #     raise NotCreated


@ app.route('/article/<int:id>', methods=['PUT'])
def update_article(id):
    request_data = request.get_json()
    return Article.update_article(id, request_data['name'], request_data['description'],
                                  request_data['prix']), 200


@ app.route('/article/<int:id>', methods=['DELETE'])
def remove_article(id):
    Article.delete_article(id)
    # response = Response("Article Deleted", status=200,
    #                     mimetype='application/json')
    # return response


if __name__ == "__main__":
    app.testing = True
    app.run(port=1234, debug=True)
