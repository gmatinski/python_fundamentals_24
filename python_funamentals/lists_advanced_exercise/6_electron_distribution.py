number_of_electrons = int(input())
shell_list = []
for shell in range(1, number_of_electrons + 1):
    max_current_shell = 2 * shell ** 2
    if number_of_electrons >= max_current_shell:
        shell_list.append(max_current_shell)
        number_of_electrons -= max_current_shell
    else:
        shell_list.append(number_of_electrons)
        break
print(shell_list)
