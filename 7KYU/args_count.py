# Solution for task: https://www.codewars.com/kata/5c44b0b200ce187106452139/

""" returns the count of passed arguments """
args_count = lambda *args, **kwargs: len(args) + len(kwargs)