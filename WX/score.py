import sys
def evaluate_grade(score):
    if score >= 80:
        result = "Excellent"
    elif 50 <= score <80:
        result = "Pass"
    elif score < 50:
        result = "Fail"
    return result
    pass

def main():
    test_score = 85
    result = evaluate_grade(test_score)
    print(f"Score: {test_score} -> Grade: {result}")

if __name__ == "__main__":
    main()