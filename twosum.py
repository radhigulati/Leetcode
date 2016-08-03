def pair_sum(arr,k):

    if len(arr)<2:
        return

    # Sets for tracking
    #seen = set()
    seen = []
    #output = set()
    output = []
    #output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k-num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.append(num)

        else:
            # Add a tuple with the corresponding pair
            output.append(target)
            output.append(num)

    return output

pair_sum([1,3,6,6],4)