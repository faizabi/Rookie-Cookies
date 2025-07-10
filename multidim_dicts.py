'''Beginner Exercises
Create a multidimensional dictionary: 
Write a Python code snippet that creates a multidimensional dictionary with the following structure:
 {1: {'a': 1, 'b': 2}, 2: {'c': 3, 'd': 4}}. 
Expected output: A multidimensional dictionary with the specified structure.'''

mul_dix=dict([(1,{'a':1,'b':2}),(2,{'c':3,'d':4})])
print(mul_dix)

'''Access a value in a multidimensional dictionary: 
Write a Python code snippet that accesses the value associated with the key a in the multidimensional dictionary 
{1: {'a': 1, 'b': 2}, 2: {'c': 3, 'd': 4}}. Expected output: 1.'''

print(mul_dix[1]['a'])

'''Intermediate Exercises
Update a value in a multidimensional dictionary: 
Write a Python code snippet that updates the value associated with the key b in the multidimensional dictionary 
{1: {'a': 1, 'b': 2}, 2: {'c': 3, 'd': 4}} to 3. 
Expected output: A multidimensional dictionary with the updated value.'''

mul_dix[1]['b']=3
print(mul_dix)

'''Add a new key-value pair to a multidimensional dictionary: 
Write a Python code snippet that adds a new key-value pair e: 5 to the multidimensional dictionary 
{1: {'a': 1, 'b': 2}, 2: {'c': 3, 'd': 4}} in the inner dictionary with key 1. 
Expected output: A multidimensional dictionary with the added key-value pair.'''
mul_dix[1].update({'e': 5})
print
# or alternatively to replace the inner dictionary
mul_dix[1] = {'e': 5}

print(mul_dix)

'''Advanced Exercises

Corporate Real-time Scenario: 
Employee Data: Write a Python code snippet that represents employee data as a multidimensional dictionary with the following structure: 
{employee_id: {'name': employee_name, 'department': employee_department, 'salary': employee_salary}}. 
Then, write a function that updates the employee's salary by a certain percentage. 
The function should take the employee's ID and the percentage as input. 
Expected output: A multidimensional dictionary with the updated salary value.'''

# employee_ID=int(input("Enter employee ID: "))
sal_percent=float(input("Enter salary percentage: "))   

emp_data=dict([('emp_ID',{'name':'John Doe','dept':'Engineering','salary':50000})])
print(emp_data)
def sal_change(emp_data, sal_percent):
    emp_data['emp_ID'].update({'salary': round(emp_data['emp_ID']['salary'] * (1 + sal_percent / 100))})
    return emp_data
print(f"With salary increment of {sal_percent}%, the employee data with updated salary is:\n", sal_change(emp_data, sal_percent))


