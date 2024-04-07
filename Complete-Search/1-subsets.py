# generate all subsets for a set of input integers --> can be extended to generic objects in an array

#recursive
input = [3,4,5]
res = []
N = 3
def search(k, subset):
    if k ==N:
        res.append(subset.copy())
    else:
        search(k + 1, subset)
        subset.append(input[k])
        search(k + 1, subset)
        subset.pop()

search(0, [])
print(res)