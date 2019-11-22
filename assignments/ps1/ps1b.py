def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """
    try:
        max_weight = max(egg_weights)
    except ValueError:
        return sum(memo.values())
    if max_weight == target_weight:
        memo[max_weight] = target_weight
        return 1
    elif max_weight < target_weight:
        number_of_eggs = target_weight // max_weight
        memo[max_weight] = number_of_eggs
        available_egg_weights = egg_weights[:-1]
        new_target_weight = target_weight - (max_weight * number_of_eggs)
        return dp_make_weight(available_egg_weights, new_target_weight, memo)
    elif max_weight > target_weight:
        available_egg_weights = egg_weights[:-1]
        return dp_make_weight(available_egg_weights, target_weight, memo)

if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
