yearly_payment = int(input())

shoes = yearly_payment - 40/100 * yearly_payment
clothes = shoes - 20/100 * shoes
ball = 1/4 * clothes
accessories = 1/5 * ball

price = shoes + clothes + ball + accessories + yearly_payment
print(price)