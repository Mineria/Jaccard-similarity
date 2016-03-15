#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

def init_products(total_products, categories):
    products = [0]*total_products
    number_categories = len(categories)
    offset = total_products / number_categories # products_per_category

    for cat_index in range(0, number_categories):
        for j in range (cat_index * offset, (cat_index * offset) + offset):
            products[j] = categories[cat_index]
    return products


# def init_products(n_products, categories, total_categories):
#     products = [0]*n_products # List with all the elements are 0
#     products_inserted = 0
#     products_per_category = n_products / total_categories
#     for index in range(0, total_categories):
#         offset = index * (products_per_category)
#         # print offset
#         for j in range(offset, offset + products_per_category):
#             product = {
#                 "type_of_product" : categories[index]
#                 #"categories_probability" : create_random_probabilities(total_categories)
#             }
#             # print categories[index]
#             products_inserted = products_inserted + 1
#             products[offset] = product
#             # print products
#     # print products
#     return products

def display_all_products(products):
    for index, value in enumerate(products):
        print value # print user_to_string(products[index])


#
# if __name__ == '__main__':
#     init_products(args[0], args[1], args[2])


# """
# Parameters:
# - products_type <List of string> | Contains the names of all categories
# - total_categories <Integer> | Number of all the categories we have
# - total_products <Integer> | Total number of products to be insert
# Return: List of N elements. Being N the total_products pass by parameter
# """
# def generate_products(products_type, total_categories, total_products):
#
#     products = []
#     products_per_category = total_products / total_categories
#
#     for i_category in range(0, total_categories):
#         category_name = products_type[i_category]
#         for j_product in range(0, products_per_category):
#             offset = j_product + ((i_category * products_per_category) + 1)
#             name = offset
#             product = {
#                 'name' : name,
#                 'category_name' : category_name,
#                 'related_books' : []
#             }
#             products.append(product)
#
#     return products
#
# def get_category_products(products, category_index, total_categories, total_products):
#     products_per_category = total_products / total_categories
#     offset = ((category_index * products_per_category))
#     print products_per_category
#     print offset
#     print "Category " + str(category_index)
#     for i in range(offset, offset + products_per_category):
#         print products[i]
#
# def display_all_products(products):
#     for index, value in enumerate(products):
#         # print user_to_string(products[index])
#         print value
