import time
from IOmatchbox import IOM


def main():
    iom = IOM(port="COM3")   
    print("Connected. Type a command:")
    print("  on    - turn laser on")
    print("  off   - turn laser off")
    print("  read  - show readings")
    print("  quit  - exit (closes connection)")

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "on":
            iom.start_laser()
            print("Laser ON")

        elif cmd == "off":
            iom.stop_laser()
            print("Laser OFF")

        elif cmd == "read":
            print("Readings:", iom.get_readings())
            print("Status:", iom.laser_status())

        elif cmd == "quit":
            iom.closelaser()
            print("Connection closed. Bye.")
            break

        else:
            print("Unknown command. Use: on / off / read / quit")


if __name__ == "__main__":
    main()