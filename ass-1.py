import random
import re

class Chatbot:
    def __init__(self):
        self.responses = {
            "hi": ["Hello!", "Hi there!", "Greetings!"],
            "how are you?": ["I'm just a program, but thanks for asking!", "Doing well, how about you?"],
            "bye": ["Goodbye!", "See you later!", "Take care!"],
        }

    def generate_table(self, number, limit=10):
        """Generate multiplication table for a given number"""
        table = f"\nMultiplication table for {number}:\n"
        for i in range(1, limit + 1):
            table += f"{number} x {i} = {number * i}\n"
        return table

    def generate_reverse_table(self, number, limit=10):
        """Generate reverse multiplication table for a given number"""
        table = f"\nReverse multiplication table for {number}:\n"
        for i in range(limit, 0, -1):
            table += f"{number} x {i} = {number * i}\n"
        return table

    def do_math(self, expression):
        """Perform basic math operations"""
        try:
            # Replace 'plus' with '+', 'minus' with '-', etc.
            expr = expression.lower()
            expr = expr.replace(' plus ', ' + ').replace(' minus ', ' - ')
            expr = expr.replace(' times ', ' * ').replace(' divided by ', ' / ')
            expr = expr.replace('÷', '/').replace('×', '*').replace('−', '-')
            
            # Extract the calculation part
            numbers = re.findall(r'[\d.]+|[+\-*/]', expr)
            if not numbers:
                return "Please provide a valid math expression. Example: '5 plus 3' or '10 times 2'"
            
            # Evaluate the expression safely
            result = eval(''.join(numbers))
            return f"Result: {result}"
        except:
            return "Invalid math expression. Try: '5 plus 3', '10 minus 2', '4 times 5', '20 divided by 4'"

    def count(self, numbers):
        """Count from one number to another"""
        try:
            if len(numbers) < 2:
                return "Please provide two numbers. Example: 'count from 1 to 10' or 'count 5 to 15'"
            
            start = int(numbers[0])
            end = int(numbers[1])
            
            if start > end:
                count_list = list(range(start, end - 1, -1))
            else:
                count_list = list(range(start, end + 1))
            
            return f"Counting from {start} to {end}:\n{', '.join(map(str, count_list))}"
        except:
            return "Please provide valid numbers for counting."

    def get_response(self, user_input):
        user_input_lower = user_input.lower()
        
        # Check if user is asking to count
        if "count" in user_input_lower:
            numbers = re.findall(r'\d+', user_input)
            if numbers:
                return self.count(numbers)
            else:
                return "Please provide numbers to count. Example: 'count from 1 to 10'"
        
        # Check for math operations
        if any(op in user_input_lower for op in ["plus", "minus", "times", "divided", "+", "-", "*", "/"]):
            return self.do_math(user_input)
        
        # Check if user is asking for a reverse table
        if "reverse" in user_input_lower and "table" in user_input_lower:
            # Extract number from input using regex
            numbers = re.findall(r'\d+', user_input)
            if numbers:
                number = int(numbers[0])
                return self.generate_reverse_table(number)
            else:
                return "Please provide a number for the reverse table. Example: 'reverse table 5'"
        
        # Check if user is asking for a regular table
        if "table" in user_input_lower:
            # Extract number from input using regex
            numbers = re.findall(r'\d+', user_input)
            if numbers:
                number = int(numbers[0])
                return self.generate_table(number)
            else:
                return "Please provide a number for the table. Example: 'table 5' or 'show table of 7'"
        
        return random.choice(self.responses.get(user_input_lower, ["Sorry, I don't understand that."]))

def main():
    bot = Chatbot()
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    print("Commands:")
    print("  - Math: '5 plus 3', '10 minus 2', '4 times 5', '20 divided by 4'")
    print("  - Counting: 'count from 1 to 10' or 'count 5 to 15'")
    print("  - Tables: 'table 5' or 'reverse table 5'\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()