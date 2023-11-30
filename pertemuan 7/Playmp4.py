import cv2
import tkinter as tk
from tkinter import filedialog

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player App")

        # Create widgets
        self.open_button = tk.Button(root, text="Open Video", command=self.open_video)
        self.open_button.pack(pady=10)

        self.play_button = tk.Button(root, text="Play Video", command=self.play_video)
        self.play_button.pack(pady=10)

    def open_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.cap = cv2.VideoCapture(file_path)
            if not self.cap.isOpened():
                print("Error opening video file")
            else:
                print("Video file opened successfully")

    def play_video(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            while True:
                ret, frame = self.cap.read()
                if ret:
                    cv2.imshow('Video Player', frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break

            self.cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
