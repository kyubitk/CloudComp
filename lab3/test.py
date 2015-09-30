var = raw_input("Enter Word: ")
word = var
is_palindrome = word.find(word[::-1])
if is_palindrome == 0:
  print("True")
else:
  print("false")
