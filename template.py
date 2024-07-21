import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
"src/_init__.py",
"src/helper.py",
"src/prompt.py",
".env",
"setup.py",
"research/trials.ipynb",
"app.py",
"store_index.py",
"static",
"templates/chat.html"
]
