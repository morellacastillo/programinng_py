def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

users_input =input()
output= convert(users_input)
print(output)