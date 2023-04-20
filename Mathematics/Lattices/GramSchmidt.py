import numpy as np
v = [np.array([4,1,3,-1]), np.array([2,1,-3,4]), np.array([1,0,-2,7]), np.array([6,2,9,-5])]
u = [v[0]]
for i in range(1, 4):
    m_i = [np.dot(v[i], u[j]) / np.dot(u[j], u[j]) for j in range(len(u))]
    u += [v[i] - sum([m_i_j * uj for (m_i_j, uj) in zip(m_i, u)])]
print(round(u[3][1], 5))
