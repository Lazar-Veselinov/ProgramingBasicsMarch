from math import ceil

series = input()
duration_episode = int(input())
duration_break = int(input())

lunch_time = 1/8 * duration_break
rest_time = 1/4 * duration_break
free_time = duration_break - lunch_time - rest_time

if duration_episode <= free_time:
    print(f"You have enough time to "
          f"watch {series} and left with {ceil(free_time - duration_episode)}"
          f" minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need "
          f"{ceil(duration_episode - free_time)} more minutes.")