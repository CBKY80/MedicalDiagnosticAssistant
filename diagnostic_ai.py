def medical_diagnostic_assistant():
    print("--------------------------------------------------")
    print("Welcome to the Medical Diagnostic Assistant!")
    print("Please answer the following questions with 'yes' or 'no'.")
    print("Disclaimer: This is a simple educational tool and not a substitute for professional medical advice.")
    print("--------------------------------------------------\n")

    has_fever = get_yes_or_no_answer("Do you have fever?")

    if has_fever:
        print("\nBased on your Fever, we might be looking at the flu.")

        has_body_aches = get_yes_or_no_answer("Are you experiencing body aches?")
        if has_body_aches:
            diagnosis = "The flu. Body aches and fever are common symptoms of the flu."
        else:
            diagnosis = "Possible the flu, but it could be another condition causing the fever."
    else:
        print("\nSince you do not have a fever, it is less likely to be the flu")

        is_worse_indoors = get_yes_or_no_answer("Are your symptoms (like sneezing and stuffy nose) worse indoors? ")
        if is_worse_indoors:
            diagnosis = "Allergies. Symptoms that worsen indoors can often be due to indoor allergens like dust mites or pet dander."
        else:
            has_a_sore_throat = get_yes_or_no_answer("Do you have a sore throat?")
            if has_a_sore_throat:
                diagnosis = "The Common Cold. A sore throat without a fever is a classic sign of a common cold."
            else:
                diagnosis = "This might be a cold or another minor issue."

    print("\n------------------- Diagnosis --------------------")
    print(f"Suggestion: {diagnosis}")
    print("--------------------------------------------------")
    print("\nRemember to consult with a healthcare professional for an accurate diagnosis.")



def get_yes_or_no_answer(question):
    while True:
        answer = input(question).strip().lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please answer yes or no.")

if __name__ == '__main__':
    medical_diagnostic_assistant()
