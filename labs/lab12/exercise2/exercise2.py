score = float(input())
average_score = 0
score_count = 0
total_score = 0

while (score >= 0) and (score <= 100):
    score_count += 1
    total_score += score
    score = float(input())

if score_count == 0:
    score_count = 1
    average_score = total_score / score_count 
    score_count = 0
else:
    average_score = total_score / score_count 


print(score_count)
print(f"{total_score:.1f}")
print(f"{average_score:.2f}")
