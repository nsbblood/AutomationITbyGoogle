import re

pattern = r"^Hello"  # Matches strings starting with "Hello"
matches = re.findall(pattern, "Hello, world!")
print(matches)

pattern = r"(Hello) (world)"  # Captures "Hello" and "world"
matches = re.findall(pattern, "Hello, world!")
print(matches)

pattern = r"\d+(?= dollars)"  # Matches numbers followed by " dollars"
amounts = re.findall(pattern, "I have 100 dollars and 50 dollars.")
print(amounts)

pattern = r"(\w+)@(\w+\.\w+)"
text = "john@example.com"
match = re.match(pattern, text)
if match:
    username = match.group(1)  # Extracts the username
    domain = match.group(2)  # Extracts the domain
    print(f"Username: {username}, Domain: {domain}")


emails = ["test@example.com", "invalid.email", "another@test.co.uk"]
print("\n--- Practice with emails ---")
for email in emails:
    # Match anything, then @, then anything
    is_email = bool(re.match(r".+@.+", email))
    print(f"{email}: {'Valid' if is_email else 'Invalid'}")