import sys
from pathlib import Path

import nbformat


def clear_code_cells(ipynb_file: Path, output_file: Path, clear_output: bool = True):
    """Clear the code cells in a Jupyter notebook, leaving markdown cells unchanged.

    Optionally clears the output of code cells.

    Args:
        ipynb_file (Path): Path to the input notebook file.
        output_file (Path): Path to the output notebook file.
        clear_output (bool): If True, clears the output of code cells as well.
    """
    # Load the notebook
    notebook = nbformat.read(ipynb_file, as_version=4)

    # Iterate over all cells in the notebook
    for cell in notebook.cells:
        # If the cell is a code cell
        if cell.cell_type == "code":
            # Clear its content
            cell.source = ""
            # Optionally clear its output
            if clear_output:
                cell.outputs = []
                if "execution_count" in cell:
                    cell["execution_count"] = None

    # Save the modified notebook
    nbformat.write(notebook, output_file)


def process_notebooks(
    solutions_dir: Path, exercises_dir: Path, clear_output: bool = False
):
    """Process all Jupyter notebooks in the solutions directory, clearing code cells.

    Optionally their output, and save them to the exercises directory.

    Args:
        solutions_dir (Path): Path to the solutions directory.
        exercises_dir (Path): Path to the exercises directory.
        clear_output (bool): If True, clears the output of code cells as well.
    """
    # Ensure the exercises directory exists
    exercises_dir.mkdir(parents=True, exist_ok=True)

    # Iterate over all .ipynb files in the solutions directory
    for ipynb_file in solutions_dir.glob("*.ipynb"):
        # Define the output file path in the exercises directory
        output_file = exercises_dir / ipynb_file.name

        # Apply the clear_code_cells function
        clear_code_cells(ipynb_file, output_file, clear_output)


if __name__ == "__main__":
    # Define base paths
    base_dir = Path(__file__).resolve().parent.parent
    solutions_dir = base_dir / "docs" / "notebooks" / "solutions"
    exercises_dir = base_dir / "docs" / "notebooks" / "exercises"

    # Option to clear output
    clear_output = True  # Set to False to keep the output

    # Process the notebooks
    process_notebooks(solutions_dir, exercises_dir, clear_output)


if __name__ == "__main__":
    # Check if '--clear_output' is in the command line arguments
    clear_output = "--clear_output" in sys.argv

    # Define base paths
    base_dir = Path(__file__).resolve().parent.parent
    solutions_dir = base_dir / "docs" / "notebooks" / "solutions"
    exercises_dir = base_dir / "docs" / "notebooks" / "exercises"

    # Process the notebooks
    process_notebooks(solutions_dir, exercises_dir, clear_output)
