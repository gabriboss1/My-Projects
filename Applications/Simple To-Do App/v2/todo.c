#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TASKS 100
#define TASK_LENGTH 100

typedef struct {
    char description[TASK_LENGTH];
    int isCompleted;
} Task;

Task tasks[MAX_TASKS];
int taskCount = 0;

void displayMenu();
void addTask();
void viewTasks();
void markTaskCompleted();
void deleteTask();

int main() {
    int choice;

    while (1) {
        displayMenu();
        printf("Enter your choice: ");
        scanf("%d", &choice);
        getchar(); 

        switch (choice) {
            case 1:
                addTask();
                break;
            case 2:
                viewTasks();
                break;
            case 3:
                markTaskCompleted();
                break;
            case 4:
                deleteTask();
                break;
            case 5:
                printf("Exiting... Have a productive day!\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}

void displayMenu() {
    printf("\n");
    printf("========== TO-DO APP ==========\n");
    printf("1. Add Task\n");
    printf("2. View Tasks\n");
    printf("3. Mark Task as Completed\n");
    printf("4. Delete Task\n");
    printf("5. Exit\n");
    printf("================================\n");
}

void addTask() {
    if (taskCount >= MAX_TASKS) {
        printf("Task list is full! Cannot add more tasks.\n");
        return;
    }

    printf("Enter the task description: ");
    fgets(tasks[taskCount].description, TASK_LENGTH, stdin);
    tasks[taskCount].description[strcspn(tasks[taskCount].description, "\n")] = 0;
    tasks[taskCount].isCompleted = 0;

    taskCount++;
    printf("Task added successfully!\n");
}

void viewTasks() {
    if (taskCount == 0) {
        printf("No tasks available!\n");
        return;
    }

    printf("\n========== TO-DO LIST ==========\n");
    for (int i = 0; i < taskCount; i++) {
        printf("%d. [%c] %s\n", i + 1, tasks[i].isCompleted ? 'X' : ' ', tasks[i].description);
    }
    printf("================================\n");
}

void markTaskCompleted() {
    int taskNumber;

    if (taskCount == 0) {
        printf("No tasks to mark as completed!\n");
        return;
    }

    viewTasks();
    printf("Enter the task number to mark as completed: ");
    scanf("%d", &taskNumber);
    getchar(); 

    if (taskNumber < 1 || taskNumber > taskCount) {
        printf("Invalid task number! Please try again.\n");
        return;
    }

    tasks[taskNumber - 1].isCompleted = 1;
    printf("Task marked as completed!\n");
}

void deleteTask() {
    int taskNumber;

    if (taskCount == 0) {
        printf("No tasks to delete!\n");
        return;
    }

    viewTasks();
    printf("Enter the task number to delete: ");
    scanf("%d", &taskNumber);
    getchar();

    if (taskNumber < 1 || taskNumber > taskCount) {
        printf("Invalid task number! Please try again.\n");
        return;
    }

    for (int i = taskNumber - 1; i < taskCount - 1; i++) {
        tasks[i] = tasks[i + 1];
    }
    taskCount--;
    printf("Task deleted successfully!\n");
}
