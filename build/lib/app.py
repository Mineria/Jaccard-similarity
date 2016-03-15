#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import math
from random import randint
import api as api

config = json.load(open('config.json')) # Loading configuration from file
rows = config['clients'] # Number of clientes
columns  = config['products'] # Number of products max
categories = config['categories'] # list with all the possible values for a product
categories_num = len(categories)
max_products_result = 10

def main():
    total_clients = rows
    total_products = columns

    clients  = api.init_clients(rows, categories_num, columns)
    products = api.init_products(total_products, categories)
    matrix   = api.init_random_matrix(total_clients, total_products, clients, categories_num)

    products_related  = api.get_related_products(matrix, rows, columns)

    print matrix[0]

    for index_user in range(0, 20):

        print "Recommendations for user %d" % index_user

        total_displayed_products = 0
        api.define_profile(clients[index_user]) # print informatio nabout the user
        recommendations = api.get_user_recommendations(index_user, products_related, matrix, rows, columns)

        for r in recommendations:
            if total_displayed_products >= max_products_result:
                break

            product_name = r[0]
            product_distance = r[1]
            accuracy = product_distance * 100

            if accuracy < 60:
                pass # don't recommend products with less than 50% of accuracy
            else:
                print "Product_id(" + str(product_name) + ") - Accuracy: " + str(int(product_distance * 100)) + "% | " + str(products[product_name])
                total_displayed_products += 1


        #get_user_preferred_category() # returns a list of the categories the user prefer (based on the probabilities for each category)

        if total_displayed_products == 0:
            print "¡Hola!. De momento no tienes productos recomendados"
            print "¿Qué te parece si le echas un vistazo a nuestra tienda?"
            print "Cuanto más compres, más productos únicos vas a encontrar ;)"
        print "-----------"
    #
    # for user_index in range(0, total_clients):
    #     print "---\n\nRecommendations for user %d are: " % user_index
    #     print api.define_profile(clients[0])
    #     print "\n"
    #     user_recommendations = api.get_user_recommendations(user_index, products_related, matrix, rows, columns)
    #     print user_recommendations
    #     total_products_displayed = 0
    #
    #     for r in user_recommendations:
    #         if total_products_displayed >= max_products_result:
    #             break
    #         product_name = r[0]
    #         product_distance = r[1]
    #         accuracy = product_distance * 100
    #         #print product_name
    #         if (accuracy < 50):
    #             pass # don't recommend products with less than 50% of accuracy
    #         else:
    #             total_products_displayed += 1
    #             print "Product: " + str(product_name) + ". Accuracy " + str(product_distance * 100) + "%"
    #             print "Type of product " + str(products[product_name])
    #
    #     #get_user_preferred_category() # returns a list of the categories the user prefer (based on the probabilities for each category)
    #
    #     if total_products_displayed == 0:
    #         print "¡Hola!. De momento no tienes productos recomendados"
    #         print "¿Qué te parece si le echas un vistazo a nuestra tienda?"
    #         print "Cuanto más compres, más productos únicos vas a encontrar ;)"
    #
    #
    #

    #







# from mynewmodule import hola
#hola.hola()


main()
