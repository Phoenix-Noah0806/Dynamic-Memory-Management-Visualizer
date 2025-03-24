import matplotlib.pyplot as plt
import numpy as np

class MemoryVisualizer:
    def __init__(self, heap_size):
        self.heap_size = heap_size

    def visualize(self, heap):
        """Visualize the heap memory."""
        heap_array = np.array([1 if block == "ALLOCATED" else 0 for block in heap])
        plt.figure(figsize=(10, 2))
        plt.bar(range(self.heap_size), heap_array, color=['red' if x == 1 else 'green' for x in heap_array])
        plt.xlabel("Memory Address")
        plt.ylabel("Allocation Status")
        plt.title("Heap Memory Visualization")
        plt.show()