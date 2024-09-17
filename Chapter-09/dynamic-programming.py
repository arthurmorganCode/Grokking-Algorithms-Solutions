def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create a matrix (table) to store LCS values
    L = [[0] * (n + 1) for i in range(m + 1)]

    # Build the L[m+1][n+1] matrix in a bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS for X[0..n-1] and Y[0..m-1]
    index = L[m][n]

    # Create the LCS string from the matrix
    lcs = [""] * (index + 1)
    lcs[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        # If characters are the same, they are part of the LCS
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If characters are not the same, move in the direction of the larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)

# Given strings
X = "blue"
Y = "clues"

# Calculate and display LCS
result = lcs(X, Y)
print(f"The longest common subsequence between '{X}' and '{Y}' is: '{result}'")
