## SimpleClone

SimpleClone is a Sublime Text 2 plugin for lightning-fast file cloning.

## Documentation

After installing SimpleClone, clone the active view using these simple shortcuts:

**Windows/Linux**

  * Ctrl-Shift-Right to clone the active view to the right.
  * Ctrl-Shift-Down to clone the active view down.
  * Ctrl-Shift-Alt-N to clone to a new window.

**OSX**

  * Super-Shift-Right to clone the active view to the right.
  * Super-Shift-Down to clone the active view down.
  * Super-Shift-Alt-N to clone to a new window.

You can also clone your view via the View Menu or by right clicking on a file's tab

## Overriding keyboard shortcuts

Sublime Text 2 is a great text editor with lots of features and actions. Most of these actions are bound to keyboard shortcuts so it’s nearly impossible to provide convenient plugin shortcuts for third-party plugins.

If you’re unhappy with default keymap, you can disable individual keyboard shortcuts with disabled_keymaps preference of SimpleClone.sublime-settings file.

Use a comma-separated list of clone locations for which default keyboard shortcuts should be disabled. For example, if you want to release Ctrl+Shift+Right (“Clone to Right View”), you must set the following value:

"disabled_keymaps": "right"
You should refer Default (Your-OS-Name).sublime-keymap file to get action ids (look for args/action key).

To disable all default shortcuts, set value to all:

"disabled_keymaps": "all"
Not that if you disabled any action like so and you’re create your own keyboard shortcut, you should not use simpleclone_keymap_enabled.LOCATION_NAME context since this is the key that disables locations.

## License

Copyright (c) 2012 Mike Fowler

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

