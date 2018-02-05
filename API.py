from flask import Flask, request, jsonify, abort
import os.path
import json

#source from https://www.youtube.com/watch?v=2gunLuqHvc8

app = Flask(__name__)

with open('data.json', 'r') as json_data:
    data_json = json.load(json_data)

actors_list = data_json[0]
movies_list = data_json[1]

#=================Get========================
@app.route('/Assignment2.1/actors/<string:actor_name>', methods=['GET'])
def filter_actor(actor_name):
    actor_filter = []
    for actor in actors_list:
        if(actor_name in actors_list[actor]['name']):
            actor_info = actors_list[actor]
            actor_filter.append({actor:actor_info})

    if(actor_filter == []):
        abort(400)

    return jsonify(actor_filter)

@app.route('/Assignment2.1/actors_age/<int:actor_age>', methods=['GET'])
def filter_age(actor_age):
    actor_filter = []
    for actor in actors_list:
        if(actor_age == actors_list[actor]['age']):
            actor_info = actors_list[actor]
            actor_filter.append({actor:actor_info})

    if(actor_filter == []):
        abort(400)

    return jsonify(actor_filter)

@app.route('/Assignment2.1/actors_gross/<int:actor_gross>', methods=['GET'])
def filter_acter_gross(actor_gross):
    actor_filter = []
    for actor in actors_list:
        if(actor_gross == actors_list[actor]['total_gross']):
            actor_info = actors_list[actor]
            actor_filter.append({actor:actor_info})
    if(actor_filter == []):
        abort(400)

    return jsonify(actor_filter)

@app.route('/Assignment2.1/movies/<string:movie_name>', methods=['GET'])
def filter_movie(movie_name):
    movie_filter = []
    for actor in actors_list:
        actor_movies = actors_list[actor]['movies']
        for i in range(0, len(actor_movies)):
            if(movie_name in actor_movies[i]):
                actor_info = actors_list[actor]
                movie_filter.append({actor:actor_info})

    if(movie_filter == []):
        abort(400)
    return jsonify(movie_filter)

@app.route('/Assignment2.1/movie_actor/<string:actor_name>', methods=['GET'])
def filter_movie_actor(actor_name):
    movie_filter = []
    for movie in movies_list:
        movie_actors = movies_list[movie]['actors']
        for i in range(0, len(movie_actors)):
            if(actor_name in movie_actors[i]):
                movie_info = movies_list[movie]
                movie_filter.append({movie:movie_info})

    if(movie_filter == []):
        abort(400)
    return jsonify(movie_filter)

@app.route('/Assignment2.1/movie_year/<int:movie_year>', methods=['GET'])
def filter_year(movie_year):
    movie_filter = []
    for movie in movies_list:
        if(movie_year == movies_list[movie]['year']):
            movie_info = movies_list[movie]
            movie_filter.append({movie:movie_info})
    if(movie_filter == []):
        abort(400)
    return jsonify(movie_filter)

@app.route('/Assignment2.1/movie_gross/<int:movie_gross>', methods=['GET'])
def filter_movie_gross(movie_gross):
    movie_filter = []
    for movie in movies_list:
        if(movie_gross == movies_list[movie]['box_office']):
            movie_info = movies_list[movie]
            movie_filter.append({movie:movie_info})
    if(movie_filter == []):
        abort(400)
    return jsonify(movie_filter)


#=================Put========================
@app.route('/Assignment2.1/actor_put/<string:actor_name>', methods=['PUT'])
def actor_put(actor_name):
    put_actor = []
    for actor in actors_list:
        if(actor_name in actors_list[actor]['name']):
            actor_info = actors_list[actor]
            put_actor.append({actor:actor_info})
            actors_list[actor_name]['total_gross'] = request.json['total_gross']

    if(put_actor == []):
        abort(400)

    return jsonify(actors_list)

@app.route('/Assignment2.1/movie_put/<string:movie_name>', methods=['PUT'])
def movie_put(movie_name):
    put_movie = []
    for movie in movies_list:
        if(movie_name in movies_list[movie]['name']):
            movie_info = movies_list[movie]
            put_movie.append({movie:movie_info})
            movies_list[movie_name]['box_office'] = request.json['box_office']

    if(put_movie == []):
        abort(400)
    return jsonify(put_movie)

#=================Delete=======================
@app.route('/Assignment2.1/actor_del/<string:actor_name>', methods=['DELETE'])
def delete_actor(actor_name):
    actor_delete = []
    for actor in actors_list:
        if(actor_name in actors_list[actor]['name']):
            actor_info = actors_list[actor]
            actor_delete.append({actor:actor_info})

    if(actor_delete == []):
        abort(400)

    actors_list.pop(actor_name)
    return jsonify(actors_list)

@app.route('/Assignment2.1/movie_del/<string:movie_name>', methods=['DELETE'])
def delete_movie(movie_name):
    movie_delete = []
    for movie in movies_list:
        if(movie_name in movies_list[movie]['name']):
            movie_info = movies_list[movie]
            movie_delete.append({movie:movie_info})

    if(movie_delete == []):
        abort(400)
    movies_list.pop(movie_name)
    return jsonify(movies_list)

#=================Post========================
@app.route('/Assignment2.1/add_actor', methods=['POST'])
def add_actor():
    actor_add = {'name':request.json['name']}
    actors_list.update(actor_add)
    return jsonify(actors_list)

@app.route('/Assignment2.1/add_movie', methods=['POST'])
def add_movie():
    movie_add = {'name': request.json['name']}
    movies_list.update(movie_add)
    return jsonify(movies_list)

if __name__ == '__main__':
    app.run(port=8888, debug=True)