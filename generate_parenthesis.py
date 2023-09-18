# This is backtracking and recursion
def generateParenthesis(n):
    results = []
    def recurse_gen_parent(current, open_count, close_count):
        #print(results)
        # This is the base case of recursion where the length of the currnet is equal to 2*n then add it into results and return
        if len(current) == 2 * n:
            # Append the current combination of parentheses to the result
            results.append(current)
            return
        # This if condition makes sure that the open_count is not greater than the given n
        if open_count < n:
            recurse_gen_parent(current+"(", open_count+1, close_count)
        # This if condition makes sure that the close count is not greater than open count
        if close_count < open_count:
            recurse_gen_parent(current+")", open_count, close_count+1)    

    recurse_gen_parent("", 0, 0)
    return results


print(generateParenthesis(5))





