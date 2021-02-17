def up_array(arr):
    if not arr:
       return None
    else:
        string = ''
        for item in arr:
            if not str(item).isdigit() or item > 9:
                return None
            else:
                string += str(item)
        total = []            
        for char in str(int(string)+1):
            total.append(int(char))

        return total