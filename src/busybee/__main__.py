import cli
import sys

if __name__ == "__main__":
    app = cli.BusyBee()
    sys.exit(app.cmdloop())