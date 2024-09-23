# Python Models for Covid Symptoms 

This repository contains two Python programs, each solving different problems related to generating random data and parsing mathematical equations.

## Covid-19 Symptoms Model

This model generates random data for 100 individuals, each displaying four Covid-19 symptoms: **fever**, **cold**, **shivering**, and **weight loss**. The data can be sorted based on any symptom, as selected by the user.

### Features:
- Generates random values for fever (in Fahrenheit), cold severity (0-10 scale), shivering severity (0-10 scale), and weight loss (in pounds).
- Allows the user to sort the data based on the symptom of their choice.
- Outputs the sorted data in a readable format.

### How to Use:
1. Run the `covid_symptoms.py` script.
2. The program will ask which symptom you want to sort by (Fever, Cold, Shivering, Weight Loss).
3. After selecting the symptom, the program will display the sorted data for all 100 individuals.

### Example:

```bash
Enter the symptom to sort by (Fever, Cold, Shivering, Weight Loss): Fever
Data sorted by Fever:
       Fever  Cold  Shivering  Weight Loss
43     98.01     4          7          3.9
...
