url = "https://www.example.com"
if re.match(r"^(http|https)://www\.[a-z0-9.-]+\.[a-z]{2,4}$", url):
    print("Valid URL")
else:
    print("Invalid URL")