## 5. External Dependencies Declaration

This software (To-Do Your List) uses the following Python standard library modules and external dependencies. Their sources and licenses are stated below.

| Module/Library | Version | Purpose | License |
|----------------|---------|---------|---------|
| `os` | Standard Library | File path checking, environment operations | Python Software Foundation License |
| `tkinter` | Standard Library | GUI (windows, labels, buttons, listbox, etc.) | Python Software Foundation License (underlying Tcl/Tk follows Tcl/Tk BSD-style license) |
| `tkinter.ttk` | Standard Library | Advanced widgets (Combobox) | Python Software Foundation License |
| `tkinter.messagebox` | Standard Library | Popup dialogs, error messages | Python Software Foundation License |
| `tkinter.filedialog` | Standard Library | File selection dialogs | Python Software Foundation License |
| `time` | Standard Library | Countdown timer, time formatting | Python Software Foundation License |
| `winsound` | Standard Library (Windows) | Play system beep and WAV audio | Python Software Foundation License |
| `threading` | Standard Library | Multi-threading for audio playback to avoid UI blocking | Python Software Foundation License |

**Notes**:
- All modules listed above are part of the Python 3.12 standard library and require no additional installation.
- Audio playback relies on `winsound` on Windows; if porting to other platforms, an alternative library (e.g., `playsound` or `pygame`) must be used.
- The GUI is built on Tcl/Tk, which is distributed under a BSD-style license allowing free use, modification, and redistribution. See [Tcl/Tk License](https://www.tcl.tk/software/tcltk/license.html) for details.

**Third-party libraries (future extensions)**:
Currently, no third-party libraries are used. If future versions add custom audio format support or cloud sync, corresponding library licenses (e.g., `pygame`, `requests`) will be declared accordingly.