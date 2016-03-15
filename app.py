#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import math
from random import randint
import api as api

config = json.load(open('config.json')) # Loading configuration from file
rows = config['clients'] # Number of clientes
columns = config['products'] # Number of products max
categories = config['categories'] # list with all the possible values for a product
categories_num = len(categories)

def main():
    total_clients = rows
    total_products = columns

    clients  = api.init_clients(rows, categories_num, columns)
    products = api.init_products(total_products, categories)
    matrix   = api.init_random_matrix(total_clients, total_products, clients, categories_num)

    print "[OK] Clients generated."
    print "[OK] Products randomly generated."
    print "[OK] Clients/products matrix."
    print "[WAITING]  Calculating related products..."

    related_products  = api.get_related_products(matrix, rows, columns)

    def display_recommendations(recommendations):
        products_displayed = 0
        max_products_result = 10 # maximum number of recommendations to show the user

        for r in recommendations:
            if products_displayed >= max_products_result:
                break

            product_name = r[0]
            product_id   = str(product_name)

            if len(product_id) <= 2:
                product_id = "0%s" % product_id
            product_distance = r[1]
            accuracy = product_distance * 100

            if accuracy < 60:
                pass # don't recommend products with less than 50% of accuracy
            else:
                print "\tid(" + str(product_id) + ") - Accuracy " + str(int(product_distance * 100)) + "% | " + str(products[product_name])
                products_displayed += 1

        if products_displayed == 0:
            print "\n\t¡Hola!. De momento no tienes productos recomendados"
            print "\t¿Qué te parece si le echas un vistazo a nuestra tienda?"
            print "\tCuanto más compres, más productos únicos vas a encontrar ;)"

    def display_users(max_users):

        max_users = total_clients if max_users > total_clients else max_users

        for index_user in range(0, max_users):

            print "-" * 80
            print "\tRecommendations for user %d \n" % index_user

            api.display_user_profile(clients[index_user]) # print informatio nabout the user

            print "\n\tRecommend products user:"
            recommendations = api.get_user_recommendations(index_user, related_products, matrix, rows, columns)
            display_recommendations(recommendations)

    display_users(10)

main()
