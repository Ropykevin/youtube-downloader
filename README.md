# YouTube Downloader

## Overview

This is a simple YouTube video downloader built using Python and Tkinter for the graphical user interface. The application leverages the Pytube library for handling YouTube video downloads and provides a clean and user-friendly interface for users to download videos from YouTube.

## Features

- **User-Friendly Interface**: The GUI is built using Tkinter and styled with the customtkinter module, providing an aesthetically pleasing and intuitive experience.

- **YouTube Video Download**: Users can input a YouTube video link, and the application will download the video in the highest available resolution.

- **Download Progress**: The application includes a progress bar and percentage display, allowing users to track the download progress in real-time.

- **Error Handling**: The application handles download errors gracefully and displays relevant error messages to the user.

## Getting Started

### Prerequisites

- Python 3.x
- Install required Python packages using the following command:

  ```bash
  pip install -r requirements.txt
  ```

### Usage

1. Run the application by executing the following command:

   ```bash
   python youtube_downloader.py
   ```

2. Insert a YouTube video link in the provided input field.

3. Click the "Download" button to initiate the download process.

4. Monitor the download progress through the progress bar and percentage display.

5. Upon completion, the application will display a success message, or in case of an error, an appropriate error message will be shown.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature/bugfix: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Pytube](https://github.com/pytube/pytube): A lightweight, dependency-free Python library for downloading YouTube videos.
- [Tkinter](https://docs.python.org/3/library/tkinter.html): The standard GUI toolkit for Python.
- [CustomTkinter](https://github.com/username/CustomTkinter): A custom theme for Tkinter used in this project.

---
