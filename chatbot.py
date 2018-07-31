# --- Define your functions below! ---
def intro():
    print()
    print("Welcome to the ChatBot!")
def greeting():
    print()
    print("Let's have a deep conversation!")
def dating():
    print()
    print("Unfortunately, I am incapable of that D;")
    print("I can do other stuff")
    rep = input("Soooooo, come here often?")
    print()
    print("I was talking with your cousin >:")
def ivi(response, all_ivi):
    if response in all_ivi :
        return True
    else :
        return False

dating_prompt = ["Hello ;)", "love me", "Come here often?", "I need a partner in crime"]
# --- Put your main program below! ---
def main():
    valid_input = ["Hi!", "Hello ;)", "love me", "Come here often?", "I need a partner in crime", "hi", "hey"]
    intro()
    while True :
        answer = input("(What will you say?) ")
        if ivi(answer, valid_input) :
            if answer == "Hi!" or "hi" or "hey":
                greeting()
            elif answer in dating_prompt :
                dating()
        else:
            print()
            print("Sorry! I didn't catch that...Try saying 'Hi!' or")
            for vi in valid_input:
                print(vi)
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
