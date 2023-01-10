def check_answer(answer):
    answer = str(answer)
    if answer.lower().replace(" ","") in ["42", "forty-two","fortytwo"]:
        print("yes")
    else:
        print("no")


answer = input("What is the answer to the Great Question of Life, the Universe and Everything? " )

check_answer(answer)
