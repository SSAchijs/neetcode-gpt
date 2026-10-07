import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z = z - np.max(z)
        exps = np.e**z
        ans = np.round(exps / np.sum(exps), 4)
        return ans
