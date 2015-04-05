# gleap

GLeap is a small tool for Linux to switch your desktops using Leap Motion. It only simulates keystrokes on your keyboard after swipe gestures (if you need, you can change keyboard shortcut).

If you want to use this script, but have some troubles - be free to write me at e-mail in profile.

## Installation

1. Clone this repository:  
`git clone https://github.com/Enet/gleap.git /path/to/your/folder`
2. Open shortcut file *gleap.desktop* in text editor and change the line:  
from `Exec=python gleap.py` to `Exec=python /path/to/your/folder/gleap.py`
3. Move file *gleap.desktop* to your autostart directory:  
`mv /path/to/your/folder/gleap.desktop ~/.config/autostart`
4. Relogin and try to swipe ;)

## Configuration

1. You can set up a minimal time between two swipes in *gleap.py* (line 26).
2. You can change keyboard shortcut, which should be pressed after swipe (line 46).
3. To run this script any time, just type in your terminal:  
`python /path/to/your/folder/gleap.py`