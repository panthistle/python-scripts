def total_combinations(n, k):
    nc, kf = 1, 1
    for i in range(1, k + 1):
        kf *= i
    for i in range(n - k + 1, n + 1):
        nc *= i
    if not kf:
        return 0
    return int(nc / kf)


def find_combinations(nset, k, start_index, curr, results):
    # Base case: a combination is complete
    if len(curr) == k:
        # add current_combination to results
        results.append(curr.copy())
        return

    # Recursive step
    for i in range(start_index, len(nset)):
        # Add current number to the combination
        curr.append(nset[i])
        # Recurse with next number
        find_combinations(nset, k, i + 1, curr, results)
        # Remove last added number to try the next one
        curr.pop()
    return results


# Ranges
n = 12
k = 3

# # total unique combinations
# ncombos = total_combinations(n, k)
# print(ncombos)

# # all combinations in list of lists
# nset = [i + 1 for i in range(n)]
# results = find_combinations(nset, k, 0, [], [])
# print(len(results), "\n")
# print(results)
