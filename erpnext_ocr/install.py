import os

from erpnext.demo.demo import make


def after_install():
    if os.getenv("enable_demo_first_run_wizard", 1):
        make()