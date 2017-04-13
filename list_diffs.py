def diffs(current, target):
    """ Returns two arrays, the first with elements in target but not 
    current (additions to the array), the second with elements in 
    current but not target(deletions from the array)
    """
    
    additions = [val for val in target if val not in current]
    deletions = [val for val in current if val not in target]

    return additions, deletions

if __name__ == '__main__':
    current = [1, 3, 5, 6, 8, 9 ]
    target = [1, 2, 5, 7, 9]
    print("current: " + str(current))
    print("target: " + str(target))
    additions, deletions = diffs(current, target)
    print("additions: " + str(additions))
    print("deletions: " + str(deletions))

