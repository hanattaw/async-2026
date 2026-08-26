import sys
def evaluate_grade(score):
    # --- เขียนโค้ดของนักเรียนในส่วนนี้ / Write your code here ---
    if score >= 80:
        return "Excellent"
    elif 50 <= score < 80:
        return "Pass"     
    else :
        return "Fail"

def main():
    test_score = 85
    result = evaluate_grade(test_score)
    print(f"Score: {test_score} -> Grade: {result}")

if __name__ == "__main__":
    main()
