class MemoryManager:
    def __init__(self, heap_size=1024):
        self.heap_size = heap_size
        self.heap = [None] * heap_size  
        self.allocated_blocks = {}  

    def malloc(self, size):
        """Allocate a block of memory of the given size."""
        if size <= 0 or size > self.heap_size:
            raise ValueError("Invalid size for allocation")
            

        
        start = 0
        while start < self.heap_size:
            if self.heap[start] is None:
                free_size = 0
                for i in range(start, self.heap_size):
                    if self.heap[i] is None:
                        free_size += 1
                        if free_size >= size:
                            break
                    else:
                        start = i + 1
                        break
                if free_size >= size:
                    for i in range(start, start + size):
                        self.heap[i] = "ALLOCATED"
                    self.allocated_blocks[start] = size
                    return start
            else:
                start += 1
        raise MemoryError("Not enough memory available")  

    def free(self, start):
        """Deallocate a block of memory."""
        if start in self.allocated_blocks:
            size = self.allocated_blocks[start]
            for i in range(start, start + size):
                self.heap[i] = None
            del self.allocated_blocks[start]
        else:
            raise ValueError("Invalid memory address")

    def get_heap_status(self):
        """Return the current state of the heap."""
        return self.heap
    def detect_fragmentation(self):
        """Detect fragmentation in the heap."""
        free_blocks = []
        start = 0
        while start < self.heap_size:
            if self.heap[start] is None:
                free_size = 0
                for i in range(start, self.heap_size):
                    if self.heap[i] is None:
                        free_size += 1
                    else:
                        break
                free_blocks.append((start, free_size))
                start += free_size
            else:
                start += 1
        return free_blocks

    def detect_memory_leaks(self):
        """Detect memory leaks (allocated but unreachable blocks)."""
        return self.allocated_blocks