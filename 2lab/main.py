def check_brackets(s):
    # Словарь соответствий скобок
    brackets = {')': '(', ']': '[', '}': '{'}
    # Стек для отслеживания открывающихся скобок
    stack = []
    
    # Проходим по каждому символу в строке
    for i, char in enumerate(s, 1):  # начинаем нумерацию с 1
        if char in brackets.values():
            # Если это открывающаяся скобка - добавляем в стек с позицией
            stack.append((char, i))
        elif char in brackets:
            # Если это закрывающаяся скобка
            if not stack:
                # Стек пуст - нет соответствующей открывающей скобки
                return i
            if stack[-1][0] != brackets[char]:
                # Несоответствие скобок
                return i
            # Скобки совпали - удаляем открывающую из стека
            stack.pop()
    
    # После обработки всей строки проверяем стек
    if stack:
        # В стеке остались незакрытые скобки
        return stack[0][1]  # позиция первой незакрытой скобки
    else:
        return "ok"

# Пример
test_string = "(a)(b(c[d{e{r}f{g}s}w]r)tasd)"
result =check_brackets(test_string)
print(f"input - {test_string}")
print(f"output - {result}")
