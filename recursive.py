def recursive(list, target):
    if len(list) == 0: #check if list exists
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target: #if my list midpoint already == target just return True
            return True
        else:
            if list[midpoint] < target: #Ex: 5 < 8 -- True
                return recursive(list[midpoint+1:], target) 
            else:
                return recursive(list[:midpoint], target)

def verify(result):
    print("target found: ", result)

numbers = [1,2,3,4,5,6,7,8,9]
result = recursive(numbers, 12)
verify(result)

result = result = recursive(numbers, 6)
verify(result)

