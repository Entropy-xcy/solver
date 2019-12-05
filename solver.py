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
geometric_predicates['parallel'] = [['e1b', 'e2b', 'e6b'], ['e5a', 'e4b', 'e3a', 'e7a', 'e8a'],
                                    ['e5c', 'e1a', 'e7c', 'e8d'], ['e3b', 'e8c', 'e7b'],
                                    ['e1c', 'e8e', 'e4c', 'e6c'], ['e4a', 'e3c', 'e2a', 'e8b', 'e6a']]
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
                               ['a2a', 'a8c', 180], ['a8a', 'a3c', 180]]
original_sum_table = [['a1a', 'a8e', 180], ['a8e', 'a5c', 180],
                               ['a5b', 'a8a', 180], ['a8a', 'a4c', 180],
                               ['a4b', 'a8b', 180], ['a8b', 'a3a', 180],
                               ['a3c', 'a8c', 180], ['a8a', 'a2a', 180],
                      ['a2a', 'a8c', 180], ['a8a', 'a3c', 180]]
geometric_predicates['similar'] = []
original_parallel = []

angle_record_table = {'a1a': -1, 'a1b': -1, 'a1c': -1,
                      'a2a': -1, 'a2b': -1, 'a2c': -1,
                      'a3a': -1, 'a3b': -1, 'a3c': -1,
                      'a4a': -1, 'a4b': -1, 'a4c': -1,
                      'a5a': -1, 'a5b': -1, 'a5c': -1,
                      'a6a': -1, 'a6b': -1, 'a6c': -1,
                      'a7a': -1, 'a7b': -1, 'a7c': -1,
                      'a8a': -1, 'a8b': -1, 'a8c': -1,
                      'a8d': -1, 'a8e': -1}

edge_record_table = {'e1a': -1, 'e1b': -1, 'e1c': -1,
                     'e2a': -1, 'e2b': -1, 'e2c': -1,
                     'e3a': -1, 'e3b': -1, 'e3c': -1,
                     'e4a': -1, 'e4b': -1, 'e4c': -1,
                     'e5a': -1, 'e5b': -1, 'e5c': -1,
                     'e6a': -1, 'e6b': -1, 'e6c': -1,
                     'e7a': -1, 'e7b': -1, 'e7c': -1,
                     'e8a': -1, 'e8b': -1, 'e8c': -1,
                     'e8d': -1, 'e8e': -1}

area_record_table = {'ar1': -1, 'ar2': -1, 'ar3': -1,
                     'ar4': -1, 'ar5': -1, 'ar6': -1,
                     'ar7': -1, 'ar8': -1}

edge_to_angle_table = {'a1c': ['e1b', 'e1c'], 'a2b': ['e2b', 'e2a'], 'a3b': ['e3b', 'e3a'],
                       'a4a': ['e4c', 'e4a'], 'a5a': ['e5a', 'e5c'], 'a8d': ['e8d', 'e8c'],
                       'a1a': ['e1c', 'e1a'], 'a8e': ['e8d', 'e8e'], 'a5b': ['e5a', 'e5b'],
                       'a8a': ['e8e', 'e8a'], 'a4b': ['e4b', 'e4a'], 'a8b': ['e8a', 'e8b'],
                       'a8c': ['e8c', 'e8b'], 'a3c': ['e3c', 'e3b']}


for i in range(1, 8):
    triangles.append(triangle(str(i)))
for t in triangles:
    all_elements += t.flatten()


def delete_repetition(sett):
    return list(set(sett))


def is_subset_of(sub, big_set):
    flag = False
    if all(x in big_set for x in sub):
        flag = True
    return flag


def is_subsubset_of(sub, big_set):
    for ele in big_set:
        if is_subset_of(sub, ele):
            return True
    return False


def has_subset_of(big_subsetset, set):
    for sub in big_subsetset:
        if is_subset_of(sub, set):
            return True
    return False


def has_element_of(big_subset, ele):
    flattened = []
    for i in big_subset:
        for j in i:
            flattened.append(j)
    for i in ele:
        if i in flattened:
            return True
    return False


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


