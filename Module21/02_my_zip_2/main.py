def my_zip(*args):
    result = [tuple(struct[i] for struct in map(list, args)) for i in range(min(len(element) for element in args))]
    return result


#print(my_zip([1,2,3], ('a','b','c')))