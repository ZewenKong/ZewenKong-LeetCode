def IsomorphicString(s, t):
    # return len(set(s)) == len(set(zip(s, t))) == len(set(t))
    zipped = set(zip(s, t))
    return len(zipped) == len(set(s)) == len(set(t))

# # when strings ae isomorphic:
# s = "egg"
# t = "add"
#
# zipped_set = {('e', 'a'), ('g', 'd')}
# # now comparing their lengths when duplicacies are removed
# return len(zipped_set) == len(set(s)) == len(set(d))
# # return 2 == 2 == 2 -> True

# # when strings are not isomorphic:
# s = "egk"
# t = "add"
#
# zipped_set = {('e', 'a'), ('g', 'd'), ('k', 'd')}
# # now comparing their lengths when duplicacies are removed
# return len(zipped_set) == len(set(s)) == len(set(d))
# # return 3 == 3 == 2 -> False
