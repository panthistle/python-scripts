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

# RECURSION FUNCTION LOGIC (steps for n=3, k=2):
# main loop 1st iteration: i = 0
# 1st call (subloop si): c[1], si=1
# 2nd call (subloop ti): c[1,2], ti=2
# jump to c[1], next ti=3, end of subloop ti
# back to 1st call: c[1,3], si=2
# jump to c[1], next si=3, end of subloop si
# main loop 2nd iteration: i = 1
# 1st call (subloop si): c[2], si=2
# 2nd call (subloop ti): c[2, 3], ti=3
# jump to c[2], next ti=3, end of subloop ti
# next si=3, end of subloop si
# main loop 3rd iteration: i = 2
# 1st call (subloop si): c[3], si=3, end of subloop si
# next i=3, end of main loop

