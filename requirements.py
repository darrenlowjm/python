#from globals import SHOCKWAVEPATH
import os
import subprocess
import sys


def pip_install(*args, **kwargs):  # type: (...) -> None
    """
    Run the Python pip installer to add/update packages.

    Special: if check=False provided in the argument list, do not test to
    see if the process completed successfully.
    """
    func = subprocess.check_call
    if 'check' in kwargs and not kwargs['check']:
        func = subprocess.call
    pip_args = [sys.executable, "-m", "pip", "install"] + [arg for arg in args]
    print(pip_args)
    #func(pip_args)
    
    
    
def install_requirements():
    SHOCKWAVEPATH = r'c:\Shockwave'
    filePath = os.path.join(SHOCKWAVEPATH, "requirements.txt")
    try:
        # It is much faster to install an entire requirements file at once.
        # Attempt this first, and only try to install them one-by-one if
        # it fails.
        pip_install("-r", filePath)
    except subprocess.CalledProcessError:
        install_requirements_one_by_one(filePath)


install_requirements()
    
