buffer_text = ""
def palindrome(og_text):
    global buffer_text
    if len(og_text) == 0:
        return buffer_text
    else:
        buffer_text = buffer_text + og_text[-1]
        return palindrome(og_text[:-1])

og_text = input("Enter a string: ")
revrse_text = palindrome(og_text)

if og_text == buffer_text:
    print("Yes. This text is a palindrome.")
else:
    print("This is not a palindrome.")



