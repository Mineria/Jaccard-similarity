#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from random import randint
from operator import itemgetter

""" Returns a matrix with dimensions row*column.
    Each element of the matrix can be 0 or 1.
    0 = product bought by client | 1 = product not bought by client.
    The column is the product and the row is each of the client."""

def init_random_matrix(rows, columns, users, numb_categories):
    matrix = [[ 0 for c in range(columns) ] for r in range(rows) ] # Build multidimensional matrix with Columns*Rows
    total_products = columns
    total_clients = rows

    products_per_category = total_products / numb_categories

    for user_index in range(0, total_clients):
        # print "------"
        # print "User " + str(user_index)
        # print users[user_index]
        for category_index in range(0, numb_categories):

            left   = category_index * products_per_category
            offset = (category_index * products_per_category) + products_per_category

            cat_prob = users[user_index]['categories_probability'][category_index]
            cat_total_produts = users[user_index]['number_products']
            products_for_category = int(cat_prob * cat_total_produts)
            # 
            # print "---------------------------------------"
            # print "Valores de usuario"
            # print " valor left: " + str(left)
            # print " valor offset: " + str(offset)
            # print " valor cat_prob: " + str(cat_prob)
            # print " valor products_for_category: " + str(products_for_category)
            # print users[user_index]
            # print "---------------------------------------"

            start_position = randint(left, offset-1)
            position = start_position

            for n in range(0, products_for_category):
                matrix[user_index][position-1] = 1
                if position + 1 > offset:
                    position = left
                else:
                    position += 1
            #
            # total_inserted = 0
            # try_to_insert = 0
            # start_rand = randint(left, offset-1) % products_per_category
            # # print "rand" + str(start_rand)
            #
            # while total_inserted < products_for_category and try_to_insert < products_per_category:
            #     rand_category = left + randint(left, offset-1)
            #     print "Valor rand_category" + str(rand_category)
            #     if matrix[user_index][rand_category] == 0:
            #         matrix[user_index][rand_category] = 1
            #         total_inserted += 1
            #     else:
            #         pass # hit. Recompute in the next round
            #     try_to_insert += 1
            #
            # for i in range(0, products_for_category):
            #     try:
            #         matrix[user_index][start_rand] = 1
            #     except:
            #         print "---------------------------------------"
            #         print "---------------------------------------"
            #         print "---------------------------------------"
            #         print "---------------------------------------"
            #         print "---------------------------------------"
            #         print "---------------------------------------"
            #         print "ERROR EN EL FOR"
            #         print " valor start_rand: " + str(start_rand)
            #         print " valor user_index: " + str(user_index)
            #         print " valor left: " + str(left)
            #         print " valor offset: " + str(offset)
            #         print users[user_index]
            #         print "---------------------------------------"
            #         print "---------------------------------------"
            #         print "---------------------------------------"
            #         print "---------------------------------------"
            #     if start_rand + 1 > offset:
            #         start_rand = left
            #     else:
            #         start_rand += 1
        #
        # print matrix[user_index]

            # print cat_prob
            # print cat_total_produts
            # print "--te" + str(products_for_category)

            #print matrix[user_index][0]
            # pass
            #
            # category_probability = users[user_index]['categories_probability']
            # category_total_boughts = users[user_index]['number_products']
            # # print category_probability
            # # print category_total_boughts
            # total_products_to_insert = int(category_probability[category_index] * category_total_boughts)
            # # print int(total_products_to_insert)
            #
            # left_limit  = product_index * products_per_category
            # right_limit = (product_index * products_per_category) + products_per_category
            #
            # random_start = randint(0, products_per_category-1) %  products_per_category
            # next_index   = left_limit + random_start # defines when we start
            #
            # # Insert the total number of products a client has per each category
            # for total_inserted_products in range(0, total_products_to_insert):
            #     matrix[user_index][random_start] = 1 # product bought
            #     if next_index + 1 > right_limit:
            #         next_index = left_limit # restart index to left limit
            #     else:
            #         next_index += 1

    return matrix
