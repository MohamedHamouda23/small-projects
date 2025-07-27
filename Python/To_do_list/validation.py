import csv

class CSVHandler:
            @staticmethod
            def _read_csv(filename="task_managment.csv"):
                try:
                    with open(filename, "r") as manage:
                        tasks = list(csv.reader(manage))
                    header = tasks[0]
                    data_rows = tasks[1:]
                except Exception as e:
                    print(f"Error reading CSV: {e}")
                    
                return header, data_rows, tasks
            
            @staticmethod
            def _write_csv(data, filename="task_managment.csv"):
                try:
           
                    with open(filename, "w", newline='') as manage:
                        writer = csv.writer(manage)
                        writer.writerows(data)
                except Exception as e:
                    print(f"Error reading CSV: {e}")
       
                    
                    
            @staticmethod
            def exists(task_name,category):
                    if not task_name or not category:
                        print(" Please provide both task name and category to remove.")
                        return False

                    try:
                        with open("task_managment.csv", "r") as manage:
                            reader = csv.reader(manage)
                            next(reader)  
                            for row in reader:
                                if len(row) < 4:
                                    continue
                                if row[0].lower() == task_name.lower() and row[3].lower() == category.lower():
    
                                    return True
                        return False
                    except FileNotFoundError:
                        return False


class Validator(CSVHandler):


    def validation(self):
        self.task = self.task.lower()
        self.priority = self.priority.lower()
        self.due = self.due.lower()
        self.category = self.category.lower()
        self.mark = self.mark.lower()
        if not all([self.task, self.priority, self.due, self.category, self.mark]):
            print("Please fill all the fields")
            return False

        if self.priority not in ["high", "medium", "low"]:
            print("Please enter a valid priority")
            return False

        if self.mark not in ["completed", "uncompleted"]:
            print("Please enter a valid mark")
            return False

        if self.category not in ["work", "home", "study"]:
            print("Please enter a valid category")
            return False

        if self.due not in ["today", "tomorrow", "this week", "this month"]:
            print("Please enter a valid due date")
            return False

        if  CSVHandler.exists(self.task, self.category):
            print("This task with the same category already exists.")
            return False

        return True
    
    