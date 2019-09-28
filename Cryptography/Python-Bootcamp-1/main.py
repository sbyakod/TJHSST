profanity = open("profanity.txt").read().split()
token, oldToken = "", None

while token != oldToken:
  oldToken = token
  token = input("Enter input: ")
  print(token)
  print(token.count("e"))
  print(token[::-1])
  if token == "DOUBLE":
    print(token * 2)
  print(token.replace("s","*"))
  print(token.upper())
  if len(token) > 50:
    print("TOO LONG")
  if any(word == token.lower() for word in profanity):
    print("Be Nice")