import numpy as np
import mazeGenerator
from tempfile import TemporaryFile
count = 2
while count < 51:
    grid = np.zeros([101, 101], dtype=int)
    mazeGenerator.make_passages(0, 0, grid)
    outfile = TemporaryFile()
    np.save(''+str(count), grid)
    count += 1
