def find_best_subset(universe,subsets):
    best_subset = None
    max_covered_elements = -1
    for subset in subsets:
        covered_elements = len(subset & universe)
        if covered_elements > max_covered_elements:
            max_covered_elements = covered_elements
            best_subset = subset

    return best_subset



def greedy_set_cover(universe, subsets):

    selected_subsets = []
    while universe:
        best_subset = find_best_subset(universe, subsets)
        selected_subsets.append(best_subset)
        universe -= best_subset
        subsets.remove(best_subset)

    return selected_subsets


# Example usage:
universe = set([1, 2, 3, 4, 5])
subsets = [set([1, 2, 3]), set([2, 4]), set([3, 4]), set([4, 5])]

solution = greedy_set_cover(universe, subsets)
print("Selected subsets:", solution)