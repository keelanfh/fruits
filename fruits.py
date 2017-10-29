class Orange(object):
    def __init__(self):
        self.peeled = False
        self._weight=100

    def peel(self):
        self.peeled = True

    def __repr__(self):
        return "Orange()"

    def _repr_png_(self):
        if self.peeled:
            return open('./orange_peeled.png', 'r').read()
        else:
            return open('./orange.png', 'r').read()

class Apple(object):
    def __init__(self):
        pass
        self._weight=200

    def __repr__(self):
        return "Apple()"

    def _repr_jpeg_(self):
        return open('./apple.jpeg', 'r').read()

def weigh(obj):
    return obj._weight
