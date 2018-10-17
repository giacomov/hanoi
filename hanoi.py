import sys
import argparse


class Hanoi(object):

	def __init__(self, n):

		self._n = n

		# List of numbers in reverse order, like
		# [4, 3, 2, 1]
		self._left = list(range(1, n+1))[::-1]
		self._middle = []
		self._right = []

		# Keep track of number of moves
		self._n_moves = 0

	def solve(self):
		"""
		Solve the problem recursively.
		"""

		# This wrapper around the real solving method (_solve)
		# allows us to keep track
		# of the number of moves and check that at the end they are what
		# is expected

		self._n_moves = 0

		self.print_status()

		self._solve(self._n, source_rod=self._left, 
			             helper_rod=self._middle, 
			             target_rod=self._right)

		expected_moves = 2**(self._n) - 1

		assert self._n_moves == 2**(self._n) - 1, \
		       "Used %s moves instead of %s" % (self._n_moves, expected_moves)

	# This is the main recursive function
	def _solve(self, n, source_rod, helper_rod, target_rod):
		"""
		Move n pieces from the source_rod to the target_rod, using the
		helper_rod as working space
		"""

		if n == 1:

			# Base case: only one piece to be moved from source to target
			item = source_rod.pop()
			target_rod.append(item)
			self._n_moves += 1

			self.print_status()

		else:

			# Move n-1 disks from the left rod to the middle rod using the
			# right rod as swap
			self._solve(n - 1, source_rod=source_rod, 
				           helper_rod=target_rod,
				           target_rod=helper_rod)

			# Move one disk to target
			item = source_rod.pop()
			target_rod.append(item)
			self._n_moves += 1

			self.print_status()

			# Move all other disks from middle rod to right rod
			self._solve(n - 1, source_rod=helper_rod, 
				           helper_rod=source_rod, 
				           target_rod=target_rod)

	# The next methods are just to print as we go

	@staticmethod
	def _print(i, twr):

		d = "      "

		if len(twr) > i:

			sys.stdout.write("%5s%s" % (twr[i], d))

		else:

			sys.stdout.write("%5s%s" % (" ", d))

	def print_status(self):

		max_height = max([len(self._left), len(self._middle), len(self._right)])

		for i in list(range(max_height))[::-1]:

			self._print(i, self._left)
			self._print(i, self._middle)
			self._print(i, self._right)

			sys.stdout.write("\n")

		print("===========================")

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("n_disks", help="Number of disks")
	args = parser.parse_args()

	h = Hanoi(args.n_disks)

	h.solve()
		
