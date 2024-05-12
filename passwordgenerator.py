{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "601a565e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Password Generator\n",
      "Enter the desired length of the password: 7\n",
      "Generated Password: q)q$vXT\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import string\n",
    "\n",
    "def generate_password(length):\n",
    "    characters = string.ascii_letters + string.digits + string.punctuation\n",
    "    password = ''.join(random.choice(characters) for _ in range(length))\n",
    "    return password\n",
    "\n",
    "def main():\n",
    "    print(\"Welcome to Password Generator\")\n",
    "\n",
    "    while True:\n",
    "        try:\n",
    "            length = int(input(\"Enter the desired length of the password: \"))\n",
    "            if length <= 0:\n",
    "                raise ValueError(\"Length must be a positive integer\")\n",
    "            break\n",
    "        except ValueError as e:\n",
    "            print(\"Invalid input. Please enter a valid positive integer.\")\n",
    "\n",
    "    password = generate_password(length)\n",
    "    print(\"Generated Password:\", password)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba1b0784",
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
