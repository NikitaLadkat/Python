def sentence(line):
    r = line.capitalize()
    quest = ("how","why","whom")
    if line.startswith(quest):
        return("{}?".format(r))
    else:
        return("{}.".format(r))


result=[]
while True:
    user_input = input("Say Something :")

    if user_input == "\end":
        break
    else :
        result.append(sentence(user_input))

print("".join(result))





