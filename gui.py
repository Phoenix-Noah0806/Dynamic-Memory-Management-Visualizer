import tkinter as tk
from tkinter import messagebox
from memory_manager import MemoryManager
from memory_visualizer import MemoryVisualizer

class MemoryVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Memory Management Visualizer")

        
        self.heap_size = 1024
        self.memory_manager = MemoryManager(self.heap_size)
        self.visualizer = MemoryVisualizer(self.heap_size)

        
        self.label = tk.Label(root, text="Enter Command (e.g., malloc 100 or free 0):")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.run_button = tk.Button(root, text="Run Command", command=self.run_command)
        self.run_button.pack()

        self.visualize_button = tk.Button(root, text="Visualize Heap", command=self.visualize_heap)
        self.visualize_button.pack()

        self.reset_button = tk.Button(root, text="Reset Heap", command=self.reset_heap)
        self.reset_button.pack()

    def run_command(self):
        """Execute the memory command entered by the user."""
        command = self.entry.get().strip().split()
        if not command:
            return

        try:
            if command[0] == "malloc":
                size = int(command[1])
                address = self.memory_manager.malloc(size)
                if address is not None:
                    messagebox.showinfo("Success", f"Allocated {size} bytes at address {address}")
                else:
                    messagebox.showerror("Error", "Not enough memory!")
            elif command[0] == "free":
                address = int(command[1])
                self.memory_manager.free(address)
                messagebox.showinfo("Success", f"Freed memory at address {address}")
            else:
                messagebox.showerror("Error", "Invalid command!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def visualize_heap(self):
        """Visualize the current state of the heap."""
        heap_status = self.memory_manager.get_heap_status()
        self.visualizer.visualize(heap_status)

    def reset_heap(self):
        """Reset the heap to its initial state."""
        self.memory_manager = MemoryManager(self.heap_size)
        messagebox.showinfo("Reset", "Heap memory has been reset.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryVisualizerApp(root)
    root.mainloop()