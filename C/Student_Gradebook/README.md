# 🏆 Student Grade Manager program

A beginner-friendly **C** program to **add students**, **record grades**, **check highest & lowest marks**, and **determine pass/fail** status, using a simple text file (`student.csv`) to store all student records.


## 🧠 Features

- ✅ Add new students with their grades for Math, Physics, Biology, and Chemistry  
- 🔍 Check a student’s highest and lowest grades by ID  
- 🛡️ Validate inputs for student names and grades (grades between 0-100)  
- ✏️ Calculate letter grades based on average marks (A-F scale)  
- 🎯 Avoid invalid or duplicate IDs with ID validation  
- 📁 Store and read all records in a simple CSV text file


## 📸 Screenshots

### 📂 Student Data File (CSV)  
![Student CSV](assets/grades_file.png)

### ➕ Adding a New Student  
![Add Student](assets/Adding.png)

### 🔍 Searching Student Grades: Highest and Lowest
![Grade Range](assets/Grade%20Range.png)

### ✅ Pass/Fail Check  
![Pass Fail](assets/Outcome.png)


## 🚀 How to Run

Follow these steps to compile and run the program:

1. 🖥️ **Open your terminal or command prompt.**

2. 📂 **Navigate to the `app` folder** where the source code (`main.c`) is located:

   ```bash
   cd app
   ```
3. 🛠️ Compile the program using gcc:

   ```bash
gcc main.c -o output
    ```

4. ▶️ Run the compiled program:
 
   ```bash
./student_manager
    ```
