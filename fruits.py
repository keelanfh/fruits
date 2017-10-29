import os
direc = os.path.dirname(__file__)

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
            return open(os.path.join(direc,'orange_peeled.png'), 'r').read()
        else:
            return open(os.path.join(direc,'orange.png'), 'r').read()

class Apple(object):
    def __init__(self):
        pass
        self._weight=200

    def __repr__(self):
        return "Apple()"

    def _repr_jpeg_(self):
        return open(os.path.join(direc,'apple.jpeg'), 'r').read()

def weigh(obj):
    return obj._weight
