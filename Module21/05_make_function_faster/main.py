def calculating_math_func(data, checklist):
        if data in checklist.keys():
            result = checklist[data]
        else:
            result = 1
            for index in range(1, data + 1):
                result *= index
                checklist[data] = result
        result /= data ** 3
        result = result ** 10
        return result

checklist = {}

# Дальше идут просто проверки
#print(calculating_math_func(2, checklist))
#print(calculating_math_func(3, checklist))
#print(checklist)


