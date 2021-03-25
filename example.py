from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt



parser = ArgumentParser()
parser.add_argument("array", type=str, help="numpy array file")
args = parser.parse_args()


if __name__ == "__main__":
	coords = np.load(args.array)
	plt.scatter(y=coords[:, 0], x=coords[:, 1])
	plt.show()
