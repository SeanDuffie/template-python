import subprocess
import sys

def build_docs():
    """
    Runs the system Doxygen command using the configuration file.
    """
    try:
        # Check=True raises an error if doxygen fails
        subprocess.run(["doxygen", "Doxyfile"], check=True)
        print("Documentation generated successfully in docs/")
    except FileNotFoundError:
        print("Error: 'doxygen' executable not found.", file=sys.stderr)
        print("Please install it via: brew install doxygen (Mac) or choco install doxygen (Win)", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("Doxygen failed to generate documentation.", file=sys.stderr)
        sys.exit(1)
