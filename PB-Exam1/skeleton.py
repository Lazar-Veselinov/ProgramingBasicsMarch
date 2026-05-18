minutes = int(input())
seconds = int(input())
length_track = float(input())
seconds_per_100_meters = int(input())

time = length_track / 100 * seconds_per_100_meters - length_track / 120 * 2.5
control = minutes * 60 + seconds

if time <= control:
    print(f"Marin Bangiev won an Olympic quota!\n"
          f"His time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {time - control:.3f} second slower.")