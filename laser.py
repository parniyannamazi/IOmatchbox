from IOmatchbox import IOM
import time
iom = IOM(port="COM3")

# read the laser (laser off)
print("Product code:", iom.get_productcode())
print("Laser model:", iom.get_laser_model())
print("Settings:", iom.get_settings())
print("Readings:", iom.get_readings())
print("Laser status:", iom.laser_status())

# TURN ON THE LASER
print("\nTurning laser ON...")
iom.start_laser()
time.sleep(3)                               
print("Status while on:", iom.laser_status())
print("Readings while on:", iom.get_readings())


# TURN OFF THE LASER
print("\nTurning laser OFF...")
iom.stop_laser()

# disconnect the laser
iom.closelaser()
print("Done.")