square_meters = float(input())
discount = 0.18
s_meters_price = 7.61
ss_meters = square_meters * s_meters_price
print(f"The final price is: {(square_meters * s_meters_price) - (discount * ss_meters)} The discount is:"
      f"{discount * ss_meters}")