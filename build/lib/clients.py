#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import floor
from random import randint
from operator import itemgetter


#### VERSIÓN TRUCADA PARA QUE SALGA MÁS DEL TIPO 3

def create_random_probabilities(n_categories):
    total = 0
    probability = [0]*n_categories

    # Calculate a random number for each category
    for i in range(0, n_categories):
        if i == 3:
            probability[i] = 100
            total += 100
        elif i == 2:
            probability[i] = 50
            total += 50
        else:
            probability[i] = 10
            total += 10

    # Normalize all the indexes
    for i in range(0, n_categories):
        probability[i] /= float(total) # division with decimal

    return probability


""" Returns an array of size "n" where each of the elements
    represents the probability that the user purchased
    the different type of products.
    Example: [ 0.1, 0.2, 0.7 ] """

#
# def create_random_probabilities(n_categories):
#     total = 0
#     probability = [0]*n_categories
#
#     # Calculate a random number for each category
#     for i in range(0, n_categories):
#         probability[i] = randint(0, 100)
#         total += probability[i]
#
#     # Normalize all the indexes
#     for i in range(0, n_categories):
#         probability[i] /= float(total) # division with decimal
#
#     return probability



# def create_random_probabilities(n_categories):
#     total = 0
#     const_prob = 0.2 # Add in each iteration a constant value of probability until 1.
#     probability = [0]*n_categories
#
#     while (total + const_prob) <= 1:
#         total += const_prob
#         rand_index = randint(0,n_categories-1);
#         probability[rand_index] += const_prob
#
#     if total < 1:
#         difference = 1 - total # number to obatin 1 suming all the array elements
#         probability[randint(0, n_categories-1)] += difference # add the difference to a random index
#
#     return probability

""" Given the number of clients (n_clients), the total number of products (total_products)
    and the number of categories the system admits,
    returns a list where each element is a dictionary.
    client:
    - purchased_products (int) = total number of purchases made by the user (0 <= n <= max_allowed_products)
    - categories_probability (list) = list where each element is the probability the user has bought the given type of product
    """

def init_clients(total_clients, total_categories, maximum_products_number):
    clients  = [0]*total_clients # List with all the elements are 0
    for index in range(0, total_clients):
        client = {
            "number_products" : randint(0, maximum_products_number-1),
            "categories_probability" : create_random_probabilities(total_categories)
        }
        clients[index] = client

    return clients

def display_all_clients(clients):
    for index, value in enumerate(clients):
        print "Client: " + str(index)
        print value
        print "----"


""" given the user object(array of probabilities + number of bought articles) """
def define_profile(user):

    print user

    products = user['number_products']
    probabilities = user['categories_probability']
    first_maximum = 0

    categories = [
    "sport",
    "science",
    "film",
    "informatic",
    "politic"
  ]

    def get_maximum(prob):
        return prob.index(max(prob))

    def get_second_maximum(prob, first_maximum_index):
        copy_max_prob = prob[first_maximum_index]
        prob[first_maximum_index] = 0 # remove to get the second higher
        second_max = prob.index(max(prob))
        prob[first_maximum_index] = copy_max_prob
        return second_max

    maximum = get_maximum(probabilities)
    second_maximum = get_second_maximum(probabilities, maximum)

    def create_table():
        str = ""

        max_elemn = maximum
        second_maximum = second_maximum

        elemns = [ max_elemn, second_maximum ]


        for n in range(9, 2):
            str += "|"
            i = 0
            while i < 15:
                if i <= len(max_elemn):
                    str += elemns[n][i]
                else:
                    str += " "
            i = 0
            while i < 15:
                if i <= len(max_elemn):
                    str += elemns[n][i]
                else:
                    str += " "

    print "\n"
    print "Favorite category: " + "(" + str(probabilities[maximum]) + "): " + categories[maximum]
    print "Second favorite category: " + "(" + str(probabilities[second_maximum]) + "): " + categories[second_maximum]
    print "\n"
