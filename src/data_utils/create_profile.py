import csv
import bcrypt
from getpass import getpass  # for secure password input
import os
import json

def prompt_user_data():

    def hash_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

        # Function to get user choice from a list of options
    def get_user_choice(prompt_message, options):
        print(prompt_message)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Enter the number of your choice: ")
        while not choice.isdigit() or not (1 <= int(choice) <= len(options)):
            print("Invalid choice. Please enter a number corresponding to the options.")
            choice = input("Enter the number of your choice: ")
        return options[int(choice) - 1]

    # Function to get user choice from a list of options
    def get_user_choice(prompt_message, options):
        print(prompt_message)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Enter the number of your choice: ")
        while not choice.isdigit() or not (1 <= int(choice) <= len(options)):
            print("Invalid choice. Please enter a number corresponding to the options.")
            choice = input("Enter the number of your choice: ")
        return options[int(choice) - 1]
    
    username = input("Enter your username: ")


    # Collect user input
    user_data = {
        'password': getpass("Enter your password: "),  # Secure password entry
        'name': input("Enter your full name: "),
        'dob': input("Enter your date of birth (YYYY-MM-DD): "),
        'gender': input("Enter your gender: "),
        'height': input("Enter your height (in cm): "),
        'weight': input("Enter your weight (in kg): "),
        'state': input("Enter your state: "),
    }

    # Securely hash the password
    user_data['password'] = hash_password(user_data['password'])

    # Advanced questions with choices
    user_data['goal'] = get_user_choice("What's your goal? Choose the option that best describes you:",
                                        ["Be Healthier", "Improve Fitness", "Optimize Performance"])

    user_data['coaching_style'] = get_user_choice("\nStyle of coaching? Who do you want to get better with?",
                                                  ["Ted Lasso", "Motivational", "Aggressive", "Neutral"])

    user_data['fitness_level'] = get_user_choice("\nEnter your current fitness level:",
                                                 ["Beginner", "Intermediate", "Advanced"])

    user_data['equipment_availability'] = get_user_choice("\nDescribe your equipment availability:",
                                                          ["Gym", "Home", "None"])

    # Additional open-ended questions
    user_data['dietary_habits'] = input("Describe your dietary habits: ")
    user_data['stress_levels'] = input("Rate your stress levels on a scale of 1 to 10: ")
    user_data['obstacles'] = input("List any obstacles or challenges you face in exercising: ")
    user_data['time_availability'] = get_user_choice("How much time can you dedicate to exercise (per day/week): ", ["1-2 days/week", "3-4 days/week", "5-7 days/week"])
    user_data['location_preferences'] = get_user_choice("Your preferred location for exercising: ", ["Indoors", "Outdoors", "Gym"])
    user_data['medical_conditions'] = input("List any existing medical conditions (separate by comma): ")
    user_data['previous_injuries'] = input("List any previous injuries (separate by comma): ")
    user_data['medications'] = input("List any medications you are currently taking (separate by comma): ")

    return {username: user_data}


def save_user_data(user_profiles, file_name='user_profiles.json'):
    # Check if file exists and load existing data
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            existing_data = json.load(file)
        existing_data.update(user_profiles)
        user_profiles = existing_data

    # Write updated data to file
    with open(file_name, 'w') as file:
        json.dump(user_profiles, file, indent=4)


def create_user_profile():
    # Example usage
    user_profiles = prompt_user_data()
    save_user_data(user_profiles)

    print(f"User profiles saved to user_profiles.json")

# The entry point of the script
if __name__ == "__main__":
    create_user_profile()