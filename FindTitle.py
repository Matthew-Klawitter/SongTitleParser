import atexit
import os
import psutil
import threading
import time
import win32gui


class SongTitleFinder:
    def __init__(self):
        self.DIRECTORY = os.getcwd() + "/Titles/"
        self.VLC_FILE = "VLC.txt"
        self.SPOTIFY_FILE = "Spotify.txt"
        self.VLC_FILTER = "VLC media player"
        self.SPOTIFY_FILTER = "Spotify"

        self.vlc_enum = None
        self.spotify_enum = None
        self.is_running = True

        # Callback that ensures text files within the Titles folder are cleared of data on exit
        atexit.register(self.exit_handler)

    def run(self):
        # Creates text files if they don't already exist
        self.file_check(self.DIRECTORY, self.VLC_FILE)
        self.file_check(self.DIRECTORY, self.SPOTIFY_FILE)

        while self.is_running:
            if not threading.main_thread().is_alive():
                self.is_running = False

            if self.vlc_enum is None or self.spotify_enum is None:
                win32gui.EnumWindows(self.update_window_id, None )
            self.update_text()
            time.sleep(1)

    def update_window_id(self, hwnd, ctx):
        title = win32gui.GetWindowText(hwnd)

        if self.VLC_FILTER in title:
            if self.vlc_enum is None:
                self.vlc_enum = hwnd
        elif self.SPOTIFY_FILTER in title:
            if self.spotify_enum is None:
                self.spotify_enum = hwnd

    def update_text(self):
        try:
            if not (self.vlc_enum is None):
                title = win32gui.GetWindowText(self.vlc_enum)
                if title:
                    vlc_index = title.find("VLC") - 3
                    title = title[:vlc_index]
                    self.save(self.DIRECTORY, "VLC.txt", title + "     ")
                else:
                    self.vlc_enum = None
                    self.save(self.DIRECTORY, "VLC.txt", "")

            if not (self.spotify_enum is None):
                title = win32gui.GetWindowText(self.spotify_enum)
                if title:
                    if title == "Spotify" or title == "Spotify Premium":
                        self.save(self.DIRECTORY, "Spotify.txt", "")
                    else:
                        self.save(self.DIRECTORY, "Spotify.txt", title + "     ")
                else:
                    self.spotify_enum = None
                    self.save(self.DIRECTORY, "Spotify.txt", "")

        except Exception as err:
            print(err)
            self.vlc_enum = None
            self.spotify_enum = None

    def file_check(self, dir, filename):
        if not os.path.exists(dir):
            os.makedirs(dir)

        if not os.path.isfile(dir + filename):
            with open(dir + filename, "w") as f:
                f.write("")
                f.seek(0)
                f.close()

    def save(self, dir, filename, content):
        self.file_check(dir, filename)

        with open(dir + filename, "w", encoding="utf8") as f:
            f.write(content)
            f.seek(0)
            f.close()

    def exit_handler(self):
        print("Application is closing: clearing title data...")
        self.is_running = False
        self.save(self.DIRECTORY, "VLC.txt", "")
        self.save(self.DIRECTORY, "Spotify.txt", "")

print("Getting things ready...")
print("For optimal results, please have VLC and/or Spotify Desktop open with no music playing until this is ready.")

stf = SongTitleFinder()
thread = threading.Thread(target = stf.run)

print()
print("Ready to track some tracks! Please play your music whenever you're ready.")
print("Song titles will be output to text files within the 'Titles' folder where this app is being run.")

thread.start()

input = input("Press enter to stop.")
stf.is_running = False
# Figure out foreign characters via unicode conversion
