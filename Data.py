import json
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def remove_actor(list):
    """
    To remove actors list which actor's movie list is empty or the age is less than 0
    :param list: The array list that need to be modified
    :return: Return an array list that the actor with incomplete informations
    """
    for actor in list.keys():
        if((list[actor]['age'] <= 0) or (list[actor]['movies'] == [])):
            list.pop(actor, None)


def remove_movie(list):
    """
    To remove the movie list which has empty actor list or box_office is less than 0
    or the movie year is less than 0
    :param list:
    :return:
    """
    for movie in list.keys():
        if((list[movie]['box_office'] <= 0) or (list[movie]['actors'] == []) or (list[movie]['year'] <= 0)):
            list.pop(movie, None)

def add_actor_node_toGraph(graph):
    """
    Adding actor's name and information node to the graph
    :param graph: The graph of the node is going to add in
    :return: A graph with actors nodes
    """
    for actor in actors_list:
        graph.add_node(actor, attr_dic = actors_list[actor])

def add_movie_node_toGraph(graph):
    """
    Adding movie's name and information node to the graph
    :param graph: The graph of the node is going to add in
    :return: A graph with movies nodes
    """
    for movie in movies_list:
        graph.add_node(movie, attr_dic = movies_list[movie])

def add_edge_toGraph(graph):
    """
    To add edge with the actor node and movie node, if actor is in certain movie,
    add and edge in between
    :param graph: The graph of the edges is going to add in
    :return: A graph with edges
    """
    for node in graph.node():
        if(graph.node[node]['attr_dic']['json_class'] == 'Actor'):
            name = graph.node[node]['attr_dic']['name']
            for movie in movies_list:
                actors_movie = graph.node[movie]['attr_dic']['actors']
                if(name in actors_movie):
                    graph.add_edge(node, movie)


def find_hub(actor1_movies, actor2_movies, current_idx):
    """
    To find actor_1 has any common movie with actor_2
    :param actor1_movies: the list of movies from actor_1
    :param actor2_movies: the list of movies from actor_2
    :param current_idx: to check which actor_1 is checking the hub with other actors
    :return: return a list of common moive between actor_1 and actor_2
    """
    short_length = 0
    long_length = 0
    tmp_list1 = []
    tmp_list2 = []

    if(len(actor1_movies) < len(actor2_movies)):
        short_length = len(actor1_movies)
        long_length = len(actor2_movies)
        tmp_list1 = actor1_movies
        tmp_list2 = actor2_movies
    else:
        short_length = len(actor2_movies)
        long_length = len(actor1_movies)
        tmp_list1 = actor2_movies
        tmp_list2 =actor1_movies
    for i in range(0, short_length):
        count = 0
        for j in range(0, long_length):
            if(tmp_list1[i] == tmp_list2[j]):
                actors_common_movies[current_idx].append(tmp_list1[i])
                count = count + 1
            if(count > 0):
                break
        if(count > 0):
            break

def get_hub(list):
    """
    To find which actors has most hub
    :param list: The list of common movies of actors
    :return: a sorted array from most to fewest common movie numbers of actors
    """
    count = -1
    for i in range(0, len(list) - 1):
        if(count == -1):
            if(len(list[i + 1]) > len(list[i])):
                count = i
        else:
            if(len(list[i]) > len(list[count])):
                count = i
    top_actors_hub.append(actors_name[count])
    top_actors_hub_num.append(len(list[count]))
    list[count] = []
    return count


with open('data.json') as json_data:
    data_json = json.load(json_data)

# Global variables
actors_list = data_json[0]
movies_list = data_json[1]
actors_name = []
actors_common_movies = [[]for i in range(271)]
actors_hub = []

# Remove incomoplete acotrs and movies informations
remove_actor(actors_list)
remove_movie(movies_list)


# Graphing
Graph = nx.Graph()
add_actor_node_toGraph(Graph)
add_movie_node_toGraph(Graph)
add_edge_toGraph(Graph)
# nx.draw(Graph)
# plt.savefig("Graph.png")
# plt.show()

#========just for checking nodes output============================
# for n in Graph.node():
#     print("Node :" + str(n))
#     print("Attr :" + str(Graph.node[n]['attr_dic']['json_class']))
#==================================================================

for name in actors_list:
    actors_name.append(actors_list[name]['name'])

#To iterate through each actor's movie list
current = 0
while(current < len(actors_name)):
    list_one = []
    list_two = []
    current_actor = actors_name[current]
    # print(current_actor)
    for movies in actors_list:
        if(actors_list[movies]['name'] == current_actor):
            list_one = actors_list[movies]['movies']
        else:
            list_two = actors_list[movies]['movies']
        find_hub(list_one, list_two, current)
    current = current + 1



top_actors_hub = []
top_actors_hub_num = []
current_idx = 0
while(current_idx < len(actors_name)):
    get_hub(actors_common_movies)
    current_idx = current_idx + 1


#======to make x and y for plot same dimension=============
a = list(range(20))
x = np.array(a)
y = np.array(top_actors_hub_num[:20])
#===========================================================
my_xticks = top_actors_hub[:20]
fig, ax = plt.subplots()
plt.xticks(x, my_xticks)
plt.plot(x, y, 'ro')
ax.xaxis_date()
fig.autofmt_xdate()
plt.savefig("hub.png")
plt.show()
