def unflatten(dictionary):
    result = {}
    for k,v in dictionary.iteritems():
        parts = k.split(".")
        dict1 = result
        for part in parts[:-1]:
            if part not in dict1:
                dict1[part] = {}
            dict1 = dict1[part]
        dict1[parts[-1]] = v
    return result



     
print unflatten({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
