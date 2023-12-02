## Bài 1
class Contact:
  def __init__(self, name, phone_number, email):
    self.name = name
    self.phone_number = phone_number
    self.email = email
  
  def __str__(self):
    return f"{self.name} - {self.phone_number} - {self.email}"

class Phonebook:
  def __init__(self):
    self.contact = []
    
  def add_contact(self, contact):
    self.contact.append(contact)
    print(f"Contact {contact.name} added successfully.")
  
  def remove_contact(self, name):
    for contact in self.contact:
      if contact.name == name:
        self.contact.remove(contact)
        print(f"Contact {contact.name} removed successfully.")
        return self.contact 
      print(f"Contact {name} is not in contact list.")

  def display_contact(self):
    if not self.contact:
      print("Phone book is empty.")
    else:
      print("Contacts in the phone book:")
      for contact in self.contact:
        print(contact)

  def search_contact(self, name):
    for contact in self.contact:
      if contact.name == name:
        print("Contact found: " + contact)
        return self.contact
      else:
        print(f"Contact {name} is not in contact list.")

phone_book = Phonebook()

contact_1 = Contact("A", "0975.210.226", "A@gmail.com")
contact_2 = Contact("B", "0909.091.691", "B@gmail.com")

phone_book.add_contact(contact_1)
phone_book.add_contact(contact_2)

phone_book.display_contact()

phone_book.search_contact(contact_1)
phone_book.search_contact(contact_2)

phone_book.remove_contact(contact_1)
phone_book.remove_contact(contact_2)

## Bài 2
# class Employee:
#   def __init__(self, name, age, salary):
#     self.name = name
#     self.age = age
#     self.salary = salary
#   def display(self):
#     print(f"{self.name} - {self.age} - {self.salary}VND")
#   def calculate_bonus(self):
#     return self.salary / 10

# class Manager(Employee):
#   def __init__(self, name, age, salary, department):
#     super().__init__(name, age, salary)
#     self.department = department
#   def display(self):
#     super().display()
#     print(f"Department: {self.department}")
  
# class Engineer(Employee):
#   def __init__(self, name, age, salary, specialization):
#     super().__init__(name, age, salary) 
#     self.specialization = specialization
#   def display(self):
#     super().display()
#     print(f"Specialization: {self.specialization}")
    
# def main():
#   employees = [
#     Manager("A", 35, 10000000, "IT"),
#     Engineer("B", 28, 7000000, "IT"),
#     Engineer("C", 25, 6000000, "IT"),
#   ]

#   print("Employee information:")
#   for employee in employees:
#     employee.display()
  
#   print("Bonus:")
#   for employee in employees:
#     bonus = employee.calculate_bonus()
#     print(f"{employee.name} bonus: {bonus}VND")
  
# main()