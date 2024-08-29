from flask import Flask, request, jsonify
from helpers import sort_titles, video_list, search_video

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')
    find_title = search_video(sort_titles(video_list ), title) 
    if find_title is None:
        return jsonify("Video not Found"), 404
    else:
        return jsonify(find_title), 200
if __name__ == '__main__':
    app.run(debug=True)