# using dictionaries for storing employee data
employee = {
  101: {
       "name":"Sabum",
        "age": "30", 
        "department": "IT"
        },
  102: {
       "name":"John",
        "age": "25", 
        "department": "HR"
        },
  103: {
    "name":"Alice",
    "age":"28",
    "department":"Finance"
  },
  104: {
    "name":"Bob",
    "age":"35", 
    "department":"Marketing"
}
}
# How to output the name, age and department of all the employees using a for loop
for emp_id,emp_data in employee.items():
      print(f"Employee ID:{emp_id},Name:{emp_data['name']},Age:{emp_data['age']},Department:{emp_data['department']}")
      