def contains(sol, name):
    for i in sol:
        for j in i:
            if name == j:
                return True
    return False


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    # check length
    if len(a_set.intersection(b_set)) > 0:
        return list(a_set.intersection(b_set))
    else:
        return []


def test_perpendicular():
    perpendiculars = geometric_predicates['perpendicular'].copy()

    for i in range(len(perpendiculars)):
        for j in range(len(perpendiculars)):
            if i != j and len(common_member(perpendiculars[i], perpendiculars[j])) > 0:
                perpendiculars[i] += perpendiculars[j]
                perpendiculars[j] = []
    while [] in perpendiculars:
        perpendiculars.remove([])

    for p in perpendiculars:
        max = 1
        max_element = ''
        for angle in p:
            if p.count(angle) > max:
                max = p.count(angle)
                max_element = angle
        flag = False
        while max_element in p:
            p.remove(max_element)
            flag = True
        if flag:
            geometric_predicates['parallel'].append(p)
            # solution['parallel'].append(p)
    # Infer parallels
    # geometric_predicates['parallel'] += perpendiculars


def test_angle():
    perpendiculars = geometric_predicates['perpendicular'].copy()
    for per_instance in perpendiculars:
        pass


def is_same(l1, l2):
    l11 = l1.copy()
    l22 = l2.copy()
    l11.sort()
    l22.sort()
    return l11 == l22


def get_parallels(name):
    for i in geometric_predicates['parallel']:
        for n in i:
            if n == name:
                return i
    return []


def delete_2d_repetition(l):
    for i in l:
        i.sort()
    # Trust me, don't try to understand how this works
    *y, = map(list, {*map(tuple, l)})
    return y


def test_parallel():
    parallels = geometric_predicates['parallel'].copy()
    for i in range(len(parallels)):
        for j in range(len(parallels)):
            if i != j and len(common_member(parallels[i], parallels[j])) > 0:
                parallels[i] += parallels[j]
                parallels[j] = []
    for i in range(len(parallels)):
        parallels[i] = delete_repetition(parallels[i])
    while [] in parallels:
        parallels.remove([])
    orig = geometric_predicates['parallel'].copy()
    for i in parallels:
        has = False
        for j in orig:
            if is_same(i, j):
                has = True
        if not has:
            solution['parallel'].append(i)
    geometric_predicates['parallel'] = parallels

    # Infer perpendicular from parallel
    for p in geometric_predicates['perpendicular'].copy():
        p.sort()
        e0 = p[0]
        e1 = p[1]
        p0 = get_parallels(e0)
        p1 = get_parallels(e1)
        for i in p0:
            solution['perpendicular'].append([i, e1])
        for i in p1:
            solution['perpendicular'].append([i, e0])
        delete_2d_repetition(solution['perpendicular'])
        for i in solution['perpendicular']:
            if p[0] == i[0] and p[1] == i[1]:
                solution['perpendicular'].remove(i)


def map_perpendicular_to_angle():
    perpendiculars = geometric_predicates['perpendicular'].copy()
    sensitive_edges = []
    for key in edge_to_angle_table:
        sensitive_edges.append(edge_to_angle_table[key])
    for p in perpendiculars:
        # Test if have corresponding angle
        p0 = p[0]
        p0_parallels = []
        p1 = p[1]
        p1_parallels = []
        for pa in geometric_predicates['parallel']:
            if p0 in pa:
                p0_parallels = pa
            if p1 in pa:
                p1_parallels = pa
        p0_sensitive = ''
        p1_sensitive = ''
        valid_edges = []
        for i in p0_parallels:
            for j in p1_parallels:
                if i != j:
                    if [i, j] in sensitive_edges or [j, i] in sensitive_edges:
                        valid_edges.append([i, j])
        for v in valid_edges:
            for key in edge_to_angle_table:
                te = edge_to_angle_table[key]
                if (te[0] == v[0] and te[1] == v[1]) or (te[1] == v[0] and te[0] == v[1]):
                    angle_record_table[key] = 90


