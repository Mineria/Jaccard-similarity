#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import math
from random import randint


"""
Returns a list of length max_categories, where each of the elements
is the probability that a user has to buy a product of category i
"""

def create_random_probabilities(list_size):

    total = 0
    const_prob = 0.2 # Add in each iteration a constant value of probability until 1.
    probability = [0]*list_size

    while (total + const_prob) <= 1:
        total += const_prob
        rand_index = randint(0,list_size-1);
        probability[rand_index] += const_prob

    return probability



def generate_user_purchases(user_purchases, total_products, categories, category_probability, total_categories):

    purchases = []
    category_range = total_products/total_categories

    for category_index in range(0, total_categories):

        i = 0
        starting_index_category = randint(0, products_per_category-1)
        products_per_category = int(math.ceil(category_probability[category_index] * user_purchases)) # calculate the number of products for each category user has

        while i < products_per_category:
            category_range
            purchases.append()
            i += 1

        print select_products_per_category
        #
        # print starting_index_category
        # print products_for_category
        # for i in products_for_category:
        #     starting_index_category = (starting_index_category + 1) % products_for_category
    print "\n"
    return purchases

def generate_user_categories_probability(max_categories):
    total = 0
    probability = [0]*max_categories
    constant_probability = 0.2 # Add in each iteration a constant value of probability until 1.

    while total + constant_probability <= 1:
        total += constant_probability
        index_random_category = randint(0, max_categories-1);
        probability[index_random_category] += constant_probability

    return probability

def create_user(name, categories, total_categories, total_books):

    total_user_purchases = randint(0, total_books-1)
    categories_probability = generate_user_categories_probability(total_categories)

    user = {
        'name' : name,
        'total_purchases' : total_user_purchases,
        'purchased_products' : generate_user_purchases(total_user_purchases, total_books, categories, categories_probability, total_categories),
        'purchased_products_total' : 0,
        'categories_probability' : categories_probability
    }
    return user

def generate_users(categories, max_categories, total_books):
    books = []
    for index in range(0, total_books):
        user = create_user(index, categories, max_categories, total_books)
        books.append(user)
    return books

def user_to_string(user):
    user_str = ""
    for key in user:
        user_str += (key + ": " + str(user[key]) + ' \n')
    user_str += "\n"
    return user_str

def display_all_users(users):
    for index, value in enumerate(users):
        print user_to_string(users[index])

def matchUserProducts(totalUser, totalProducts):
    products = generate_products(totalProducts);
    users = generate_users(totalUser)




#print generate_users(100)



""" Given a list of probabilities of a user
returns a list of M products randomly chosen
where M is the number of products a user has bought """
