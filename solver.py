class edge:
    def __init__(self, name):
        self.angle = -1
        self.length = -1
        self.name = name

    def __str__(self):
        return "Edge: " + self.name


class angle:
    def __init__(self, name):
        self.angle = -1
        self.name = name

    def __str__(self):
        return "Angle: " + self.name


class triangle:
    def __init__(self, name):
        self.components = {'a' + name + 'a': angle(name='a' + name + 'a'),
                           'a' + name + 'b': angle(name='a' + name + 'b'),
                           'a' + name + 'c': angle(name='a' + name + 'c'),
                           'e' + name + 'a': angle(name='e' + name + 'a'),
                           'e' + name + 'b': angle(name='e' + name + 'b'),
                           'e' + name + 'c': angle(name='e' + name + 'c')}
        self.name = name
        self.area = -1

    def __str__(self):
        return "Triangle: " + self.name + "\n" + str(self.components)


geometric_predicates = {}
solution = {}
triangles = []

solution['parallel'] = []
solution['perpendicular'] = []
solution['equal'] = []
solution['fraction'] = []
solution['sum'] = []
solution['similar'] = []
solution['parallel'] = []
solution['perpendicular'] = []
solution['equal'] = []
solution['fraction'] = []
solution['sum'] = []
solution['similar'] = []
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


for i in range(1, 8):
    triangles.append(triangle(str(i)))
for t in triangles:
    print(t)

# Add Truth to the geometric_predicates first
geometric_predicates['equal'].append(['a1a', 'a5c'])


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


# No need for our problem set
def set_tan(name1, name2):
    pass


def solve():
    pass


def get_all():
    solve()
    return solution


def main():
    pass


if __name__ == "__main__":
    main()
