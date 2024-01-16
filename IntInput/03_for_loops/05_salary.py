tabs_open = int(input())
salary = float(input())
facebook = 150
instagram = 100
reddit = 50
for i in range(tabs_open):
    site_name = input()
    if site_name == "Facebook":
        salary -= facebook
    elif site_name == "Instagram":
        salary -= instagram
    elif site_name == "Reddit":
        salary -= reddit
if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(f"{int(salary)}")
