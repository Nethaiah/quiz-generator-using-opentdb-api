import requests
import json

# difficulty levels
difficulty_levels = {1: "Easy", 2: "Medium", 3: "Hard"}

# question types
question_types = {1: "Multiple", 2: "Boolean"}

# Function to fetch categories
def fetch_category():
    url = "https://opentdb.com/api_category.php"
    
    try: 
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Check if the response status is OK (200)
        if response.status_code == 200:
            # Load the JSON response text into a Python dictionary
            data = json.loads(response.text)
            # Extract the 'trivia_categories' list from the data dictionary
            categories = data.get("trivia_categories", [])
        
            # Loop through all categories and print their IDs and names
            for category in categories:
                print(f"{category["id"]}: {category["name"]}")
            
            return categories
        
        else:
            print("Failed to fetch categories.")
            return
        
    except Exception as e:
        print(f"An Exception Occured {e}")
        return 
        
# Function to choose a category
def choose_category(categories):
    # Create a list of category IDs from categories
    category_ids = []
    
    for category in categories:
        category_ids.append(category["id"])
        
    category_id = int(input("\nPlease input the ID of the category you want to answer: "))
    
    if category_id not in category_ids:
        print("Invalid category ID. Please try again.")
        return choose_category(categories)
        
    return category_id

def choose_difficulty():
    difficulty_level = int(input(f"\nPlease input the number of difficulty level you want to answer: {difficulty_levels}: "))
    
    if difficulty_level not in difficulty_levels:
        print("Invalid difficulty level. Please try again.")
        return choose_difficulty()
    
    return difficulty_levels[difficulty_level]

def choose_question_type():
    question_type = int(input(f"\nPlease input the number of question type you want to answer {question_types}: "))
    
    if question_type not in question_types:
        print("Invalid question type. Please try again.")
        return  choose_question_type()
    
    return question_types[question_type]
    
def fetch_question(num_ques, category_id, diff_level, ques_type):
    url = f"https://opentdb.com/api.php?amount={num_ques}&category={category_id}&difficulty={diff_level}&type={ques_type}"
    
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Check if the response status is OK (200)
        if response.status_code == 200:
            # Load the JSON response text into a Python dictionary
            data = json.loads(response.text)
            # Extract the 'trivia_categories' list from the data dictionary
            questions = data.get("results", [])
            
            return questions
            
        else:
            print("Error occurred while fetching questions.")
            return
        
    except Exception as e:
        print(f"An Exception Occured {e}")
        return 
    
def main():
    catagories = fetch_category()
    category_id = choose_category(catagories)
    diff_level = choose_difficulty().lower()
    ques_type = choose_question_type().lower()
    num_ques = int(input("\nHow many questions would you like to answer? (1 - 50): "))
    
    if num_ques < 1 or num_ques > 50:
        print("Invalid number of questions. Please choose a number between 1 and 50.")
        return
    
    questions = fetch_question(num_ques, category_id, diff_level, ques_type)
    
    score = 0
    
    if ques_type == "boolean":
        for i, question in enumerate(questions):
            print(f"\nQuestion {i + 1}: {question['question']}")
            answer = input("Your answer (True/False): ").strip().lower()
            correct_answer = question['correct_answer'].lower()
            
            if answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.\n")
                
    elif ques_type == "multiple":
        for i, question in enumerate(questions):
            print(f"\nQuestion {i + 1}: {question['question']}")
            print("Options:")
            all_answers = question["incorrect_answers"] + [question["correct_answer"]]
            for j, option in enumerate(all_answers):
                print(f"{j + 1}. {option}")
                
            answer = int(input("Enter the number of your answer: "))
            
            if all_answers[answer - 1] == question["correct_answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {question['correct_answer']}.\n")
                
    print(f"Quiz completed! Your score is {score}/{num_ques}.")
    
if __name__ == "__main__":
    main()
    