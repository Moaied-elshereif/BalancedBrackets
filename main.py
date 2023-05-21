def check_balance(Str):
    # list for storing opening brackets
    lst = []

    # Loop for checking the string and store to the stack
    for char in Str:
        #
        if char == '{' or char == '(' or char == '[':
            lst.append(char)

        elif char == '}' or char == ')' or char == ']':
            if len(lst) == 0:
                return False
            top_element = lst.pop()
            # function to compare whether two brackets are corresponding each other
            if not compare(top_element, char):
                return False
    # Check that list is empty or not
    if len(lst) != 0:
        return False

    return True


# Function to check if two corresponding brackets are matched or not.
def compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False


print(check_balance("[[()]]"))

print(check_balance("[{()}]"))

print(check_balance("[{)]"))

print(check_balance("[({)}]"))