def map_equal_to_angle():
    for e in geometric_predicates['equal'].copy():
        angle_flag = False
        edge_flag = False
        val = -1
        for item in e:
            if item in angle_record_table.keys():
                # Angle
                angle_flag = True
                val = angle_record_table[item]
            elif item in edge_record_table.keys():
                # Edge
                edge_flag = True
                val = edge_record_table[item]
            else:
                print("Exception!!")
        if angle_flag:
            for item in e:
                angle_record_table[item] = val
        if edge_flag:
            for item in e:
                edge_record_table[item] = val


def map_angle_to_perpendicular():
    for key in angle_record_table.keys():
        if angle_record_table[key] == 90:
            set_perpendicular(edge_to_angle_table[key][0], edge_to_angle_table[key][1])


def infer_angle_from_sum_fraction():
    for s in geometric_predicates['sum']:
        s0 = s[0]
        s1 = s[1]
        total = s[2]
        if angle_record_table[s0] != -1 and angle_record_table[s1] == -1:
            angle_record_table[s1] = int(total) - angle_record_table[s0]
        elif angle_record_table[s0] == -1 and angle_record_table[s1] != -1:
            angle_record_table[s0] = int(total) - angle_record_table[s1]

    for s in geometric_predicates['fraction']:
        s0 = s[0]
        s1 = s[1]
        fraction = s[2]
        if angle_record_table[s0] != -1 and angle_record_table[s1] == -1:
            angle_record_table[s1] = angle_record_table[s0] / float(fraction)
        elif angle_record_table[s0] == -1 and angle_record_table[s1] != -1:
            angle_record_table[s0] = float(fraction) * angle_record_table[s1]


def infer_sum_fraction_from_equal():
    for s in geometric_predicates['sum']:
        s0 = s[0]
        s1 = s[1]
        sum = int(s[2])
        for e in geometric_predicates['equal'].copy():
            if s0 in e:
                for i in e:
                    if i != s0:
                        solution['sum'].append([i, s1, sum])
            elif s1 in e:
                for i in e:
                    if i!= s1:
                        solution['sum'].append([s0, i, sum])

    # Delete repetition from the predicates
    for s in solution['sum'].copy():
        s0 = s[0]
        s1 = s[1]
        if s0=='a8e':
            print()
        for ss in original_sum_table:
            if (s0 == ss[0] and s1 == ss[1]) or (s0 == ss[1] and s1 == ss[0]):
                solution['sum'].remove(s)

    for s in geometric_predicates['fraction'].copy():
        s0 = s[0]
        s1 = s[1]
        sum = int(s[2])
        for e in geometric_predicates['equal'].copy():
            if s0 in e:
                for i in e:
                    if i != s0:
                        solution['fraction'].append([i, s1, sum])
            elif s1 in e:
                for i in e:
                    if i!= s1:
                        solution['fraction'].append([s0, i, sum])


def test_similar():
    # The circumstance of similar is unique
    sensitive_edge = ['e6b', 'e7a']
    for p in geometric_predicates['parallel'].copy():
        if sensitive_edge[0] in p and sensitive_edge[1] in p:
            solution['similar'].append(['ar1', 'ar5'])
            solution['similar'].append(['ar2', 'ar3'])


def infer_area_fraction():
    pass


def solve():
    test_equal()
    test_perpendicular()
    test_parallel()
    map_perpendicular_to_angle()
    map_angle_to_perpendicular()
    test_perpendicular()
    infer_angle_from_sum_fraction()
    infer_sum_fraction_from_equal()
    test_similar()
    test_angle()


def get_all():
    solve()
    return solution


def display_angle_edge():
    for key in angle_record_table.keys():
        if angle_record_table[key] != -1:
            print(key, angle_record_table[key])
    for key in edge_record_table.keys():
        if edge_record_table[key] != -1:
            print(key, edge_record_table[key])


def main():
    # set_equal('a5b', 'a5c')
    # set_sum_value('a5b', 'a5a', 50)
    # set_parallel('e7a', 'e2b')
    # set_perpendicular('e1c', 'e1b')
    # set_perpendicular('e2a', 'e3a')

    # set_perpendicular('e3c', 'e3b')
    # et_perpendicular('e3b', 'e4a')

    print(get_all())


if __name__ == "__main__":
    main()
