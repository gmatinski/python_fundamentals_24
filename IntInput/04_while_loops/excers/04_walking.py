goal_daily = 10000
steps = input()
overall_counter = 0

while goal_daily > overall_counter:
    if steps.isdigit():
        counter_steps = int(steps)
        overall_counter += counter_steps
        if overall_counter >= goal_daily:
            print(f"Goal reached! Good job!\n{overall_counter - goal_daily} steps over the goal!")
            break
    if steps == "Going home":
        steps_to_home = int(input())
        overall_counter += steps_to_home
        if overall_counter < goal_daily:
            print(f"{goal_daily - overall_counter} more steps to reach goal.")
            break
        else:
            print(f"Goal reached! Good job!\n{overall_counter - goal_daily} steps over the goal!")
            break
    steps = input()
