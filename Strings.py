# Q1 Task 1

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
  for keyword in keywords:
    review = review.replace(keyword, keyword.upper())
  print(review)

#Task 2 

def sentiment_tally(review, positive_words, negative_words):
  """
  This function tallies the number of positive and negative words in a review.

  Args:
      review: The text of the product review.
      positive_words: A list of positive words.
      negative_words: A list of negative words.

  Returns:
      A dictionary containing the count of positive and negative words in the review.
  """

  positive_count = 0
  negative_count = 0

  # Split the review into words
  words = review.split()

  for word in words:
    # Convert the word to lowercase to handle case-insensitive comparisons
    word = word.lower()
    if word in positive_words:
      positive_count += 1
    elif word in negative_words:
      negative_count += 1

  return {"positive": positive_count, "negative": negative_count}

# Example usage
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for review in reviews:
  sentiment = sentiment_tally(review, positive_words, negative_words)
  print(f"Review: {review}")
  print(f"Sentiment: Positive - {sentiment['positive']}, Negative - {sentiment['negative']}")
  print()

#Task 3

def summarize_review(review):
  """
  This function creates a summary of a review by taking the first 30 characters and adding "...".

  Args:
      review: The text of the product review.

  Returns:
      A string containing the summarized review.
  """
  # Split the review into words
  words = review.split()

  # Truncate the review to 30 characters while considering word boundaries
  summary_length = 30
  if len(review) < summary_length:
    return review
  else:
    # Find the last space before the 30th character
    last_space = review.rfind(" ", 0, summary_length)
    if last_space == -1:
      # No space found within the first 30 characters, truncate at the character limit
      return review[:summary_length] + "..."
    else:
      # Truncate at the last space found before the 30th character
      return review[:last_space] + "..."

# Example usage
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for review in reviews:
  summary = summarize_review(review)
  print(f"Review: {review}")
  print(f"Summary: {summary}")
  print()

#Q Task

def validate_name_length(name):
  """
  This function validates the length of a name (first or last).

  Args:
      name: The name string to validate.

  Returns:
      True if the name is at least 2 characters long, False otherwise.
  """
  if len(name) < 2:
    print(f"Error: Your {name} name must be at least 2 characters long.")
    return False
  else:
    return True

def get_user_name(name_type):
  """
  This function prompts the user for their name (first or last) and validates its length.

  Args:
      name_type: A string indicating the type of name (e.g., "first", "last").

  Returns:
      The user's name if valid, None otherwise.
  """
  while True:
    name = input(f"Enter your {name_type} name: ")
    if validate_name_length(name):
      return name

# Get user's first and last name
first_name = get_user_name("first")
if first_name:
  last_name = get_user_name("last")
  if last_name:
    print(f"Hello, {first_name} {last_name}!")

#Task 2

def check_password_complexity(password):
  """
  This function checks the complexity requirements of a password.

  Args:
      password: The password string to validate.

  Prints:
      A message indicating if the password meets the complexity requirements or not.
  """
  has_uppercase = False
  has_lowercase = False
  has_number = False

  if len(password) < 8:
    print("Password must be at least 8 characters long.")
    return

  for char in password:
    if char.isupper():
      has_uppercase = True
    elif char.islower():
      has_lowercase = True
    elif char.isdigit():
      has_number = True

  if not (has_uppercase and has_lowercase and has_number):
    print("Password must contain at least one uppercase letter, one lowercase letter, and one number.")

# Example usage
password = input("Enter your password: ")
check_password_complexity(password)

#Task 3

import re

def is_valid_email(email):
  """
  This function validates an email address format using regular expressions.

  Args:
      email: The email address string to validate.

  Returns:
      True if the email is in a valid format, False otherwise.
  """
  email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
  return re.match(email_regex, email) is not None

def get_user_email():
  """
  This function prompts the user for their email address and validates its format.

  Returns:
      The user's email address if valid, None otherwise.
  """
  while True:
    email = input("Enter your email address: ")
    if is_valid_email(email):
      return email.lower()  # Convert email to lowercase for case-insensitive storage
    else:
      print("Invalid email format. Please enter a valid email address.")

# Get user's email address
email = get_user_email()
if email:
  print(f"Your email address is: {email}")

# Q3 Task 1

def parse_command(user_input):
  """
  This function parses user input to identify predefined commands.

  Args:
      user_input: The text string entered by the user.

  Prints:
      A message corresponding to the identified command or a generic message 
      if no command is found.
  """
  commands = {"help": "I can help you with various tasks. Try 'help topics' for a list of help topics.",
              "issue": "Let's troubleshoot the issue. Describe the problem you're facing.",
              "contact support": "For complex issues, you can contact our support team at support@example.com."}

  # Convert user input to lowercase for case-insensitive matching
  user_input = user_input.lower()

  # Find the first word in the user input (potential command)
  command = user_input.split()[0]

  if command in commands:
    print(commands[command])
  else:
    print("I didn't understand that command. Try 'help' for a list of available commands.")

# Example usage
while True:
  user_input = input("How can I help you today? ")
  parse_command(user_input)
  # Optionally, add functionality to exit the loop based on specific user input

#Task 2

def parse_command(user_input):
  """
  This function parses user input to identify predefined commands and categorize issues.

  Args:
      user_input: The text string entered by the user.

  Prints:
      A message corresponding to the identified command or a generic message 
      if no command is found. For "issue" commands, it also attempts to 
      categorize the issue.
  """
  commands = {"help": "I can help you with various tasks. Try 'help topics' for a list of help topics.",
              "issue": "Let's troubleshoot the issue. Describe the problem you're facing.",
              "contact support": "For complex issues, you can contact our support team at support@example.com."}

  # Convert user input to lowercase for case-insensitive matching
  user_input = user_input.lower()

  # Find the first word in the user input (potential command)
  command = user_input.split()[0]

  if command in commands:
    print(commands[command])
    if command == "issue":
      # Identify issue category based on keywords
      issue_categories = {"login": ["login", "signin", "authentication"],
                          "performance": ["slow", "performance", "lag"],
                          "error": ["error", "crash", "bug"]}
      for category, keywords in issue_categories.items():
        for keyword in keywords:
          if keyword in user_input:
            print(f"  * Potential issue category: {category}")
            break  # Exit the inner loop after finding a matching keyword
  else:
    print("I didn't understand that command. Try 'help' for a list of available commands.")

# Example usage
while True:
  user_input = input("How can I help you today? ")
  parse_command(user_input)
  # Optionally, add functionality to exit the loop based on specific user input
