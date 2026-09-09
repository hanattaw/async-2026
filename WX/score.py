import sys
def evaluate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 80:
        return "Excellent"
    elif score >= 50 and score < 80:   
        return "Pass"
    elif score < 50:
        return "Fail"
    pass

def main():
    test_score = 85
    result = evaluate_grade(test_score)
    print(f"Score: {test_score} -> Grade: {result}")

if __name__ == "__main__":
    main()
