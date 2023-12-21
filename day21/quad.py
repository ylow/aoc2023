import numpy as np
model = np.poly1d(np.polyfit([0,1,2,3], [3762,33547,93052,182277], 2))
print(model.coeffs)
print(model.coeffs[0] * (202300 * 202300) + model.coeffs[1] * 202300 + model.coeffs[2])