#
# def init_random_matrix(products, clients, row_clients, column_products):
#     matrix = [[ 0 for c in range(column_products) ] for r in range(row_clients) ] # Build multidimensional matrix with Columns*Rows
#
#     for column in range(0, column_products):
#         columnStr = ""
#         for row in range(0, row_clients):
#             matrix[row][column] = randint(0, 1) # 0= not bought | 1= bought
#             columnStr +=  "_" + str(matrix[row][column]) + "_ "
#         #print columnStr
#
#     return matrix

""" Given a Matrix, returns a dictionary where each key
    is the element and the value are an array of elements
    that has higher distance with the key.

    distance(A,B) = |(A intersection B)| / |A u B|
    Higer distance between 2 products mean that costumers who
    buy product A, will like product B."""

def get_related_products(matrix, row, column):
    distances = {
        # each key is the column index.
        # and the value associate with dat key,
        # is the array of tuples (column, distanced) ordered from higher distance to lower.
    }

    print "[ Calculating related products... ]"

    def distance(columnA, columnB):
        intersection = 0.0 # products where both colums are 1. That means the user has bought the 2 products
        union = 0.0 # number of products that the costumer has bought

        # intersection A / B
        for r in range(0, row):
            if (matrix[r][columnA] == 1) and (matrix[r][columnB] == 1):
                intersection += 1
            if (matrix[r][columnA] == 1) or (matrix[r][columnB] == 1):
                union += 1

        if (intersection and union) == 0:
            return 0
        return intersection / union # hits (products they have in commun) / union

    for currentColumn in range(0, column):
        A = currentColumn
        A_related_products = []
        for j in range(0, column):
            if A != j:
                B = j
                distanceAB = distance(A, B)
                column_distance = ( j, distanceAB )
                A_related_products.append(column_distance)
        distances[currentColumn] = sorted(A_related_products,key=itemgetter(1), reverse=True)

    print "[ Related products calculated. Thanks for your patience! ;) ]"
    return distances


def get_user_recommendations(user_index, related_products_distance, matrix, rows, columns):

    debug = False

    def get_pucharsed_product(user_index):
        purchased_products = []
        for c in range(0, columns):
            if matrix[user_index][c] == 1:
                purchased_products.append(c) # add the column index

        print "Purchased products: " + str(purchased_products)
        return purchased_products

    # calculate related products for the user
    purchased_list = get_pucharsed_product(user_index)
    total_purchases = len(purchased_list)
    products_to_recommend = {
        # "product_index" : "distance"
    }

    for i in range(0, total_purchases):
        product_column = purchased_list[i]
        related_products_i = related_products_distance[product_column]

        if debug: print "----------------"
        if debug: print "Related products"
        if debug: print "----------------"

        if debug: print "\n"
        if debug: print related_products_i
        if debug: print "\n"

        # traverse related products
        for product in related_products_i:

            if debug: print "\n- Product: " + str(product)

            index_product = product[0]
            product_distance_to_i = product[1]

            if debug: print "\tIndex: " + str(index_product)
            if debug: print "\tDistance to i: " + str(product_distance_to_i)

            if index_product in purchased_list: # get tuple first element (product index)
                if debug: print "\t\t(YES) The user has purchased this object. So don't recommend it again"
                pass
            else:

                if debug: print "\t\t(NOP) The user has not bought this product. we should recommend it"
                if debug: print "\t\t     Check if the product is on the final recommendation list"

                if index_product in products_to_recommend:
                    if debug: print "\t\t\t(YES) The product is on the recommendation list."
                    if debug: print "\t\t\t      Check if the current product has greater distance the that previous element"
                    if product_distance_to_i > products_to_recommend[index_product]:
                        if debug: print "\t\t\t\t(YES) New distance is greater than previous one."
                        products_to_recommend[index_product] = product_distance_to_i
                    else:
                        if debug: print "\t\t\t\t(NOP) Previous distance is greater. So leave it."
                else:
                    if debug: print "\t\t\t(NO) The product is NOT on the recommendation list. So add it"
                    products_to_recommend[index_product] = product_distance_to_i
            if debug: print "-------------------------"
        if debug: print products_to_recommend
        if debug: print "---"


    convert_to_tuple = [(key, value) for key, value in products_to_recommend.iteritems()]
    convert_to_tuple.sort(key=itemgetter(1), reverse=True) # higher distance first on the tuple

    return convert_to_tuple








    #
    #
    # def get_user_bought_products(user_index):
    #     products = []
    #     for product_index in range(0, columns):
    #         if matrix[user_index][product_index] == 1:
    #             products.append(product_index)
    #     return products
    #
    # def get_user_recommend_products(users_products, products_distances):
    #     recommend_products = []
    #     for product_index in users_products:
    #         print products_distances[product_index]
    #
    #     return recommend_products
    #
    # print "FUNCTION "
    # user_bought_products = get_user_bought_products(user_index)
    #
    # print "user_bought_products "
    # print user_bought_products
    #
    # user_recommend_products = get_user_recommend_products(user_bought_products, related_products_distance)
    #
    # print user_recommend_products
    # return user_recommend_products
