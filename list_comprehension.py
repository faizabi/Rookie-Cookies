'''Exercise 1: Basic List Comprehension
Create a list of squares of numbers from 1 to 5 using list comprehension.
Output: [1, 4, 9, 16, 25]'''

list_sq=[i**2 for i in range(1,6)]
print(list_sq)

'''Exercise 2: List Comprehension with If Condition
Create a list of even numbers from 1 to 10 using list comprehension with an if condition.
Output: [2, 4, 6, 8, 10]'''

list_if=[i for i in range(1,11) if i%2==0]
print(list_if)

'''Intermediate Exercises
Exercise 3: Multi-Dimensional List Comprehension
Create a 3x3 matrix of numbers from 1 to 9 using list comprehension.
Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''

list_matx=[[i*3 + j - 3 + 1 for j in range(0,3)] for i in range(1,4)]
print(list_matx)

'''Exercise 4: Real-Time Use Case - Filtering Data
Suppose you have a list of user data, and you want to filter out users who are inactive (status = 0). Use list comprehension to create a new list of active users.
Input: users = [{'name': 'John', 'status': 1}, {'name': 'Jane', 'status': 0}, {'name': 'Bob', 'status': 1}]
Output: [{'name': 'John', 'status': 1}, {'name': 'Bob', 'status': 1}]'''

list_stats=[i for i in [{'name': 'John', 'status': 1}, {'name': 'Jane', 'status': 0}, {'name': 'Bob', 'status': 1}] if i['status']==1]
print(list_stats)

'''Advanced Exercises
Exercise 5: Real-Time Use Case - Data Transformation
Suppose you have a list of sales data, and you want to transform it into a dictionary where the keys are the product names and the values are the total sales.
Input: sales_data = [{'product': 'Product A', 'quantity': 10, 'price': 20}, {'product': 'Product B', 'quantity': 5, 'price': 30}, {'product': 'Product A', 'quantity': 15, 'price': 20}]
Output: {'Product A': 200, 'Product B': 150}'''

sales_data = [{'product': 'Product A', 'quantity': 10, 'price': 20}, {'product': 'Product B', 'quantity': 5, 'price': 30}, {'product': 'Product A', 'quantity': 15, 'price': 20}]
total_sales={i['product']:i['quantity']*i['price'] for i in sales_data}


# total_sales = {}
# for item in sales_data:
#     product = item['product']
#     total = item['quantity'] * item['price']
#     if product in total_sales:
#         total_sales[product] += total
#     else:
#         total_sales[product] = total
print(total_sales)


'''Corporate Real-time Scenario: User Profile Management: Write a Python code snippet that represents a user profile as
 a dictionary with the following keys: username, email, phone_number, address, interests.
 Then, write a function that updates the user's profile by adding a new interest. 
 The function should take the user's username and the new interest as input.
 Output: {
    'username': 'john_doe',
    'email': 'johndoe@example.com',
    'phone_number': '123-456-7890',
    'address': '123 Main St',
    'interests': ['reading', 'hiking', 'coding', 'gaming']
}'''

dict={
    'username': 'john_doe',
    'email': 'johndoe@example.com',
    'phone_number': '123-456-7890',
    'address': '123 Main St',
    'interests': ['reading', 'hiking', 'coding', 'gaming']
}
username=input("Enter username: ")
new_interest=input("Enter new interest: ")
def update_profile(dict, username, new_interest):
    '''Function to update user profile by adding a new interest'''
    if dict['username'] == username:
        if new_interest not in dict['interests']:
            dict['interests'].append(new_interest)
    return dict
print(update_profile(dict, username, new_interest))

