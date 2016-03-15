#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import floor
from random import randint
from operator import itemgetter
import json

config = json.load(open('config.json')) # Loading configuration from file
categories = config['categories'] # list with all the possible values for a product

def create_random_probabilities(n_categories):
    """Returns array of size n (total number of categories in the store) where each
    index is the probability the user buy a particular product category.
    Example: [0.3, 0.2, 0.2, 0.2, 0.1] == The user buy 30 percent of product A..."""

    category_total_probab  = 0 # store the total number of random number generated to all the categories
    category_probabilities = [0] * n_categories # array of ceroe's

    for i in range(0, n_categories): # Assigning random probabilities to each category
        if i == 3:
            category_total_probab += 100
            category_probabilities[i] = 100
        elif i == 2:
            category_total_probab += 50
            category_probabilities[i] = 50
        else:
            category_total_probab += 10
            category_probabilities[i] = 10

    for i in range(0, n_categories): # normalize probabilities
         category_probabilities[i] /= float(category_total_probab) # division with decimal

    return category_probabilities


def init_clients(total_clients, total_categories, maximum_products_number):
    """Returns a list of users with random number of purchased products and
    random probabilities for each shop category."""

    clients  = [0] * total_clients # List with all the elements are 0

    for index in range(0, total_clients):
        clients[index] = { # creating a new client
            "number_products" : randint(2, maximum_products_number/5),
            "categories_probability" : create_random_probabilities(total_categories)
        }

    return clients

def display_user_profile(user):
    """ given the user object(array of probabilities + number of bought articles) """
    global categories

    products = user['number_products']
    probabilities = user['categories_probability']
    first_maximum = 0

    def get_maximum(prob):
        return prob.index(max(prob))

    def get_second_maximum(prob, first_maximum_index):
        copy_max_prob = prob[first_maximum_index]
        prob[first_maximum_index] = 0 # remove to get the second higher
        second_max = prob.index(max(prob))
        prob[first_maximum_index] = copy_max_prob
        return second_max

    max_category = get_maximum(probabilities)
    second_max_category = get_second_maximum(probabilities, max_category)

    print "\tTotal bought products: " + str(user['number_products'])
    print "\n\tCategory probabilities:"
    for key, value in enumerate(user['categories_probability']):
        cat_str = "\t" + str(categories[key]) + ": " + str(int(value*100)) + "%"
        print cat_str
        #print "\t" + str(categories[key]) + str(categories[value])

    print "\n\tTop user categories (more bought products)"
    print "\t#1 category: " + str(categories[max_category])
    print "\t#2 category: " + str(categories[second_max_category])
