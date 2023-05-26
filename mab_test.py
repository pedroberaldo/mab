import numpy as np
import random

# Number of button types
n_buttons = 4
n_sims = 1000

# Initialize counts of successes (clicks) and failures (no clicks) for each button type
successes = [0] * n_buttons
failures = [0] * n_buttons

# Number of rounds to run the experiment
n_rounds = 100

# Simulate the true probability of clicks for each button type
# (you should replace these with the true probabilities for your specific case)
true_probabilities = [0.1, 0.15, 0.2, 0.25]

# Function to simulate a click based on the true probability of the button
def simulate_click(button_idx):
    return random.random() < true_probabilities[button_idx]

# Run the Thompson Sampling algorithm
for _ in range(n_sims):
    for _ in range(n_rounds):
        # Sample from the Beta distribution for each button
        samples = [np.random.beta(successes[i] + 1, failures[i] + 1) for i in range(n_buttons)]

        # Select the button with the highest sampled value
        selected_button = np.argmax(samples)

        # Simulate a click on the selected button
        click = simulate_click(selected_button)

        # Update the success and failure counts for the selected button
        if click:
            successes[selected_button] += 1
        else:
            failures[selected_button] += 1

# Print the results
print("True probabilities:", true_probabilities)
print("Estimated probabilities:", [successes[i] / (successes[i] + failures[i]) for i in range(n_buttons)])
print("Total successes:", successes)
print("Total failures:", failures)
