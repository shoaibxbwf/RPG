import random
import string
import time

try:
    import pyperclip
    clipboard_available = True
except ImportError:
    clipboard_available = False

def generate_password():
    # --------- Banner ---------
    print("🔒🔒🔒 Welcome to Secure Password Generator 🔒🔒🔒\n")

    # --------- User Choices ---------
    length = int(input("✏️ Enter the password length (e.g., 12): "))

    include_numbers = input("🔢 Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("✨ Include special symbols? (y/n): ").lower() == 'y'
    include_uppercase = input("🔠 Include uppercase letters? (y/n): ").lower() == 'y'

    # --------- Build Character Pool ---------
    characters = string.ascii_lowercase

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("⚠️ No character types selected. Defaulting to lowercase letters.")
        characters = string.ascii_lowercase

    # --------- Generate Password ---------
    print("\n🔄 Generating your secure password...")
    time.sleep(1)

    password = ''.join(random.choice(characters) for _ in range(length))

    print("\n✅ Your generated password is:")
    print(f"🔑 {password}")

    # --------- Strength Checker ---------
    if length < 6:
        strength = "Weak 😟"
    elif 6 <= length < 10:
        strength = "Medium 🙂"
    else:
        strength = "Strong 💪"

    print(f"\n🔎 Password Strength: {strength}")

    # --------- Ask if the User Wants to Copy to Clipboard ---------
    if clipboard_available:
        copy_choice = input("\n📋 Do you want to copy the password to clipboard? (y/n): ").lower()
        if copy_choice == 'y':
            pyperclip.copy(password)
            print("✅ Password copied to clipboard!")
    else:
        print("📋 (Clipboard feature is not available.)")

    print("\n🎉 Thank you for using Secure Password Generator! Stay safe! 🔥")

def main():
    while True:
        generate_password()
        
        # Ask the user if they want to generate another password
        generate_again = input("\n🔄 Do you want to generate another password? (y/n): ").lower()
        if generate_again != 'y':
            print("👋 Exiting... Thank you for using the Password Generator!")
            break

# Run the program
if __name__ == "__main__":
    main()
