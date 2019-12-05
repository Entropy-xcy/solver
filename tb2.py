import solver

solver.set_perpendicular('e6b', 'e6c')
solver.set_perpendicular('e6c', 'e7a')

solver.set_equal('a6a', 'a5b')

print(solver.get_all())
