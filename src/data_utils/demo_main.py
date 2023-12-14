import json
import gradio as gr
from src.user_data_src.create_profile import save_user_data
from sleep_features import analyze_sleep_data, add_data_to_profile, load_user_profiles
from workouts_features import analyze_wearable_data, add_data_to_profile
from physiological_features import analyze_recovery_data, add_data_to_profile

import zipfile
import io
import os

# You can import your existing functions from create_profile.py or paste them directly into this script
from src.user_data_src.create_profile import prompt_user_data, save_user_data

def create_health_persona(username, password, name, dob, gender, height, weight, state, goal, coaching_style, fitness_level, equipment_availability, dietary_habits, stress_levels, obstacles, time_availability, location_preferences, medical_conditions, previous_injuries, medications):
    user_data = {
        'username': username,
        'password': password,  # Assume this will be hashed within the function
        'name': name,
        'dob': dob,
        'gender': gender,
        'height': height,
        'weight': weight,
        'state': state,
        'goal': goal,
        'coaching_style': coaching_style,
        'fitness_level': fitness_level,
        'equipment_availability': equipment_availability,
        'dietary_habits': dietary_habits,
        'stress_levels': stress_levels,
        'obstacles': obstacles,
        'time_availability': time_availability,
        'location_preferences': location_preferences,
        'medical_conditions': medical_conditions,
        'previous_injuries': previous_injuries,
        'medications': medications
    }
    
    # Since we can't directly use input() in a Gradio app, we'll assume the data is already provided by the interface
    user_profiles = {username: user_data}
    save_user_data(user_profiles)
    return "User profiles saved to user_profiles.json"


def process_whoop_files(username, file_info):

    # Path to zip file
    local_file_path = os.environ.get('LOCAL_PATH')
    zip_file_path = local_file_path + os.envrion.get('ZIP_PATH')
    profiles_file_name = 'user_profiles.json'
    profiles = load_user_profiles(profiles_file_name)

    # Check if the file path exists
    if os.path.exists(zip_file_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Extract to a folder named after the username (without the .zip part)
            extraction_path = local_file_path + f"{username}_whoop_data"
            zip_ref.extractall(extraction_path)

        # Process each type of data
        data_files = {
            'sleep': f"{extraction_path}/{username}_sleep.csv",
            'physiological': f"{extraction_path}/{username}_physiological_cycles.csv",
            'workouts': f"{extraction_path}/{username}_workouts.csv"
        }
        
        responses = []

        analyzed_data_sleep = analyze_sleep_data(data_files['sleep'])

        analyzed_data_recovery = analyze_recovery_data(data_files['physiological'])

        analyzed_data_wearable = analyze_wearable_data(data_files['workouts'])
                
        profiles = add_data_to_profile(username, analyzed_data_sleep, profiles)
        profiles = add_data_to_profile(username, analyzed_data_recovery, profiles)
        profiles = add_data_to_profile(username, analyzed_data_wearable, profiles)


        # Save the updated profiles back to the JSON file
        try:
            with open(profiles_file_name, 'w') as file:
                json.dump(profiles, file, indent=4)
            responses.append("Profile data saved successfully.")
        except Exception as e:
            responses.append(f"An error occurred while saving: {e}")

        return "\n".join(responses)
    else:
        return f"Local file {local_file_path} not found."

    
def combined_function(username, password, name, dob, gender, height, weight, state, goal, coaching_style, fitness_level, equipment_availability, dietary_habits, stress_levels, obstacles, time_availability, location_preferences, medical_conditions, previous_injuries, medications, file_info):
    # First create the health persona
    create_health_persona_response = create_health_persona(username, password, name, dob, gender, height, weight, state, goal, coaching_style, fitness_level, equipment_availability, dietary_habits, stress_levels, obstacles, time_availability, location_preferences, medical_conditions, previous_injuries, medications)
    
    # Then process the Whoop files
    process_whoop_files_response = process_whoop_files(username, file_info)
    
    # Combine responses from both functions
    return create_health_persona_response + "\n" + process_whoop_files_response


# Create a Gradio interface with the required inputs
iface = gr.Interface(
    fn=combined_function,
    inputs=[
        gr.Textbox(label="Username"),
        gr.Textbox(label="Password", type="password"),
        gr.Textbox(label="Full Name"),
        gr.Textbox(label="Date of Birth"),
        gr.Radio(label="Gender", choices=["Male", "Female", "Other"]),
        gr.Number(label="Height (in cm)"),
        gr.Number(label="Weight (in kg)"),
        gr.Textbox(label="State"),
        gr.Radio(label="Goal", choices=["Be Healthier", "Improve Fitness", "Optimize Performance"]),
        gr.Radio(label="Coaching Style", choices=["Ted Lasso", "Motivational", "Aggressive", "Neutral"]),
        gr.Radio(label="Fitness Level", choices=["Beginner", "Intermediate", "Advanced"]),
        gr.Radio(label="Equipment Availability", choices=["Gym", "Home", "None"]),
        gr.Textbox(label="Dietary Habits"),
        gr.Slider(label="Stress Levels", minimum=1, maximum=10, step=1),
        gr.Textbox(label="Obstacles or Challenges"),
        gr.Radio(label="Time Availability for Exercise", choices=["1-2 days/week", "3-4 days/week", "5-7 days/week"]),
        gr.Radio(label="Preferred Location for Exercising", choices=["Indoors", "Outdoors", "Gym"]),
        gr.Textbox(label="Medical Conditions"),
        gr.Textbox(label="Previous Injuries"),
        gr.Textbox(label="Medications"),
        gr.File(label="Upload your Whoop file (zip)")
    ],
    outputs="text"
)



# Run the Gradio app
iface.launch()