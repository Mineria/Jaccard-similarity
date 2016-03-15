import clients as clients
import products as products
import matrix_methods as matrix_methods

### Initializers
def init_clients(row_clients, categories_number, column_books):
    return clients.init_clients(row_clients, categories_number, column_books)

def init_products(total_products, categories):
    return products.init_products(total_products, categories)

def init_random_matrix(rows, columns, users, numb_categories):
    return matrix_methods.init_random_matrix(rows, columns, users, numb_categories)

def get_related_products(matrix, row, column):
    return matrix_methods.get_related_products(matrix, row, column)

def display_matrix(matrix, rows, columns):
    matrix_methods.display_matrix(matrix, rows, columns)

def display_products(products_list):
    products.display_all_products(products_list)

def get_user_recommendations(user_index, related_products_distance, matrix, rows, columns):
    return matrix_methods.get_user_recommendations(user_index, related_products_distance, matrix, rows, columns)

def define_profile(user):
    clients.define_profile(user)
