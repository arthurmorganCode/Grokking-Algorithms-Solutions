def greedy_set_cover(universe, subsets):
    """
    Solve the set-covering problem using a greedy algorithm.

    :param universe: A set of all elements that need to be covered.
    :param subsets: A list of subsets of the universe.
    :return: A list of subsets that together cover the entire universe.
    """
    # List to store the selected subsets
    selected_subsets = []
    
    # While there are still elements in the universe that are not covered
    while universe:
        # Find the subset that covers the most uncovered elements
        best_subset = max(subsets, key=lambda s: len(s & universe))
        
        # Add the best subset to the selected list
        selected_subsets.append(best_subset)
        
        # Remove the covered elements from the universe
        universe -= best_subset
        
        # Remove the best subset from the list of subsets
        subsets.remove(best_subset)
    
    return selected_subsets

# Example usage:
universe = set([1, 2, 3, 4, 5])
subsets = [set([1, 2, 3]), set([2, 4]), set([3, 4]), set([4, 5])]

solution = greedy_set_cover(universe, subsets)
print("Selected subsets:", solution)
