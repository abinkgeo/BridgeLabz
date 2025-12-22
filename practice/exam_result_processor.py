def exam_result(marks):
    for m in marks:
        if m < 35:
            return "FAIL"
    avg = sum(marks) / 5
    if avg >= 75:
        return "DISTINCTION"
    return "PASS"

marks = list(map(int, input().split()))
print(exam_result(marks))
