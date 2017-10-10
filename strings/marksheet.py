# Output Format:Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
# Sample Input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output
# 56.00
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    print float(str(round(sum(student_marks[query_name])/(len(student_marks[query_name])),2)))
