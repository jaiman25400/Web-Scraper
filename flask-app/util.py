import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')


def process_question_data(raw_data):
    # Split the raw data by '###', which separates the questions
    question_blocks = raw_data.strip().split("###")
    print("blocks :", question_blocks)
    
    questions_list = []
    
    for block in question_blocks:
        # Trim leading/trailing whitespace
        block = block.strip()
        
        if not block:
            continue  # Skip empty blocks
        
        # Split the block into lines (first line is the question, subsequent lines are options)
        lines = block.split("\n")
        
        question_obj = {}
        
        # The first line is the question
        question_obj['question'] = lines[0].strip()
        print("ques obj :", question_obj)
        
        # The following lines are options (A, B, C, D, etc.)
        options = {}
        for line in lines[1:]:
            # Each option starts with 'A.', 'B.', 'C.', 'D.', etc.
            if line.startswith("A.") or line.startswith("B.") or line.startswith("C.") or line.startswith("D."):
                option_label = line.split(".")[0].strip()  # Option A, Option B, etc.
                option_text = line.split(".")[1].strip()  # Option text
                options[option_label] = option_text
        
        question_obj['options'] = options
        
        # Add this question object to the list
        questions_list.append(question_obj)
        
    print("Final List :", questions_list)
    return questions_list  # Return as a list of dictionaries



def classifyUser(context):
    prompt = f"""
    We had given user few MCQ Questions with 4 options. Below is the Response of Answers we got from the user
    
    User Response : {context}
    
    Please classify user based on User Interest and Response.
    
    Important : Give just one word answer in your Response.
    
    """
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = completion.choices[0].message.content
        
        print("User Classify Data :",result)
        return result
    except Exception as e:
        print(f"Error while calling OpenAI API: {e}")
        return None

def generate_mcq_from_content(title,context):
    # Define a prompt that asks OpenAI to generate MCQs based on website content
    prompt = f"""
        Objective:
        Generate 5 meaningful multiple-choice questions (MCQs) with 4 options based on the given website's context. The questions and options should aim to classify the visitor's intent into categories such as 'Highly Active', 'Active', 'Less Active', or 'New User' based on their choices. These are not right-or-wrong questions but instead should guide user categorization.

        Requirements:

        Focus on the website's main products, services, or categories to craft the questions and options.
        Avoid repeating questions or options. Each question should provide a distinct perspective.
        Frame the options in a way that reflects user preferences or behavior, making it possible to infer activity levels based on their selection.
        Do not include any special characters (e.g., !, ?, ").
        Keep the questions user-friendly and related to what the visitor might choose or be interested in.
        Input Provided:

        Page Title: {title}
        Page Context: {context}
        Output Format:

        Start directly with the questions without any headings or numbers (e.g., do not include "Question 1").
        Separate each question using two blank lines.
        Begin the options for each question with A., B., C., and D.
        Use ### at the start of each question for clarity.
    """

    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        question_data = completion.choices[0].message.content
        
        print("Ques Data :",question_data)
        
        processed_data = process_question_data(question_data)
        
        return processed_data
    except Exception as e:
        print(f"Error while calling OpenAI API: {e}")
        return None