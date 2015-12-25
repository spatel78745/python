class defaultdict(dict):
    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default

    def get(self, key, *args):
        if not args:
            args = (self.default,)
        return dict.get(self, key, *args)

    def merge(self, other):
        for key in other:
            if key not in self:
                self[key] = other[key]
                
"""
Well this is an interesting arrangement of the computer
"""
