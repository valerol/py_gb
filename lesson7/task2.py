def print_operation_table(operation="", num_rows=6, num_columns=6):
    print(''.join(map(str, list(map(\
        lambda y: ' '.join(map(str, [y] + list(map(\
            lambda x: x if y == 1 else round(operation(x, y)),\
            range(2, num_columns + 1))) + ['\n'])),\
        range(1, num_rows + 1))))))

exec(input("Enter operation funtion: "))
