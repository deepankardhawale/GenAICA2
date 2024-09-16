# Q:5 Generate a model for Covid 19 with symptoms of parameters like fever, cold, shivering,
# weight loss, generate 100 model data with random values for each parameter and order by
# parameter lowest to highest in display based on the input parameter.


# Code-
import random
import pandas as pd

class CovidSymptoms:
    def __init__(self, fever, cold, shivering, weight_loss):
        self.fever = fever
        self.cold = cold
        self.shivering = shivering
        self.weight_loss = weight_loss

    def __str__(self):
        return f"Fever: {self.fever}, Cold: {self.cold}, Shivering: {self.shivering}, Weight Loss: {self.weight_loss}"

def generate_random_symptoms(num_individuals):
    individuals = []
    for _ in range(num_individuals):
        fever = random.uniform(98.0, 104.0)
        cold = random.randint(0, 10)
        shivering = random.randint(0, 10)
        weight_loss = random.uniform(0, 20)
        individuals.append(CovidSymptoms(fever, cold, shivering, weight_loss))
    return individuals

def convert_to_dataframe(individuals):
    data = {
        "Fever": [person.fever for person in individuals],
        "Cold": [person.cold for person in individuals],
        "Shivering": [person.shivering for person in individuals],
        "Weight Loss": [person.weight_loss for person in individuals]
    }
    return pd.DataFrame(data)

individuals = generate_random_symptoms(100)
df = convert_to_dataframe(individuals)
symptom = input("Enter the symptom to sort by (Fever, Cold, Shivering, Weight Loss): ")
sorted_df = df.sort_values(by=symptom)
print(f"Data sorted by {symptom}:")
print(sorted_df)
