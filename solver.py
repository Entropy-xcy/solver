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
                           'e' + name + 'a': edge(name='e' + name + 'a'),
                           'e' + name + 'b': edge(name='e' + name + 'b'),
                           'e' + name + 'c': edge(name='e' + name + 'c')}
        self.name = name
        self.area = -1

    def __str__(self):
        return "Triangle: " + self.name + "\n" + str(self.components)

    def flatten(self):
        ret = []
        for keys in self.components:
            ret.append(self.components[keys])
        return ret



geometric_predicates = {}
solution = {}
triangles = []
all_elements = []

# Create Solution
solution['parallel'] = []
solution['perpendicular'] = []
solution['equal'] = []
solution['fraction'] = []
solution['sum'] = []
solution['similar'] = []

# Add Truth to the geometry predicates
geometric_predicates['parallel'] = []
geometric_predicates['perpendicular'] = []
geometric_predicates['equal'] = [['a5a', 'a7c'], ['a6c', 'a1c'],
                                 ['a2b', 'a6b'], ['a3b', 'a7a'],
                                 ['a4a', 'a6a'], ['a1a', 'a5c'],
                                 ['a4c', 'a5b'], ['a3a', 'a4b'],
                                 ['a3c', 'a2a']]
geometric_predicates['fraction'] = []
geometric_predicates['sum'] = [['a1a', 'a8e', 180], ['a8e', 'a5c', 180],
                               ['a5b', 'a8a', 180], ['a8a', 'a4c', 180],
                               ['a4b', 'a8b', 180], ['a8b', 'a3a', 180],
                               ['a3c', 'a8c', 180], ['a8a', 'a2a', 180],
                               ['a8d', 'a1b', 'a2c', 180]]
geometric_predicates['similar'] = []



for i in range(1, 8):
    triangles.append(triangle(str(i)))
for t in triangles:
    all_elements += t.flatten()
print(all_elements)

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


# This rule infer other equal from name1 and name2
def infer_equal(name):
    equals = geometric_predicates['equal']
    select = []
    for e in equals:
        if name in e:
            select.append(e)
    return_lst = []
    for s in select:
        for element in s:
            if element != name:
                return_lst.append(element)
    return return_lst


def test_equal():
    equals = geometric_predicates['equal']
    eq_record = []
    infered = []
    for e in equals:
        for element in e:
            if element not in eq_record:
                eq_record.append(element)
            else:
                # There is a duplicate in equal
                infered.append(infer_equal(element))
    solution['equal'] += infered


def test_sum():
    pass


def test_angle():
    perpendiculars = geometric_predicates['perpendicular']
    for per_instance in perpendiculars:
        pass


def solve():
    test_equal()
    test_angle()


def get_all():
    solve()
    return solution


def main():
    set_equal('a5b', 'a5c')
    print(get_all())


if __name__ == "__main__":
    main()
