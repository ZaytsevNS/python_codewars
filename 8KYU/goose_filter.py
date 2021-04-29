geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds: list) -> list:
    return list(filter(lambda x: x not in geese, birds))
#     return [i for i in birds if i not in geese]