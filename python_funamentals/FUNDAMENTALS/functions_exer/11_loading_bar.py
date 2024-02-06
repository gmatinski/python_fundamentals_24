def progress(bar_current_value):
    if bar_current_value == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{bar_current_value}% [{'%'* (bar_current_value // 10)}{'.' * (10 - bar_current_value // 10)}]\n" \
           f"Still loading..."


value_bar = int(input())
print(progress(value_bar))