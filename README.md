# ytmusictui 🎵

A Terminal User Interface (TUI) for YouTube Music. 

## Dependencies

Before running ytmusictui, you need to make sure a few required tools and libraries are installed on your system. The project relies on Python packages for the interface and backend, and a system-level media player for audio playback.

### 1. System Requirements

You must have **[mpv](https://mpv.io/)** installed on your machine to play the audio streams. 

* **Ubuntu/Debian:**
    ```bash
    sudo apt install mpv
    ```
* **macOS:**
    ```bash
    brew install mpv
    ```
* **Arch Linux:**
    ```bash
    sudo pacman -S mpv
    ```
* **Windows:** Download the executable from the mpv website or use a package manager like Scoop (`scoop install mpv`) or Chocolatey (`choco install mpv`).

### 2. Python Packages

This project requires Python 3 and the following libraries:

* **`ytmusicapi`**: Handles all interactions with the YouTube Music backend.
* **`rich`**: Renders the beautiful, formatted text and layout in the terminal.
* **`yt-dlp`**: Extracts the actual audio stream URLs from YouTube.

You can install all the required Python dependencies at once using `pip`:

```bash
pip install ytmusicapi rich yt-dlp
