"""
Ask user for their scores and adds them to list,
until they enter a negative score, then prints highest score.
"""

scores = []
score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))
print("Your highest score is", max(scores))
