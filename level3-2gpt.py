def solution(l):
    # Step 1: Pre-processing
    sorted_indices = sorted(range(len(l)), key=lambda x: l[x])
    l_sorted = [l[i] for i in sorted_indices]

    triples = []

    # Step 2: Finding Triples
    count = 0
    n = len(l_sorted)
    for i in range(n):
        for j in range(i+1, n):
            if l_sorted[j] % l_sorted[i] == 0:  # l[i] divides l[j]
                for k in range(j+1, n):
                    if l_sorted[k] % l_sorted[j] == 0:  # l[j] divides l[k]
                        count += 1

    return count
print(solution([6,5,4,3,2,1]), solution([1,1,1]))