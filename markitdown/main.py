import sys
from markdown import *

if __name__ == "__main__":
  for fn in sys.argv[1:]:
      print(translate(fn))
