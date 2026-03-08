import argparse
from . import get_version

def main():
    parser = argparse.ArgumentParser(
        prog="ros2-debug",
        description="ROS 2 Debug Assistant"
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version and exit"
    )

    args = parser.parse_args()

    if args.version:
        print(f"ros2-debug-assistant v{get_version()}")
        return

    print("ROS 2 Debug Assistant — no commands implemented yet.")
