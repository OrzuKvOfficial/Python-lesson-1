Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
... while True:
... joriy_vaqt = time.localtime()
... sana = time.strftime("%Y-%m-%d", joriy_vaqt)
... soat = time.strftime("%H:%M:%S", joriy_vaqt)
... daqiqalar = time.strftime("%M", joriy_vaqt)
... print("Sana:", sana, "Soat", soat, "Daqiqalar",daqiqalar)
