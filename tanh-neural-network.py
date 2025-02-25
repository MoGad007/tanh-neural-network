{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "14d29af8-6f3c-42c2-aa82-441767f25bc9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Final output of the neural network: 0.8041165383834986\n",
      "Total steps taken: 1305\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import math\n",
    "\n",
    "# Define the tanh activation function\n",
    "def tanh(x):\n",
    "    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))\n",
    "\n",
    "# Initialize weights randomly in the range [-0.5, 0.5]\n",
    "def initialize_weights():\n",
    "    return random.uniform(-0.5, 0.5)\n",
    "\n",
    "w1, w2, w3, w4 = initialize_weights(), initialize_weights(), initialize_weights(), initialize_weights()\n",
    "w5, w6 = initialize_weights(), initialize_weights()\n",
    "\n",
    "# Bias values\n",
    "b1 = 0.5\n",
    "b2 = 0.7\n",
    "\n",
    "# Input values (example)\n",
    "x1 = 0.3\n",
    "x2 = -0.2\n",
    "\n",
    "target_output = 0.8  # Target output to reach\n",
    "epsilon = 0.01  # Acceptable error margin\n",
    "learning_rate = 0.1  # Learning rate for weight updates\n",
    "\n",
    "# Counter for steps\n",
    "steps = 0\n",
    "\n",
    "# Training loop\n",
    "while True:\n",
    "    steps += 1  # Increment step counter\n",
    "    \n",
    "    # Compute hidden layer neuron output\n",
    "    h1 = tanh(w1 * x1 + w2 * x2 + b1)\n",
    "    h2 = tanh(w3 * x1 + w4 * x2 + b1)\n",
    "    \n",
    "    # Compute final output\n",
    "    o = tanh(w5 * h1 + w6 * h2 + b2)\n",
    "    \n",
    "    # Check if the output is close enough to the target\n",
    "    if abs(o - target_output) < epsilon:\n",
    "        break\n",
    "    \n",
    "    # Adjust weights randomly to move towards the target\n",
    "    w1 += random.uniform(-learning_rate, learning_rate)\n",
    "    w2 += random.uniform(-learning_rate, learning_rate)\n",
    "    w3 += random.uniform(-learning_rate, learning_rate)\n",
    "    w4 += random.uniform(-learning_rate, learning_rate)\n",
    "    w5 += random.uniform(-learning_rate, learning_rate)\n",
    "    w6 += random.uniform(-learning_rate, learning_rate)\n",
    "\n",
    "# Print output and step count\n",
    "print(\"Final output of the neural network:\", o)\n",
    "print(\"Total steps taken:\", steps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7dd8610d-df7f-4739-8e6b-9f367de26a56",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
