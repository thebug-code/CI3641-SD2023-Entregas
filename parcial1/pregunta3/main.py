import sys
from buddy import Buddy

memory_block_size = int(sys.argv[1])

if __name__ == '__main__':
    buddy_mm = Buddy(memory_block_size)
    buddy_mm.run_simulation()
