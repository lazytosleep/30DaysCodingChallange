'''
Group anagram
'''


def groupAnagram(arr):
    # Create a dictionary with sorted str and their index
    # Iterate over dictionary and get origianl elements at each index
    # So fundamentaly we are sorting to do the grouping and then capturing the index
    dict = {}
    for i in range(0, len(arr)):
        sortedStr = ''.join(sorted(arr[i]))
        if dict.get(sortedStr) == None:
            dict[sortedStr] = []
        dict.setdefault(sortedStr, []).append(i)
    finalResult = []
    for key in dict:
        result = []
        for idx in dict[key]:
            result.append(arr[idx])
        finalResult.append(result)
    return finalResult


print(groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
