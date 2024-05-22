import os
import shutil
from pathlib import Path


def remove_allure_directory():
    root_path = Path(__file__).parent.parent.parent
    allure_results_dir = os.path.join(root_path, 'allure-results')
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)


remove_allure_directory()
