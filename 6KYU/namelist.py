def namelist(arr: list) -> str:
    """
    This function returns a string formatted as a list of names separated by commas 
    except for the last two names, which should be separated by an ampersand.
    """
    if len(arr) == 0:
        return ''
    elif len(arr) == 1:
        return ''.join([i['name'] for i in arr])
    elif len(arr) == 2:
        return ' & '.join([i['name'] for i in arr])
    else:
        return ', '.join([i['name'] for i in arr][:-1]) + ' & ' + ''.join([i['name'] for i in arr][-1])
    