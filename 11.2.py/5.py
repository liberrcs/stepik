def merge(values):
    result={}
    for d in values:
        for key in d:
            result.setdefault(key, set()).add(d[key])
    return result




