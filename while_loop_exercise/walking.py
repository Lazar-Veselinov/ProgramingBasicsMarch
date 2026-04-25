
count_steps = 0
GOAL_STEPS_DAY = 10000

while count_steps < GOAL_STEPS_DAY:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        count_steps += steps
        break

    count_steps += int(steps)

if count_steps >= GOAL_STEPS_DAY:
    print(f"Goal reached! Good job!")
    print(f"{count_steps - 10000} steps over the goal!")
else:
    print(f"{10000 - count_steps} more steps to reach goal.")