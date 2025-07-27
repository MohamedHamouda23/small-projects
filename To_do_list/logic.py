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
                if not (row[0] == task and row[3] == category):
                    updated_tasks.append(row)
                    

            Task._write_csv(updated_tasks)
            print("\033c", end="")
            print(f"Task '{task}' removed successfully")


        def completed(task_name, category):
            _, data_rows, _ = Task._read_csv()
            saved_row = None

            for row in data_rows:
                if row[0] == task_name and row[3] == category:
                    saved_row = row
                    print(f" current Mark:     {row[4]}")
                    break

            if saved_row:
                new_status = "uncomplete" if saved_row[4].lower() == "completed" else "completed"
                choice = input(f"Do you want to mark this task as '{new_status}'? (yes/no): ").lower()

                if choice == "yes":
                    header, data_rows, _ = Task._read_csv()
                    updated_tasks = [header]

                    for row in data_rows:
                        if row == saved_row:
                            row[4] = new_status

                        updated_tasks.append(row)

                    Task._write_csv(updated_tasks)
                    print("\033c", end="")
                    print(f"Task '{task_name}' marked as {new_status}.")

