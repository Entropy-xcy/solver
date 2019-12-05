import solver

solver.set_equal('a6c', 'a6a')
solver.set_equal('a4a', 'a4b')
solver.set_parallel('e6b', 'e7a')
solver.set_fraction('a6c', 'a2a', 0.5)
solver.set_sum_value('a4b', 'a4c', 2)
solver.set_perpendicular('e2b', 'e2c')

print(solver.get_all())
