#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#define Name_size 50
/*------------------------------------*/

   typedef struct {
        int id;
        char name[Name_size];
    } student;

    typedef struct {
        double mathmatics;
        double physics;
        double biology;
        double chemistry;
    } ModulesGrade;

/*------------------------------------*/
int namevalidation(char *name); 
int gradevalidation(double *grade);
char gradingSystem(ModulesGrade *grades);
int Idvalidation(int *idCheck);
int markExtraction(int IdCheck, FILE *file, char *line, int *choice, ModulesGrade *grades);
void InfoEntry(student *newStudent, ModulesGrade *grades);
void fileOpen(FILE **file);
/*------------------------------------*/

int main() {
 

    FILE *file;
    char line[256];
    int lastID = 0;
    student newStudent;
    ModulesGrade grades;
    
    snprintf(newStudent.name, sizeof(newStudent.name), "New Student");
    grades.mathmatics = 0.0;
    grades.physics = 0.0;
    grades.biology = 0.0;
    grades.chemistry = 0.0;
    int choice = 0;
    fileOpen(&file);  
   

    while (choice != 4) {
        printf("\n\n1- Add a new student\n");
        printf("2- Check highest and lowest grades\n");
        printf("3- Check pass or fail\n");
        printf("4- Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {  
        case 1: {
            file = fopen("student.csv", "r");

            
          
            while (fgets(line, sizeof(line), file) != NULL) {
                sscanf(line, "%d", &lastID);
            }
            fclose(file);

            newStudent.id = lastID + 1;
            InfoEntry(&newStudent, &grades);
            file = fopen("student.csv", "a");
            fprintf(file, "%d - %s - %.2lf - %.2lf - %.2lf - %.2lf - %c\n", 
                newStudent.id, newStudent.name, 
                grades.mathmatics, grades.physics, 
                grades.biology, grades.chemistry, 
                gradingSystem(&grades));
            fclose(file);
            break;
        }

        /*--------------------------------------------------------------------------------------*/

        case 2: {
            int IdCheck = 0;

            do {
                printf("\nEnter student Id: ");
            } while (Idvalidation(&IdCheck));

            file = fopen("student.csv", "r");
            markExtraction(IdCheck, file, line, &choice, &grades);
            fclose(file);
            break;
        }

        /*--------------------------------------------------------------------------------------*/

        case 3:  {
            int IdCheck = 0;
            
            do {
                printf("\nEnter student Id: ");
            } while (Idvalidation(&IdCheck));

            file = fopen("student.csv", "r");
            markExtraction(IdCheck, file, line, &choice, &grades);
            fclose(file);
            break;
        }

        /*--------------------------------------------------------------------------------------*/

        case 4: {
            printf("Exiting...\n");
            return 0;
        }

        /*--------------------------------------------------------------------------------------*/

        default: {
            printf("Invalid choice. Please try again.\n");
            break;
        }
    }


}
    return 0;
}

         /*--------------------------------------------------------------------------------------*/

int namevalidation(char *name) {
    if (name[0] == '\0' || name[0] == ' ') {
        printf("Name cannot be empty or start with a space. Please enter a valid name.\n");
        return 0;
    }

    for (int i = 0; name[i] != '\0'; i++) {
        name[i] = tolower(name[i]);
        
        if (!isalpha(name[i]) && name[i] != ' ') {
            printf("Name must contain only alphabetic characters and spaces. Please enter a valid name.\n");
            return 0;
        }
    }
    
    return 1;
}
        /*--------------------------------------------------------------------------------------*/

int gradevalidation(double *grade) {
    if (scanf("%lf", grade) != 1) {
        printf("Invalid input. Please enter a valid number for the grade.\n");
        while (getchar() != '\n'); 
        return 1;
    }
    
    if (*grade < 0 || *grade > 100) {
        printf("Invalid grade entered. Please enter grades between 0 and 100.\n");
        return 1;
    }

    return 0;
}
        /*--------------------------------------------------------------------------------------*/

char gradingSystem(ModulesGrade *grades) {
    double average = (grades->mathmatics + grades->physics + grades->biology + grades->chemistry) / 4.0;
    char mark;
    
    if (average >= 90) mark = 'A';
    else if (average >= 75) mark = 'B';  
    else if (average >= 60) mark = 'C';  
    else if (average >= 50) mark = 'D';  
    else mark = 'F';
    
    return mark;
}
        /*--------------------------------------------------------------------------------------*/

int Idvalidation(int *idCheck) {
    if (scanf("%d", idCheck) != 1) {
        printf("Invalid input. Please enter a digit in number.\n");
        while (getchar() != '\n');
        return 1;
    }
    else if (*idCheck <= 0) {
        printf("Invalid ID. Please enter a positive integer.\n");
        return 1;
    }
    
    return 0;
}
        /*--------------------------------------------------------------------------------------*/

int markExtraction(int IdCheck, FILE *file, char *line, int *choice, ModulesGrade *grades) {
    int found = 0;

    while (fgets(line, 256, file) != NULL) {
        int id;
        char name[Name_size], grade_letter;
        double math, physics, biology, chemistry;
        
         if (sscanf(line, "%d - %49[^-] - %lf - %lf - %lf - %lf - %c",
                  &id, name, &math, &physics, &biology, &chemistry, &grade_letter) == 7) {
            if (id == IdCheck) {
                found = 1;
                ModulesGrade tempGrades;
                tempGrades.mathmatics = math;
                tempGrades.physics = physics;
                tempGrades.biology = biology;
                tempGrades.chemistry = chemistry;

                if (*choice == 3) {
                    printf("Student with Id %d has %s\n", IdCheck, 
                          gradingSystem(&tempGrades) == 'F' ? "failed" : "passed");
                } 
                else if (*choice == 2) {
                    double min_grade = fmin(fmin(math, physics), fmin(biology, chemistry));
                    double max_grade = fmax(fmax(math, physics), fmax(biology, chemistry));
                    printf("Student with Id %d got highest grade %.2lf and lowest grade %.2lf\n", 
                          IdCheck, max_grade, min_grade);
                }
                break;
            }
        }
    }

    if (!found) {
        printf("Student with Id %d not found.\n", IdCheck);
    }
    return found;
}

        /*--------------------------------------------------------------------------------------*/

void InfoEntry(student *newStudent, ModulesGrade *grades) {
    do {
        printf("Enter student name: ");
        scanf(" %[^\n]", newStudent->name);
    } while (!namevalidation(newStudent->name));

    for (int i = 0; newStudent->name[i]; i++) {
        newStudent->name[i] = tolower(newStudent->name[i]);
    }

    do {
        printf("\nEnter Math grade: ");
    } while (gradevalidation(&grades->mathmatics));

    do {
        printf("Enter Physics grade: ");
    } while (gradevalidation(&grades->physics));

    do {
        printf("Enter Biology grade: ");
    } while (gradevalidation(&grades->biology));

    do {
        printf("Enter Chemistry grade: ");
    } while (gradevalidation(&grades->chemistry));
}
        /*--------------------------------------------------------------------------------------*/
void fileOpen(FILE **file) {
    *file = fopen("student.csv", "a");
    if (*file == NULL) {
        printf("Failed to open the file.\n");
    } else {
        printf("File opened successfully.\n");
        fclose(*file);  
    }
}
/*----------------------------------------------------------------------------------------------------------------*/