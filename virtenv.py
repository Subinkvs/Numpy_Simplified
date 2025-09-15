"""
What is a Virtual Environment?

A virtual environment is an isolated, self-contained workspace on a computer.
It creates an independent space for projects, preventing conflicts with other
projects or the system's global Python installation.
"""

# -------------------------------
# Step 1: Create a virtual environment
# -------------------------------
# This creates a self-contained sandbox for your project
# Command:
# python -m venv myenv

# -------------------------------
# Step 2: Activate the virtual environment
# -------------------------------
# Windows:
# myenv\Scripts\activate
# macOS/Linux:
# source myenv/bin/activate

# -------------------------------
# Step 3: Verify the environment
# -------------------------------
# Check that this environment has its own Python interpreter
# Command:
# python --version

# -------------------------------
# Step 4: Install project-specific packages
# -------------------------------
# Packages installed here will not affect the system Python
# Command:
# pip install <package_name>
