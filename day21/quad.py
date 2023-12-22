import numpy as np
model = np.poly1d(np.polyfit([0,1,2,3], [3762,33547,93052,182277], 2))
print(model.coeffs)
print(int(model.coeffs[0]) * (202300 * 202300) + int(model.coeffs[1]) * 202300 + int(model.coeffs[2]))


model = np.poly1d(np.polyfit([1,2,3], [33547,93052,182277], 2))
print(model.coeffs)
print(int(model.coeffs[0]) * (202300 * 202300) + int(model.coeffs[1]) * 202300 + int(model.coeffs[2]))


model = np.poly1d(np.polyfit([0,1,2,3, 4,5], [3762,33547,93052,182277, 301222,449887], 2))
print(model.coeffs)
print(int(model.coeffs[0]) * (202300 * 202300) + int(model.coeffs[1]) * 202300 + int(model.coeffs[2]))



model = np.poly1d(np.polyfit([2,3,4], [93052,182277, 301222], 2))
print(model.coeffs)
print(int(model.coeffs[0]) * (202300 * 202300) + int(model.coeffs[1]) * 202300 + int(model.coeffs[2]))


model = np.poly1d(np.polyfit([3,4, 5], [182277, 301222, 449887], 2))
print(model.coeffs)
print(int(model.coeffs[0]) * (202300 * 202300) + int(model.coeffs[1]) * 202300 + int(model.coeffs[2]))


model = np.poly1d(np.polyfit([4, 5, 6], [301222, 449887, 628272], 2))
print(model.coeffs)
print(int(model.coeffs[0]) * (202300 * 202300) + int(model.coeffs[1]) * 202300 + int(model.coeffs[2]))

