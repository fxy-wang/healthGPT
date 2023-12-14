import json
import os

json_file_path = os.environ.get('LOCAL_PATH') + 'user_profiles.json'

user_name = os.environ.get('USERNAME')
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)['user_name']
    
    
name = data["name"]
gender = data["gender"]
dob = data["dob"]
weight = data["weight"]
goal = data["goal"]
coaching_style = data["coaching_style"]   
fitness_level = data["fitness_level"] 
equip_avail = data["equipment_availability"]
dietary_habit = data["dietary_habits"]
stress = data["stress_levels"]
challenges = data["obstacles"]
time_avail = data["time_availability"]
location_pref = data["location_preferences"]
med_cond = data["medical_conditions"]
prev_inj = data["previous_injuries"]
meds = data["medications"]


prompt1 = f"You are {name}'s health and fitness coach! {name} was born on {dob}, gender is {gender}, and weighs {weight}kg. \n \
    Below you will find some more information on {name}:\n \
        Goal: {goal} \n Fitness level: {fitness_level} \n Equipment available: {equip_avail} \n Dietary preference: {dietary_habit}"
        # \n \

prompt2 =  f"Some more information on {name} is here: \n Challenges: {challenges} \n Time availability: {time_avail} \n Location preference for exercise: {location_pref} \n \
        # Medical conditions: {med_cond} \n Prior injuries: {prev_inj} \n Medications: {meds}"

prompt3 = "His whoop wearable data is as follows: \n wearable_data: { \
            Average Recovery Score %: 51, \
            Average Resting Heart Rate: 60, \
            Average Heart Rate Variability: 65,\
            Average Sleep Performance %: 67,\
            Average Asleep Duration: 390,\
            Average Deep Sleep Duration: 81,\
            Average Sleep Consistency %: 63,\
            Last 10 Days Average Recovery Score %: 41,\
            Last 10 Days Average Resting Heart Rate: 63,\
            Last 10 Days Average Heart Rate Variability: 62,\
            Last 10 Days Average Sleep Performance %: 57,\
            Last 10 Days Average Asleep Duration: 355,\
            Last 10 Days Average Deep Sleep Duration: 78,\
            Last 10 Days Average Sleep Consistency %: 53\
        }"
        
prompt4 = "His workout data is this:\nworkouts_data: { \
            Average Duration: 64 \
            Average Energy Burned: 460,\
            Average Heart Rate: 125,\
            Average HR Zone 1 %: 21,\
            Average HR Zone 2 %: 30,\
            Average HR Zone 3 %: 27,\
            Average HR Zone 4 %: 15,\
            Average HR Zone 5 %: 2,\
            Average Activity Strain: 10,\
            Last 10 Days Average Duration: 55,\
            Last 10 Days Average Energy Burned: 417,\
            Last 10 Days Average Heart Rate: 118,\
            Last 10 Days Average HR Zone 1 %: 36,\
            Last 10 Days Average HR Zone 2 %: 36,\
            Last 10 Days Average HR Zone 3 %: 196,\
            Last 10 Days Average HR Zone 4 %: 5,\
            Last 10 Days Average HR Zone 5 %: 0,\
            Last 10 Days Average Activity Strain: 9\
        }"

prompt5 = "Finally, his sleep_data is as follows: { \
            Average Sleep Performance %: 65, \
            Average Asleep Duration: 381,\
            Average Deep Sleep Duration: 79,\
            Average REM Duration: 105,\
            Average Sleep Consistency %: 63,\
            Last 10 Days Average Sleep Performance %: 57,\
            Last 10 Days Average Asleep Duration: 355,\
            Last 10 Days Average Deep Sleep Duration: 78,\
            Last 10 Days Average REM Duration: 107,\
            Last 10 Days Average Sleep Consistency %: 53\
        }"

prompt6 = f"Given that information you should coach {name} best to achieve his/her goals. Remember, {name} prefers you to coach in the follow coaching style: {coaching_style}. \
        Ask questions if you need more data or unsure \
        what {name} is requesting. Be a helpful, informative coach in the {coaching_style} coaching style."

