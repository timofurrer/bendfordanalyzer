# -*- coding: utf-8 -*-

import sys
import os
from collections import defaultdict

class BendfordsLaw(object):
  @classmethod
  def analyze(cls, path):
    if not os.path.exists(path):
      sys.stderr.write("Error: given file %s does not exist\n" % path )
      return 1

    number_freq = defaultdict(int)
    with open(path, "r") as f:
      first_digits = [int(w[0]) for w in f.read().split() if w.isdigit() and int(w[0]) > 0]

    for d in first_digits:
      number_freq[d] += 1

    k = 100.0 / len(first_digits)
    for i in range(1, 10):
      try:
        freq = number_freq[i]
      except KeyError:
        freq = 0
      print "Number %d: %.2f" % (i, k * freq)


if __name__ == "__main__":
  if len(sys.argv) <= 1:
    sys.stderr.write("Error: please give a text file to analyze\n")
    sys.exit(1)

  sys.exit(BendfordsLaw.analyze(sys.argv[1]))
