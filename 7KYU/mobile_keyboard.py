def mobile_keyboard(s: str) -> int:
    keyboard: dict = {1: '0123456789*#',
                      2: 'adgjmptw',
                      3: 'behknqux',
                      4: 'cfilorvy',
                      5: 'sz'
                      }
    return sum(k for k, v in keyboard.items() for i in s if i in v)
    