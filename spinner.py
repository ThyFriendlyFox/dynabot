import sys
import time
import threading

class Spinner:
    def __init__(self, message='Working...', delay=0.1):
        self.spinner = '|/-\\'
        self.delay = delay
        self.message = message
        self.busy = False
        self.spinner_visible = False
        self._thread = None

    def write_next_character(self):
        """Write the next spinner character."""
        sys.stdout.write(next(self.spinner_generator))
        sys.stdout.flush()
        time.sleep(self.delay)
        sys.stdout.write('\b')
        sys.stdout.flush()

    def spinner_generator(self):
        """Generator for spinner characters."""
        while True:
            for char in self.spinner:
                yield char

    def start(self):
        """Start the spinner."""
        self.busy = True
        self._thread = threading.Thread(target=self.show)
        self._thread.start()

    def stop(self):
        """Stop the spinner."""
        self.busy = False
        time.sleep(self.delay)
        if self.spinner_visible:
            sys.stdout.write('\b')
            sys.stdout.flush()

    def show(self):
        """Show the spinner."""
        while self.busy:
            self.write_next_character()
            self.spinner_visible = True
        self.spinner_visible = False

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

# Example usage:
# with Spinner():
#     # Your time-consuming operations
#     time.sleep(5)
