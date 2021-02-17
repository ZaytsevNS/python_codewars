class Sleigh(object):
    def authenticate(self, name, password):
        if name == 'Santa Claus' and password == 'Ho Ho Ho!':
            return True
        return False