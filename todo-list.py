{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ac21bcba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "To-Do List Application\n",
      "1. Add Task\n",
      "2. View Tasks\n",
      "3. Update Task\n",
      "4. Remove Task\n",
      "5. Exit\n",
      "Enter your choice: 2\n",
      "No tasks to display.\n",
      "\n",
      "To-Do List Application\n",
      "1. Add Task\n",
      "2. View Tasks\n",
      "3. Update Task\n",
      "4. Remove Task\n",
      "5. Exit\n",
      "Enter your choice: 3\n",
      "Enter task index to update: 2\n",
      "Enter new task: bye\n",
      "Invalid task index.\n",
      "\n",
      "To-Do List Application\n",
      "1. Add Task\n",
      "2. View Tasks\n",
      "3. Update Task\n",
      "4. Remove Task\n",
      "5. Exit\n",
      "Enter your choice: 2\n",
      "No tasks to display.\n",
      "\n",
      "To-Do List Application\n",
      "1. Add Task\n",
      "2. View Tasks\n",
      "3. Update Task\n",
      "4. Remove Task\n",
      "5. Exit\n",
      "Enter your choice: 5\n",
      "Exiting...\n"
     ]
    }
   ],
   "source": [
    "class TodoList:\n",
    "    def __init__(self):\n",
    "        self.tasks = []\n",
    "\n",
    "    def add_task(self, task):\n",
    "        self.tasks.append(task)\n",
    "        print(\"Task added successfully!\")\n",
    "\n",
    "    def view_tasks(self):\n",
    "        if self.tasks:\n",
    "            print(\"Tasks:\")\n",
    "            for index, task in enumerate(self.tasks, 1):\n",
    "                print(f\"{index}. {task}\")\n",
    "        else:\n",
    "            print(\"No tasks to display.\")\n",
    "\n",
    "    def update_task(self, index, new_task):\n",
    "        if 1 <= index <= len(self.tasks):\n",
    "            self.tasks[index - 1] = new_task\n",
    "            print(\"Task updated successfully!\")\n",
    "        else:\n",
    "            print(\"Invalid task index.\")\n",
    "\n",
    "    def remove_task(self, index):\n",
    "        if 1 <= index <= len(self.tasks):\n",
    "            del self.tasks[index - 1]\n",
    "            print(\"Task removed successfully!\")\n",
    "        else:\n",
    "            print(\"Invalid task index.\")\n",
    "\n",
    "\n",
    "def main():\n",
    "    todo_list = TodoList()\n",
    "    while True:\n",
    "        print(\"\\nTo-Do List Application\")\n",
    "        print(\"1. Add Task\")\n",
    "        print(\"2. View Tasks\")\n",
    "        print(\"3. Update Task\")\n",
    "        print(\"4. Remove Task\")\n",
    "        print(\"5. Exit\")\n",
    "\n",
    "        choice = input(\"Enter your choice: \")\n",
    "\n",
    "        if choice == '1':\n",
    "            task = input(\"Enter task: \")\n",
    "            todo_list.add_task(task)\n",
    "        elif choice == '2':\n",
    "            todo_list.view_tasks()\n",
    "        elif choice == '3':\n",
    "            index = int(input(\"Enter task index to update: \"))\n",
    "            new_task = input(\"Enter new task: \")\n",
    "            todo_list.update_task(index, new_task)\n",
    "        elif choice == '4':\n",
    "            index = int(input(\"Enter task index to remove: \"))\n",
    "            todo_list.remove_task(index)\n",
    "        elif choice == '5':\n",
    "            print(\"Exiting...\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid choice. Please try again.\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74472f72",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}