from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def predict_coauthors():
    author_id = request.args.get('id')
    # Use your model to predict co-authors for the given author_id
    # For simplicity, we'll use dummy data here
    results = [
        {"authorID": "some_author_1", "likeliness": 1, "rank": 1},
        {"authorID": "some_author_2", "likeliness": 1, "rank": 2},
        {"authorID": "some_author_3", "likeliness": 1, "rank": 3}
    ]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
