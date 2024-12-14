import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="Power_Official",
    version="1.0",
    description="Aplikacja do obliczania napiec",
    executables=[Executable("official_power.py", base=base)],
)
