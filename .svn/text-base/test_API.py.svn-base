import json
import API
import app
import unittest
from flask import Flask
from flask_testing import TestCase

#source from https://www.youtube.com/watch?v=APbPtQg3_04

class apiTest(unittest.TestCase):

    def setUp(self):
        API.app.config['Testing'] = True
        self.app = API.app.test_client()

#===============Get test======================
    def test_filter_actor(self):
        result = self.app.get('/Assignment2.1/actors/Bruce')
        list = json.loads(result.get_data(as_text=True))
        actor_list = list[0]
        for actor in actor_list:
            assert('Bruce' in actor_list[actor]['name'])

    def test_filter_age(self):
        result = self.app.get('/Assignment2.1/actors_age/61')
        list = json.loads(result.get_data(as_text=True))

        for i in range(0, len(list)):
            for actor in list[i]:
                assert(61 == list[i][actor]['age'])


    def test_filter_acter_gross(self):
        result = self.app.get('/Assignment2.1/actors_gross/110530008')
        list = json.loads(result.get_data(as_text=True))

        for i in range(0, len(list)):
            for actor in list[i]:
                assert(110530008 == list[i][actor]['total_gross'])

    def test_filter_movie(self):
        result = self.app.get('/Assignment2.1/movies/Midnight Cowboy')
        list = json.loads(result.get_data(as_text=True))
        actor_list = list[0]
        for actor in actor_list:
            assert('Midnight Cowboy' in actor_list[actor]['movies'])

    def test_filter_movie_actor(self):
        result = self.app.get('/Assignment2.1/movie_actor/Bruce Willis')
        list = json.loads(result.get_data(as_text=True))
        movie_list = list[0]
        for movie in movie_list:
            assert('Bruce Willis' in movie_list[movie]['actors'])

    def test_filter_year(self):
        result = self.app.get('/Assignment2.1/movie_year/1988')
        list = json.loads(result.get_data(as_text=True))

        for i in range(0, len(list)):
            for movie in list[i]:
                assert(1988 == list[i][movie]['year'])

    def test_filter_movie_gross(self):
        result = self.app.get('/Assignment2.1/movie_gross/36')
        list = json.loads(result.get_data(as_text=True))

        for i in range(0, len(list)):
            for movie in list[i]:
                assert(36 == list[i][movie]['box_office'])

#===============delete test======================

    def delete_actor(self):
        result = self.app.delete('/Assignment2.1/actor_del/Bruce Willis')
        list = json.loads(result.get_data(as_text=True))
        for actor in list:
            assert('Bruce Willis' != list[actor]['name'])

    def delete_movie(self):
        result = self.app.delete('/Assignment2.1/movie_del/The Drowning Pool')
        list = json.loads(result.get_data(as_text=True))
        for movie in list:
            assert('The Drowning Pool' != list[movie]['name'])

if __name__ == '__main__':
    unittest.main()