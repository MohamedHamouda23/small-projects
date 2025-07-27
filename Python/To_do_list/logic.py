from validation import Validator
import csv

class Task(Validator):
        def __init__(self,task,priority,due,category,mark):

            self.task=task
            self.priority=priority
            self.due=due
            self.category=category
            self.mark=mark

        def __str__(self):
                  return f"Task: {self.task}, Priority: {self.priority}, Due: {self.due}, Category: {self.category},mark: {self.mark}"

    
        def add(self):

              with open("task_managment.csv", "a", newline='') as manage:
                  writer = csv.writer(manage)
                  writer.writerow([self.task, self.priority, self.due, self.category, self.mark])
                  
              print("\033c", end="")
              print(f"Task '{self.task}' removed successfully")


        def remove(task, category):
            header, data_rows, _ = Task._read_csv()
            updated_tasks = [header]

            for row in data_rows:
                if len(row) < 4:
                    updated_tasks.append(row)
                    continue

                if not (row[0].lower() == task.lower() and row[3].lower() == category.lower()):
                    updated_tasks.append(row)

            Task._write_csv(updated_tasks)
            print("\033c", end="")
            print(f"Task '{task}' removed successfully")


        def completed(task_name, category):
            header, data_rows, _ = Task._read_csv()
            saved_row = None
            updated_tasks = [header]  

            for row in data_rows:
                if len(row) < 5:  
                    continue
                if row[0].lower() == task_name.lower() and row[3].lower() == category.lower():
                    saved_row = row
                    print(f"Current Mark: {row[4]}")
                    break

            if saved_row:
                current_status = saved_row[4].lower()
                new_status = "uncompleted" if current_status == "completed" else "completed"
                
                choice = input(f"Do you want to mark this task as '{new_status}'? (yes/no): ").lower()

                if choice == "yes":
                    updated_tasks = [header]
                    for row in data_rows:
                        if len(row) < 5:
                            updated_tasks.append(row)
                            continue
                        if row[0].lower() == task_name.lower() and row[3].lower() == category.lower():
                            row[4] = new_status
                        updated_tasks.append(row)

                    Task._write_csv(updated_tasks)
                    print("\033c", end="")
                    print(f"Task '{task_name}' marked as {new_status}.")
                else:
                    print("Status change cancelled.")
            else:
                print(f"Task not found.")