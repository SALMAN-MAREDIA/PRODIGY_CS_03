import re

def check_password_strength(password):
    feedback = []

    if len(password) < 8:
        feedback.append("❌ Must be at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        feedback.append("❌ Add an uppercase letter.")
    if not re.search(r"[a-z]", password):
        feedback.append("❌ Add a lowercase letter.")
    if not re.search(r"\d", password):
        feedback.append("❌ Add a number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("❌ Add a special character.")

    return feedback

# 🔁 Loop until password is strong
while True:
    password = input("Enter your password: ")
    feedback = check_password_strength(password)

    if not feedback:
        print("✅ Strong password!")
        break
    else:
        print("\n⚠️ Weak password. Please fix the following:")
        for f in feedback:
            print(f)
        print("🔁 Try again.\n")
