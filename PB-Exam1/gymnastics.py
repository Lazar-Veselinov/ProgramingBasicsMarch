country = input()
tool = input()

if country == "Russia":
    if tool == "ribbon":
        score = 9.1 + 9.4
    elif tool == "hoop":
        score = 9.3 + 9.8
    elif tool == "rope":
        score = 9.6 + 9
elif country == "Bulgaria":
    if tool == "ribbon":
        score = 9.6 + 9.4
    elif tool == "hoop":
        score = 9.55 + 9.75
    elif tool == "rope":
        score = 9.5 + 9.4
elif country == "Italy":
    if tool == "ribbon":
        score = 9.2 + 9.5
    elif tool == "hoop":
        score = 9.45 + 9.35
    elif tool == "rope":
        score = 9.7 + 9.15

percent_left = 100 - (score/ 20 * 100)

print(f"The team of {country} get {score:.3f} on {tool}.\n"
      f"{percent_left:.2f}%")