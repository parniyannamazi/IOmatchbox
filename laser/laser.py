# 1. Connect + read first:
# from IOmatchbox import IOM
# iom = IOM(port="COM3")

# iom.get_readings()
# iom.laser_status()
# iom.get_diode_current()
# iom.get_diode_temp()

# 2. Turn on + confirm:
# iom.start_laser()

# 3. Turn off when done:
# iom.stop_laser()
# iom.closelaser()

import time
from IOmatchbox import IOM


# start the laser
def turn_laserOn(port="COM3"):
    iom = IOM(port=port)
    iom.start_laser()
    print("Laser ON")
    return iom


def read_laser(iom):
    print("Product code:", iom.get_productcode())
    print("Laser model:", iom.get_laser_model())
    print("Settings:", iom.get_settings())
    print("Readings:", iom.get_readings())
    print("Laser status:", iom.laser_status())

    # read diode temperature continuously
    for n in range(10):
        print("Diode temp:", iom.get_diode_temp())
        print("Diode current:", iom.get_diode_current())
        print("Base temp:", iom.get_base_temp_num())
        time.sleep(1)

# turn off the laser
def turn_laserOff(iom):
    iom.stop_laser()
    iom.closelaser()
    print("Laser OFF")


def main():
    iom = None
    try:
        iom = turn_laserOn(port="COM3")
        time.sleep(1)
        read_laser(iom)
    except Exception as e:
        print("Error:", e)
    finally:
        if iom is not None:
            turn_laserOff(iom)


if __name__ == "__main__":
    main()
