def sort_list_by_last_element(tuples_list):
    """
    Sort a list of non-empty tuples in increasing order based on the last element of each tuple.
    """
    return sorted(tuples_list, key=lambda x: x[-1])


# Example usage
tuples_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort_list_by_last_element(tuples_list)
print(sorted_list)
