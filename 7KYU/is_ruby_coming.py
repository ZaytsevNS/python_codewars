def is_ruby_coming(lst: list) -> bool:
    return True if any([i['language'].lower() == 'ruby' for i in lst]) else False
