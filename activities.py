student_list = []
def collect_info():
   dictionary = {}
   id = input("User ID: ")
   name = input("User Name: ")
   gender = input("User Gender: ")
   age = input("User Age: ")
   dictionary["id"]= id
   dictionary["name"]= name
   dictionary["gender"]= gender
   dictionary["age"]= age
       
   student_list.append(dictionary)
  
for users in range(10):
   collect_info()

# drop a user
# def drop_student(student_list):
#    id_to_drop = input("Enter the ID to drop from the Student List : ") 
#    for student in student_list:
#       if student.get("id") == id_to_drop:
#          student_list.remove(student)
#          print("ID successfully removed")
#          return
#       print("ID not found in the List")


# print("Initial List", student_list)
# drop_student(student_list)
# print("Updated List: ", student_list)