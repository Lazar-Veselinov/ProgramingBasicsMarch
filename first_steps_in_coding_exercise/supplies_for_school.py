number_packets_pens = int(input())
number_packets_markers = int(input())
liters_detergent = int(input())
percent_sale = int(input()) / 100

price_pens = 5.80
price_markers = 7.20
detergent = 1.20

price = number_packets_pens * price_pens + number_packets_markers * price_markers + liters_detergent * detergent
final_price = price - percent_sale * price
print(final_price)