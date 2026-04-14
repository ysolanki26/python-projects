"""
Project: Smart Password Strength Analyzer (OOP Version)
Author: Yashika Solanki

Description:
This project analyzes password strength using Object-Oriented Programming.
It evaluates password security based on multiple criteria and generates
a detailed security report including score, risk level, and suggestions.
"""

import re


class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.feedback = []
        self.common_passwords = ["123456", "password", "qwerty", "abc123"]

    def check_length(self):
        if len(self.password) >= 12:
            self.score += 25
        elif len(self.password) >= 8:
            self.score += 15
        else:
            self.feedback.append("Increase length (at least 8–12 characters)")

    def check_lowercase(self):
        if re.search("[a-z]", self.password):
            self.score += 15
        else:
            self.feedback.append("Add lowercase letters")

    def check_uppercase(self):
        if re.search("[A-Z]", self.password):
            self.score += 15
        else:
            self.feedback.append("Add uppercase letters")

    def check_numbers(self):
        if re.search("[0-9]", self.password):
            self.score += 15
        else:
            self.feedback.append("Add numbers")

    def check_special_characters(self):
        if re.search("[@#$%^&*]", self.password):
            self.score += 20
        else:
            self.feedback.append("Add special characters (@#$%^&*)")

    def check_common_password(self):
        if self.password.lower() in self.common_passwords:
            return True
        return False

    def check_patterns(self):
        if re.search(r"(123|abc|aaa)", self.password.lower()):
            self.feedback.append("Avoid predictable patterns like 123, abc, aaa")
            self.score -= 10

    def calculate_strength(self):
        # Run all checks
        if self.check_common_password():
            return "Very Weak", 0, ["Common password detected!"], "Instantly crackable", "High Risk"

        self.check_length()
        self.check_lowercase()
        self.check_uppercase()
        self.check_numbers()
        self.check_special_characters()
        self.check_patterns()

        # Score limit
        self.score = max(0, min(self.score, 100))

        # Determine strength
        if self.score < 40:
            strength = "Weak"
            crack_time = "Seconds"
            risk = "High Risk"
        elif self.score < 70:
            strength = "Medium"
            crack_time = "Hours to Days"
            risk = "Medium Risk"
        else:
            strength = "Strong"
            crack_time = "Years"
            risk = "Low Risk"

        return strength, self.score, self.feedback, crack_time, risk


class PasswordReport:
    def __init__(self, strength, score, feedback, crack_time, risk):
        self.strength = strength
        self.score = score
        self.feedback = feedback
        self.crack_time = crack_time
        self.risk = risk

    def display(self):
        print("\n========= PASSWORD SECURITY REPORT =========")
        print("Strength       :", self.strength)
        print("Score          :", self.score, "/100")
        print("Risk Level     :", self.risk)
        print("Crack Time     :", self.crack_time)

        if self.feedback:
            print("\nSuggestions to Improve:")
            for item in self.feedback:
                print("-", item)

        print("===========================================")


def main():
    password = input("Enter your password: ")

    analyzer = PasswordAnalyzer(password)
    result = analyzer.calculate_strength()

    report = PasswordReport(*result)
    report.display()


if __name__ == "__main__":
    main()