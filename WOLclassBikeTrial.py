class CoordSequance:
    def __init__(self, coords):
        self.coords = list(coords)

    @classmethod
    def from_deltas(cls,deltas):
        def accumulate(deltas):
            y = 0
            for d in deltas:
                y += d
                yield y # co to yield???
        return cls(enumerate(accumulate(deltas)))
    
    def min(self):
        xs, ys = zip(*self.coords) #transpozycja / samo self?
        return min(xs), min(ys) 
    
    def max(self):
        xs, ys = zip(*self.coords) 
        return max(xs), max(ys) 
    
    def offset(self, dx, dy): #translacja przesunięcie 
        return self.__class__((x+dx,y+dy)for x,y in self) # iterator self
    
    def __repr__(self):
        return repr(self.coords) # co to repr
    
    def __iter__(self):
        return iter(self.coords) 
    

class CoordSequanceGrup:
    def __init__(self, sequences):
        self.sequences = list(sequences)

    
    def min(self):
        xs, ys = zip(*(seq.min() for seq in self)) #transpozycja / samo self?
        return min(xs), min(ys) 
    
    def max(self):
        xs, ys = zip(*(seq.max() for seq in self)) 
        return max(xs), max(ys) 
    # 36 min
    def offset(self, dx, dy): #translacja przesunięcie 
        return self.__class__((seq.offset(dx, dy) for seq in self)) # iterator self
    
    def __repr__(self):
        return repr(self.sequences) # co to repr
    
    def __iter__(self):
        return iter(self.sequences) 
    
class SubtileRenderer:
    BACKGROUND = " "
    GLYPHS = ['_', '-', '‾', ' ']
    N_SUBS = len(GLYPHS)

    def __init__(self, sequence_grup):
        self.original_grup = sequence_grup

        min_x, min_y = self.original_grup.min()
        dx = -min_x
        dy = -(min_y // self.N_SUBS) * self.N_SUBS
        self.grup = self.original_grup.offset(dx, dy)

        max_x, max_y = self.grup.max()
        self.width = max_x + 1
        self.height = max_y // self.N_SUBS + 1
        self.subtile_height = self.height * self.N_SUBS

    def render(self):
        buffer = self._alloc_buffer()
        for seq in self.grup:
            for x, y in seq:
                self._plot_tile(buffer, x, y)
        return "\n".join("".join(row) for row in buffer)
    
    def _alloc_buffer(self):
        return [[self.BACKGROUND for col in range(self.width)]
                for row in range(self.height)]
    

    def _plot_tile(self, buffer, x, y):
        flip_y = self.subtile_height - 1 - y 
        row, subrow = divmod(flip_y, self.N_SUBS)
        buffer[row][x] = self.GLYPHS[subrow]



    
#cs = CoordSequance.from_deltas([2, 1, -1, -2, -2, -2])
cs = CoordSequance.from_deltas([1, -1,  0, 0, -1,  1,  1, 
        0,  0,  0, 0, -2, -1, -1, 
        0, -1, -1, 0,  1,  1,  0, 
        0, -1, -1, 0])
# print(cs)
# print(cs.min())
# print(cs.max())
cs2 = cs.offset(1,6)
# print(cs2)
gr = CoordSequanceGrup([cs, cs2])
# print(grp)
# print(grp.min())
# print(grp.max())
rr = SubtileRenderer(gr)
print(rr.render())


    