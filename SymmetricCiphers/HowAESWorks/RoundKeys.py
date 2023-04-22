def matrix2bytes(matrix):
  """ Converts a 4x4 matrix into a 16-byte array. """
  return bytes(sum(matrix, []))

def addRoundKeys(state, round_key, mat):
  for r in range(4):
    for c in range(4):
      mat[r][c] = state[r][c] ^ round_key[r][c]
  return mat
  
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

mat = [
    [0, 0, 0, 0], 
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print(matrix2bytes(addRoundKeys(state, round_key, mat)))
