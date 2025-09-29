num_rounds = int(input())
rounds_processed = 0
total_score = 0
final_score = 0 

for rounds in range(num_rounds):
    round_score = float(input())
    if round_score > 100:
        round_score = round_score * 1.2
    else:
        round_score = round_score

    final_score += round_score
    rounds_processed += 1

print(f"{final_score}")
print(rounds_processed)