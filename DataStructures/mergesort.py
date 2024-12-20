def merge_sort(list):
    """
    Returns a sorted list in ascending order
    Divide: Find the midpoint and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step
    """

    if len(list) <= 1: #stop condition para uma recursao, assim vai para a proxima
        return list

    left_half, right_half = split(list) #exemplo: lista [3,2,1,4] divide em 3,2 chamar o merge(left_half)
    left = merge_sort(left_half) #ai executa o split denovo o left se torna o 3 e o right se torna o 2, da para verificar pelo print
    right = merge_sort(right_half)
    
    return merge(left, right) #so vai ser executado quando o left, e o right chegarem a um tamanho de 1, se nao as funcoes ficam se chamando

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists, sorting them in the process
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left): 
        l.append(left[i])
        i += 1
    
    while j < len(right): 
        l.append(right[j])
        j += 1
    
    return l

tlist = [3, 4, 2, 1, 5, 6, 7, 8, 9, 0]
l = merge_sort(tlist)
print(l)
