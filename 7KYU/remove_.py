class List:
    def remove_(self, integer_list: list, values_list: list) -> list:
        return [i for i in integer_list if i not in values_list]
