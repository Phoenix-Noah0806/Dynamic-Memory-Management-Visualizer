# Dynamic Memory Visualizer

## Overview
**Dynamic Memory Visualizer** is a Python-based project that simulates and visualizes dynamic memory allocation, fragmentation, and memory leak detection. It provides a graphical interface for user interaction and helps understand memory management concepts in an intuitive way.

## Features
- **Core Memory Management Simulator**: Implements dynamic memory allocation and deallocation.
- **Memory Visualization Engine**: Graphically represents memory blocks and their status.
- **User-Friendly GUI**: Provides an interactive interface to visualize memory operations.
- **Error Handling & Input Validation**: Ensures safe operations with robust error handling.
- **Fragmentation & Memory Leak Detection**: Identifies and highlights memory issues.

## Files in the Repository
### 1. `memory_manager.py`
- Handles dynamic memory allocation and deallocation.
- Manages memory fragmentation and compaction.
- Implements algorithms to detect memory leaks.

### 2. `memory_visualizer.py`
- Uses Matplotlib to visualize allocated and free memory blocks.
- Represents memory fragmentation in a graphical format.

### 3. `gui.py`
- Provides an interactive interface using Tkinter (or another GUI framework).
- Allows users to allocate, deallocate memory and observe visual changes in real-time.

## Commit History
The project has been developed through the following commits:
1. **feat: Add core memory management simulator** - Implemented fundamental memory allocation and deallocation.
2. **feat: Add memory visualization engine** - Integrated a visualization engine to represent memory blocks.
3. **feat: Add GUI for user interaction** - Developed a user-friendly graphical interface for better interaction.
4. **feat: Add error handling and input validation** - Improved stability with error handling and input checks.
5. **feat: Add fragmentation and memory leak detection** - Implemented memory fragmentation visualization and leak detection.
6. **docs: Add project documentation and README** - Created documentation for project explanation and usage.
7. **chore: Finalize and test the project** - Conducted final tests and refinements.

## How to Run the Project
### Prerequisites
Ensure you have Python installed (preferably Python 3.8+). Install the required dependencies using:
```sh
pip install -r requirements.txt  # If you have a requirements.txt file
python memory_manager.py 
python memory_visualizer.py


## License
This project is licensed under the MIT License.
