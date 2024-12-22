#include <iostream>
#include <vector>
#include <string>

struct Task {
    std::string description;
    bool isCompleted;

    Task(const std::string& desc) : description(desc), isCompleted(false) {}
};

void displayMenu();
void addTask(std::vector<Task>& tasks);
void displayTasks(const std::vector<Task>& tasks);
void markTaskCompleted(std::vector<Task>& tasks);
void deleteTask(std::vector<Task>& tasks);

int main() {
    std::vector<Task> tasks;
    int choice;

    do {
        displayMenu();
        std::cout << "Enter your choice: ";
        std::cin >> choice;
        std::cin.ignore();

        switch (choice) {
            case 1:
                addTask(tasks);
                break;
            case 2:
                displayTasks(tasks);
                break;
            case 3:
                markTaskCompleted(tasks);
                break;
            case 4:
                deleteTask(tasks);
                break;
            case 5:
                std::cout << "Exiting the application. Goodbye!\n";
                break;
            default:
                std::cout << "Invalid choice. Please try again.\n";
        }

    } while (choice != 5);

    return 0;
}

void displayMenu() {
    std::cout << "\nTo-Do App Menu:\n";
    std::cout << "1. Add Task\n";
    std::cout << "2. Display Tasks\n";
    std::cout << "3. Mark Task as Completed\n";
    std::cout << "4. Delete Task\n";
    std::cout << "5. Exit\n";
}

void addTask(std::vector<Task>& tasks) {
    std::cout << "Enter the task description: ";
    std::string description;
    std::getline(std::cin, description);
    tasks.emplace_back(description);
    std::cout << "Task added successfully!\n";
}

void displayTasks(const std::vector<Task>& tasks) {
    if (tasks.empty()) {
        std::cout << "No tasks to display.\n";
        return;
    }

    std::cout << "\nTasks:\n";
    for (size_t i = 0; i < tasks.size(); ++i) {
        std::cout << i + 1 << ". " << tasks[i].description;
        if (tasks[i].isCompleted) {
            std::cout << " [Completed]";
        }
        std::cout << "\n";
    }
}

void markTaskCompleted(std::vector<Task>& tasks) {
    if (tasks.empty()) {
        std::cout << "No tasks available to mark as completed.\n";
        return;
    }

    displayTasks(tasks);
    std::cout << "Enter the task number to mark as completed: ";
    size_t taskNumber;
    std::cin >> taskNumber;

    if (taskNumber == 0 || taskNumber > tasks.size()) {
        std::cout << "Invalid task number.\n";
    } else {
        tasks[taskNumber - 1].isCompleted = true;
        std::cout << "Task marked as completed!\n";
    }
}

void deleteTask(std::vector<Task>& tasks) {
    if (tasks.empty()) {
        std::cout << "No tasks available to delete.\n";
        return;
    }

    displayTasks(tasks);
    std::cout << "Enter the task number to delete: ";
    size_t taskNumber;
    std::cin >> taskNumber;

    if (taskNumber == 0 || taskNumber > tasks.size()) {
        std::cout << "Invalid task number.\n";
    } else {
        tasks.erase(tasks.begin() + taskNumber - 1);
        std::cout << "Task deleted successfully!\n";
    }
}
