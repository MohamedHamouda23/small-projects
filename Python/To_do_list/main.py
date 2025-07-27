from logic import Task 
import csv


def operations():
     task_name=input("\n\n Enter your task: ")
     category=input(" Enter your category: ")
     return task_name, category


def option(choice):

      if choice=="1":

          task_name, category = operations()
          priority=input(" Enter your priority: ")
          due=input(" Enter your due date: ")
          mark="uncompleted"

          The_task=Task(task_name,priority,due,category,mark)
          if The_task.validation():
              The_task.add()
              


      elif choice=="2":
          task_name, category = operations()
          if Task.exists(task_name, category):
              Task.remove(task_name, category)
          else:
              print(" Task not found. Cannot remove.")


      elif  choice=="3":
           task_name, category = operations()
           Task.completed(task_name,category)

      elif choice=="4":
          exit()


try:
     with open("task_managment.csv", "r") as manage :
        lines = manage.readline()
except FileNotFoundError:
        lines = []

if not lines:  
     with open("task_managment.csv", "w", newline='') as manage:
                 writer = csv.writer(manage)
                 try:
                  writer.writerow(["Task", "Priority", "Due", "Category", "Mark"])
                 except Exception as e:
                     print(f"Error writing to CSV: {e}")



while True:
  choice=str(input("\n\nwelcome in daily to do list.please choose the best option: \n\n 1- Add task (1) \n\n 2- Remove Task (2) \n\n 3- Mark task as completed (3)\n \n 3- exit (4)\n\n please select your option: "))
  option(choice)