#
# def recommend_products(user_index, matrix, related_products_with_distance, rows, columns):
#
#     print "Related"
#     print related_products_with_distance
#
#     def get_user_bought_products(user_index):
#         bought_products = []
#         for product_column in range(0, columns):
#             if matrix[user_index][product_column] == 1:
#                 bought_products.append(product_column)
#         return bought_products
#
#     def get_related_products_ordered_by_distance(related_products_with_distance):
#         #related_tuple = [(k, v) for k, v in related.iteritems()]
#
#         print related_products_with_distance
#         print "---"
#         return ''
#         # related = related_products_with_distance
#         # related.sort(key=itemgetter(1), reverse=True)
#         # return related
#
#         # for product_key in user_products:
#         #     related_products_distance = related_products_with_distance[product_key]
#         #     print related_products_distance
#         #
#         #     for r in related_products_distance:
#         #         print r
#         #         product_id_key = r[0]
#         #         product_new_distance = r[1]
#         #
#         #         if product_id_key in related:
#         #             if related[product_id_key] < product_new_distance:
#         #                 related[product_id_key] = product_new_distance
#         #         else:
#         #             related[product_id_key] = product_new_distance
#         #
#         #         # Si el producto no es el mismo que tiene el usuario
#         #         # y además, tampoco está en related, meterlo
#         #
#         #     # print product_key
#         #     #
#         #     #     new_distance = products[product_key]
#         #     #     if (related[product_key] < new_distance):
#         #     #         related[product_key] = new_distance # Found an object with same name and greater ditance
#         #     # else:
#         #     #     related[product_key] = products[product_key]  # Add new key
#
#         return related_tuple
#
#     #user_products = get_user_bought_products(user_index)
#     #related_products = related_products_with_frecuency(user_products, related_products_with_distance)
#     related_products = get_related_products_ordered_by_distance(related_products_with_distance)
#
#     # Para cada producto quel usuario ha comprado, tenemos que ver cuales son los productos relacionados.
#     # Para cada producto relacionado:
#     #   Si el usuario lo ha compradol, entonces no lo mete
#     #   Si no lo ha comprado, lo metemso en un dictionario con su distancia.
#     #       Si al meterlo en el dictionario, el valor de la distancia es mayor que el que había, lo metemso
#     print related_products
#     print "-----"
#     return related_products

def display_matrix(matrix, rows, columns):
    print "-----------------------------"
    print "---------- MATRIX -----------"
    print "-----------------------------"
    for row in range(0, rows):
        print matrix[row]
    #
    #
    # for column in range(0, columns):
    #     columnStr = ""
    #     for row in range(0, rows):
    #         columnStr +=  "_" + str(matrix[row][column]) + "_ "
    #     print columnStr
#
# print [[ 0 for i in range(1) ] for j in range(30)]
# table= [ [ 0 for i in range(6) ] for j in range(6) ]
# print table
