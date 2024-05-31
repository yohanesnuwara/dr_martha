import pandas as pd
import numpy as np

def dentist(scores):
    # Print information
    # Initialize a dictionary to store counts for each code
    code_counts = {}
    for code in scores:
        # Check if the code exists in the dictionary
        if code in code_counts:
            # Increment the count for the existing code
            code_counts[code] += 1
        else:
            # Add the code to the dictionary with a count of 1
            code_counts[code] = 1

    # Build the output sentence
    output_parts = []
    for code, count in code_counts.items():
        output_parts.append(f"{count} {code} teeth")

    # Combine parts with commas and "and"
    output_sentence = ", ".join(output_parts[:-1]) + ", and " + output_parts[-1]
    output_sentence = "You have " + output_sentence

    print(output_sentence)

    # Dataframe consists of dental caries stage
    teeth_score_df = pd.read_csv("D:\\Tri Valley Hackathon\\flask_yolo_app\\data\\teeth_score.csv")

    # Find out the most severe condition of teeth e.g. if only one D6 detected, suggest D6 treatment
    level = [int(s[-1]) for s in scores]
    max_level = max(level)

    # Lookup table to suggest recommendation
    severity = teeth_score_df[teeth_score_df.level==max_level]
    treatment = severity.treatment.values[0]
    print(treatment)

    if severity.need_dentist.values[0]:
        need_dentist = "Book consultation with Dentist"
    else:
        need_dentist = "Keep your teeth healthy :)"
    
    print(need_dentist)
    return output_sentence, treatment, need_dentist

def diagnosis(detected_classes):
    disease = np.unique(detected_classes)
    output_sentence = "You have indication of "
    if len(disease) == 1:
        # Single element case
        output_sentence += disease[0]  # Directly access the element
    else:
        # Multiple element case (original loop)
        for item in disease:
            output_sentence += item + ", "
        # Remove the trailing comma and space (if applicable)
        output_sentence = output_sentence[:-2]
    return output_sentence

def suggest_medicine(detected_classes):
    df_medicine = pd.read_csv("D:\\Tri Valley Hackathon\\flask_yolo_app\\data\\medicine.csv")
    detected_disease = np.unique(detected_classes)
    medicines = []
    for disease in detected_disease:
        try:
            medicine = df_medicine[df_medicine.disease==disease].medicine.values
        except:
            medicine = 0
            print("Medication not available or no need.")
        medicines.append(medicine)
    return medicines
    