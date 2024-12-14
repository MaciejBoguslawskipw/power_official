import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="DziennikPro",
    version="1.0",
    description="Aplikacja DziennikPro",
    executables=[Executable("dziennikpro.py", base=base)],
)
