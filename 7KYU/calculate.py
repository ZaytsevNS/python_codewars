def calculate(num1, operation, num2): 
    operation_list = ['+', '-', '*', '/']
    try:
        for i in operation:
            if i in operation_list:
                if i == '+':
                    return num1 + num2
                elif i == '-':
                    return num1 - num2
                elif i == '*':
                    return num1 * num2
                return num1 / num2
            return None
    except:
        return None