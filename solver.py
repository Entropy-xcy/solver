geometric_predicates = {}
solution = {}

# The solver is based on the following principle:
# 1. The sum of internal Angles of a triangle is 180
# 2. The angle of a straight line is 180
# 3. The difference between absolute angle of two parallel line is 0
# 4.

def set_parallel(name1, name2):
    geometric_predicates["parallel"].append([name1, name2])

def set_perpendicular(name1, name2):
    geometric_predicates["perpendicular"].append([name1, name2])

def set_equal(name1, name2):
    geometric_predicates['equal'].append([name1, name2])

def set_fraction(name1, name2, fraction):
    geometric_predicates['fraction'].append([name1, name2, fraction])

def set_sum_value(name1, name2, sum):
    geometric_predicates['sum'].append([name1, name2, sum])

def set_similar(name1, name2):
    geometric_predicates['similar'].append([name1, name2])

# No need for our problem set
def set_congruent(name1, name2):
    pass

# No need for our problem set
def set_tan(name1, name2):
    pass

def solve():
    pass

def get_all():
    solve()
    return solution

def main():
    geometric_predicates['parallel'] = []
    geometric_predicates['perpendicular'] = []
    geometric_predicates['equal'] = []
    geometric_predicates['fraction'] = []
    geometric_predicates['sum'] = []
    geometric_predicates['similar'] = []
    geometric_predicates['parallel'] = []
    geometric_predicates['perpendicular'] = []
    geometric_predicates['equal'] = []
    geometric_predicates['fraction'] = []
    geometric_predicates['sum'] = []
    geometric_predicates['similar'] = []



if __name__ == "__main__":
    main()
