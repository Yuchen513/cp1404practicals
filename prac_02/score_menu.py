def main():
    score = get_valid_score()
    choice = ""
    while choice!= "Q":
        print("\nMenu:")
        print("(G) Get valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Enter your choice: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        elif choice!= "Q":
            print(" End of the program ")
    else:
        print("Farewell! See you next time!")

def get_valid_score():
    score = float(input("Enter a score between 0-100: "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score during 0-100.")
        score = float(input("Enter a score between 0-100: "))
    return score

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * int(score))

main()