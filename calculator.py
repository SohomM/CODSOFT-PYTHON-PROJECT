{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8f525ac3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Simple Calculator\n",
      "Operations:\n",
      "1. Addition (+)\n",
      "2. Subtraction (-)\n",
      "3. Multiplication (*)\n",
      "4. Division (/)\n",
      "Enter choice (1/2/3/4): 1\n",
      "Enter first number: 23\n",
      "Enter second number: 2\n",
      "Result: 25.0\n"
     ]
    }
   ],
   "source": [
    "def add(x, y):\n",
    "    return x + y\n",
    "\n",
    "def subtract(x, y):\n",
    "    return x - y\n",
    "\n",
    "def multiply(x, y):\n",
    "    return x * y\n",
    "\n",
    "def divide(x, y):\n",
    "    if y == 0:\n",
    "        return \"Error: Division by zero!\"\n",
    "    else:\n",
    "        return x / y\n",
    "\n",
    "print(\"Welcome to Simple Calculator\")\n",
    "print(\"Operations:\")\n",
    "print(\"1. Addition (+)\")\n",
    "print(\"2. Subtraction (-)\")\n",
    "print(\"3. Multiplication (*)\")\n",
    "print(\"4. Division (/)\")\n",
    "\n",
    "while True:\n",
    "    choice = input(\"Enter choice (1/2/3/4): \")\n",
    "\n",
    "    if choice in ('1', '2', '3', '4'):\n",
    "        num1 = float(input(\"Enter first number: \"))\n",
    "        num2 = float(input(\"Enter second number: \"))\n",
    "\n",
    "        if choice == '1':\n",
    "            print(\"Result:\", add(num1, num2))\n",
    "        elif choice == '2':\n",
    "            print(\"Result:\", subtract(num1, num2))\n",
    "        elif choice == '3':\n",
    "            print(\"Result:\", multiply(num1, num2))\n",
    "        elif choice == '4':\n",
    "            print(\"Result:\", divide(num1, num2))\n",
    "        \n",
    "        break\n",
    "    else:\n",
    "        print(\"Invalid input. Please enter a valid operation choice.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17902d52",
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
