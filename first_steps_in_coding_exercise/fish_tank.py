length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

obem = length * width * height
obem_v_litri = obem * 0.001
print(obem_v_litri - percent * obem_v_litri)