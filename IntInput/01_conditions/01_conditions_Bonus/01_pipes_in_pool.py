v_pool = int(input())  # Обем на басейна в литри
pipe_one = int(input())  # дебит на първата тръба за час
pipe_two = int(input())  # дебит на втората тръба за час
hours_gone = float(input())  # часовете които работникът отсъства

pipe_one_fill = pipe_one * hours_gone  # Колко е запълнила тръбата за часовете в които бачкатора го е нямало
pipe_two_fill = pipe_two * hours_gone  # Колко е запълнила тръбата за часовете в които бачкатора го е нямало
both_pipes = pipe_one_fill + pipe_two_fill  # Колко са запълнили двете тръби за това време

first_contributed = pipe_one_fill / (both_pipes / 100)  # процент с колко е допринесла тръбата за запълването
second_contributed = pipe_two_fill / (both_pipes / 100)  # процент с колко е допринесла тръбата за запълването
percent_full = both_pipes / (v_pool / 100)       # колко процента е пълен басейна в момента

if both_pipes <= v_pool:         # ако 2те тръби са напълнили по малко от обема >>>
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: "
          f"{first_contributed:.2f}%. Pipe 2: {second_contributed:.2f}%.")

else:  # ако 2те тръби са надвишили обема на басейна
    print(f"For {hours_gone} hours the pool overflows with {both_pipes - v_pool:.2f} liters.")
