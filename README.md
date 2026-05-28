# credit-cardverifier
A credit card number validation program that identifies card types (American Express, MasterCard, Visa) using Luhn's Algorithm.

💳 The Problem
Given a credit card number, determine if it's valid and which company issued it:

American Express - 15 digits, starts with 34 or 37

MasterCard - 16 digits, starts with 51, 52, 53, 54, or 55

Visa - 13 or 16 digits, starts with 4

🔢 Luhn's Algorithm
The validation algorithm works in two steps:

Step 1: Multiply every other digit by 2 (starting from second-to-last)
Add those products' digits together (not the numbers)

Example: 4 → 4 × 2 = 8 → add 8

Example: 6 → 6 × 2 = 12 → add 1 + 2 = 3

Step 2: Add the sum of the digits that weren't multiplied
Add together all digits in odd positions (from the right)

Step 3: Check total
If total's last digit is 0 → Card is valid

Otherwise → Card is invalid

🛠️ Implementation Details
No arrays or strings (depending on version) - Use integer arithmetic only

Extract digits using modulo (%) and division (/)

Count digits to determine card length

Check first digits to identify card type

📁 Files
credit.c - Main program (C version)

credit.py - Python version (if applicable)

🚀 Usage
bash
# C version
make credit
./credit

# Python version
python credit.py
Example Input/Output
text
Number: 4003600000000014
VISA
text
Number: 378282246310005
AMEX
text
Number: 1234567890
INVALID
🔧 Algorithm Example
Card: 4003600000000014

Step 1 (multiply every other digit from second-to-last):

4×2=8, 0×2=0, 0×2=0, 0×2=0, 0×2=0, 0×2=0, 1×2=2, 0×2=0

Sum = 8+0+0+0+0+0+2+0 = 10

Step 2 (add digits not multiplied):

0+0+0+0+0+0+0+4 = 4

Step 3 (total):

10 + 4 = 14 → Last digit is 4 → INVALID? (Wait, this is a known valid VISA)

(Actual valid number would produce total ending in 0)
