#no macierz no 
# print(sum(mnt, [])) zastosowanie drugiego parametru arr??

# map() - to specjalna funkcja dla każdego elemntu w tablicy

#mountain_section

def mountains_of_hoiyama(width):
    height = width // 2 + 1
    peak_row, peak_col = 0, height - 1
    peak_density = width

    def peak_deltas(row, col):
        return abs(row - peak_row), abs(col - peak_col)
    
    def peak_distanse(row,col):
        return sum(peak_deltas(row, col))

    def internal(row, col):
        d_row, d_col = peak_deltas(row, col)
        return d_col <= d_row
      

    def density(row, col):
        return (peak_density - peak_distanse(row,col)
            if internal(row, col) else 0)

    return [[density(row, col) for  col in range(width)] for row in range(height)]

from pprint import pprint

mnt = mountains_of_hoiyama(9)
pprint(mnt)
#print(sum(sum(mnt, [])))
print(sum(map(sum, [])))

# print(" ")
# pprint(mountains_of_hoiyama(17))


def mountain_weight(width):
    if width % 2 == 0:
        raise ValueError("Width must be an odd number")
    total_weight = 0
    for i in range(width):
        row_weight = (i+1) * (width-i)
        total_weight += row_weight
    return total_weight




















# def mountains_of_hoiyama(w):
#     return ((w + 1) ** 3 - w ** 2) // 8 + 1


# def mountains_of_hoiyama(width):
#     """
#     Notice that each top consists of a left side, a middle vertical and a right side.
#     The left and right sides are the same.
#     Then note that left side consists of such sums:
#     from k+1 to (2n-3-k)
#     where:
#     n = width // 2 + 1, is a level of the mountain
#     k = {0, 2, 4, ..., n // 2} => k = 2i where i = {0, 1, 2, ...}
#     so:
#     S_left_side = S_right_side = Sum_from_(i=0)_to_(n//2)_of_[ (2n-3-2i)(2n-3-2i+1)/2 - 2i(2i+1)/2 ]
#     so:
#     result = 2 * S_left_side + sum of numbers in the middle vertical
#     :) 
#     """
#     n = width // 2 + 1
#     return 2 * sum(2 * n ** 2 - 4 * n * i - 5 * n + 4 * i + 3 for i in range(n >> 1)) + n * (3 * n - 1) // 2

