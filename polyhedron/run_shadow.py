#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["ccc", "ccc_1", "ccc_2", "ccc_3", "ccc_4", "ccc_5"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        print("Сумма проекций:", Polyedr(f"data/{name}.geom").draw(tk))
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
