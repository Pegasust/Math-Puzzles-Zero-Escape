"""
Digital root of a base10 number is obtained by adding each digit to create a
new number, then perform the same operation until we yield one digit number.
This one-digit number is the digital root.

Digital root is the mechanics for selecting people go through puzzle doors
in Zero Escape 999.
"""

def dig_root(decimal):
    if decimal//10 > 0:
        dig_root_ = 0
        while decimal//10 > 0:
            dig_root_ += (decimal % 10)
            decimal //= 10
        return dig_root(dig_root_+decimal)
    return decimal
def fast_dig_root(decimal):
    """
        The digital root of all positive base10 number will be 0 iff
        the number is 0. Otherwise, all numbers that yield a "pseudo
        digital root" of 0 will have to return 9.
    """
    if decimal == 0:  # you out-lier, Zero :( I love all Zeroes
        return 0
    # the digital root for a base10 is thought to be just the mod 9 (pseudo
    # digital root).
    # the idea sparked as I learned (Vietnamese, primary school) that
    # a base-10 number divides 9 iff adding all digits create a number
    # that divides 9.
    #####
    # I was one outlier that does this operation until it gives one digit.
    # In such algorithm, the number '9' is synonymous to number '0'.
    # 9 % 9 gives 0, hence the idea started.
    mod_res = decimal % 9
    # normalize
    return 9 if mod_res == 0 else mod_res
def dig_root_arr(dec_arr):
    result = 0
    for decimal in dec_arr:
        result += dig_root(decimal)
    return dig_root(result)

##def all_combs(result_digroot, comb_len, provided_comb, other_bracelets):
##    if len(provided_comb) - comb_len == -1:
##        bracelet = result_digroot - dig_root_arr(provided_comb)
##        if bracelet < 0:
##            bracelet = 9 + bracelet
##        if bracelet not in other_bracelets:
##            return None
##        else:
##            other_bracelets.remove(bracelet)
##            provided_comb.add(bracelet)
##            return provided_comb
##    elif len(provided_comb) == comb_len:
##        return provided_comb if dig_root_arr(provided_comb) == result_digroot else None
##    else:
##        pop_bracelets = other_bracelets.copy()
##        while len(pop_bracelets) > 0:
##            chose = pop_bracelets.pop()
##            other_bracelets.remove(chose)
##            provided_comb.add(chose)
##            result = all_combs(result_digroot,comb_len,provided_comb,other_bracelets)
##
##
##def all_combinations(result_digroot, comb_len, provided_comb, other_bracelets):
##    solution = list()
##    while len(other_bracelets) + len(provided_comb) > comb_len:
##        _all_combinations(result_digroot, comb_len, provided_comb, other_bracelets, solution)
##    return solution
##
##def _all_combinations(result_digroot, comb_len, provided_comb, other_bracelets,solution):
##    """
##        Returns set of collection with length of comb_len
##        that has unique bracelet numbers.
##        The result is computed from provided_comb
##        which is the set of bracelet numbers that
##        have to participate to make the result_digroot.
##
##        other_bracelets is set of all other participants
##        that can be put to return value it must not contain
##        any element in provided_comb
##    """
##    print("Solution: "+ str(solution))
##    if comb_len > len(provided_comb):
##        pop_others = other_bracelets.copy()
##        while len(pop_others) > 0:
##            chose_bracelet = pop_others.pop()
##            other_bracelets.remove(chose_bracelet)
##            provided_comb.add(chose_bracelet)
##            next_attempt = _all_combinations(result_digroot, comb_len,
##                                             provided_comb, other_bracelets,
##                                             solution)
##            provided_comb.remove(chose_bracelet)
##            other_bracelets.add(chose_bracelet)
##    else:
##        if dig_root_arr(provided_comb) == result_digroot:
##            solution.append(provided_comb.copy())
##            print("Added to solution and return " + str(provided_comb))
##        else:
##            print("NOP and return " + str(provided_comb))
##    return provided_comb
##    

if __name__ == "__main__":
    # all_combinations(3, 3, {2}, {1,3,4,5,6,7,8})
    # do brute forc
    for i in range(0,(1<<32)-1):
        ground_truth = dig_root(i)
        fast = fast_dig_root(i)
        if ground_truth != fast:
            print_str = f"i = {i}: truth({ground_truth}) != fast ({fast})"
            print(print_str)
        if i % 20000 == 0 and i != 0:
            print(f"i = {i}")
    print("Testing done.")
        
    pass
