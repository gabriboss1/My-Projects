#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

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
        std::cout << "\n\033[1;32mEnter your choice: \033[0m"; 
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
                std::cout << "\n\033[1;34mExiting the application. Goodbye!\033[0m\n"; 
                break;
            default:
                std::cout << "\n\033[1;31mInvalid choice. Please try again.\033[0m\n"; 
        }

    } while (choice != 5);

    return 0;
}

void displayMenu() {
    std::cout << "\n\033[1;36m==============================\033[0m\n"; 
    std::cout << "\033[1;33m       To-Do App Menu         \033[0m\n"; 
    std::cout << "\033[1;36m==============================\033[0m\n";
    std::cout << "\033[1;37m1. Add Task\033[0m\n";
    std::cout << "\033[1;37m2. Display Tasks\033[0m\n";
    std::cout << "\033[1;37m3. Mark Task as Completed\033[0m\n";
    std::cout << "\033[1;37m4. Delete Task\033[0m\n";
    std::cout << "\033[1;37m5. Exit\033[0m\n";
    std::cout << "\033[1;36m==============================\033[0m\n";
}

void addTask(std::vector<Task>& tasks) {
    std::cout << "\n\033[1;32mEnter the task description: \033[0m"; 
    std::string description;
    std::getline(std::cin, description);
    tasks.emplace_back(description);
    std::cout << "\033[1;34mTask added successfully!\033[0m\n"; 
}

void displayTasks(const std::vector<Task>& tasks) {
    if (tasks.empty()) {
        std::cout << "\n\033[1;33mNo tasks to display.\033[0m\n"; 
        return;
    }

    std::cout << "\n\033[1;36m==============================\033[0m\n"; 
    std::cout << "\033[1;33m            Tasks             \033[0m\n"; 
    std::cout << "\033[1;36m==============================\033[0m\n";
    for (size_t i = 0; i < tasks.size(); ++i) {
        std::cout << "\033[1;37m" << std::setw(3) << i + 1 << ". " << tasks[i].description << "\033[0m";
        if (tasks[i].isCompleted) {
            std::cout << " \033[1;32m[Completed]\033[0m"; 
        }
        std::cout << "\n";
    }
}

void markTaskCompleted(std::vector<Task>& tasks) {
    if (tasks.empty()) {
        std::cout << "\n\033[1;33mNo tasks available to mark as completed.\033[0m\n"; 
        return;
    }

    displayTasks(tasks);
    std::cout << "\n\033[1;32mEnter the task number to mark as completed: \033[0m"; 
    size_t taskNumber;
    std::cin >> taskNumber;

    if (taskNumber == 0 || taskNumber > tasks.size()) {
        std::cout << "\033[1;31mInvalid task number.\033[0m\n"; 
    } else {
        tasks[taskNumber - 1].isCompleted = true;
        std::cout << "\033[1;34mTask marked as completed!\033[0m\n"; 
    }
}

void deleteTask(std::vector<Task>& tasks) {
    if (tasks.empty()) {
        std::cout << "\n\033[1;33mNo tasks available to delete.\033[0m\n";
        return;
    }

    displayTasks(tasks);
    std::cout << "\n\033[1;32mEnter the task number to delete: \033[0m";
    size_t taskNumber;
    std::cin >> taskNumber;

    if (taskNumber == 0 || taskNumber > tasks.size()) {
        std::cout << "\033[1;31mInvalid task number.\033[0m\n";
    } else {
        tasks.erase(tasks.begin() + taskNumber - 1);
        std::cout << "\033[1;34mTask deleted successfully!\033[0m\n";
    }
}
