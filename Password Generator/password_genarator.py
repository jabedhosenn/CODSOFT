import string
import random


def main():
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))

    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Please enter the length of the password (minimum 8): "))
            if length < 8:
                print("Password length should be at least 8.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"Generated Password: {''.join(random.sample(s, length))}")


if __name__ == "__main__":
    main()
