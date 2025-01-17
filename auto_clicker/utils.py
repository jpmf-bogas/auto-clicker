"""
Utility functions for the auto-clicker project.
"""

import os

def ensure_folder_exists(folder_path):
    """Ensure that a folder exists, creating it if necessary."""
    os.makedirs(folder_path, exist_ok=True)
