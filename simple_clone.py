import sublime
import sublime_plugin

import re


settings = None


# Clone the current view
class SimpleCloneCommand(sublime_plugin.WindowCommand):
    def run(self, location):  # --Matt Bolt: Renamed direction variable to the more symantically appropriate name 'location' due to additional options

        # activeGroup = self.window.active_group() --Matt Bolt: Commented out unused variable
        layout = self.window.get_layout()
        rows = len(layout['rows']) - 1
        cols = len(layout['cols']) - 1

        # Clone to new window if requested
        if location == 'new_window':
            # Create new window
            self.window.run_command("new_window")
            # Open the current file in the new window
            sublime.windows()[-1:][0].open_file(self.window.active_view().file_name())

        # Handle cloning to view
        else:

            # Start by cloning the file...
            self.window.run_command('clone_file')

            # Now modify the layout if necessary...
            if location == 'down':
                active = self.window.get_view_index(self.window.active_view())[0]
                total = self.window.num_groups()

                if rows > 1:
                    if active == total - 1:
                        self.window.set_layout(createLayout(rows + 1, cols))
                        newGroup = active + cols
                    else:
                        total = self.window.num_groups()
                        if active + cols < total:
                            newGroup = active + cols
                        elif active - cols >= 0:
                            newGroup = active - cols
                        else:
                            newGroup = active
                else:
                    self.window.set_layout(createLayout(rows + 1, cols))
                    total = self.window.num_groups()
                    newGroup = active + cols

            elif location == 'right':
                active = self.window.get_view_index(self.window.active_view())[0]
                total = self.window.num_groups()
                if cols > 1:
                    if active == total - 1:
                        self.window.set_layout(createLayout(rows, cols + 1))
                        newGroup = active + 1
                    else:
                        total = self.window.num_groups()
                        if active + 1 < total:
                            newGroup = active + 1
                        elif active - 1 >= 0:
                            newGroup = active - 1
                        else:
                            newGroup = active
                else:
                    self.window.set_layout(createLayout(rows, cols + 1))
                    newGroup = active + 1

            # And now move the file to the appropriate group
            self.window.run_command('move_to_group', {"group": newGroup})


# Clone the targeted tab context
class SimpleCloneTabContextCommand(sublime_plugin.WindowCommand):
    def run(self, location, group, index):

        # activeGroup = self.window.active_group() --Matt Bolt: Commented out unused variable
        layout = self.window.get_layout()
        rows = len(layout['rows']) - 1
        cols = len(layout['cols']) - 1

        # Clone to new window if requested
        if location == 'new_window':
            # Create new window
            self.window.run_command("new_window")
            # Open the targeted file in the new window
            sublime.windows()[-1:][0].open_file(self.window.views_in_group(group)[index].file_name())

        # Handle cloning to view
        else:

            # Store currently active view
            activeView = self.window.active_view()
            # Show targeted view
            self.window.focus_view(self.window.views_in_group(group)[index])
            # Start by cloning the file...
            self.window.run_command('clone_file')

            # Now modify the layout if necessary...
            if location == 'down':
                active = self.window.get_view_index(self.window.active_view())[0]
                total = self.window.num_groups()

                if rows > 1:
                    if active == total - 1:
                        self.window.set_layout(createLayout(rows + 1, cols))
                        newGroup = active + cols
                    else:
                        total = self.window.num_groups()
                        if active + cols < total:
                            newGroup = active + cols
                        elif active - cols >= 0:
                            newGroup = active - cols
                        else:
                            newGroup = active
                else:
                    self.window.set_layout(createLayout(rows + 1, cols))
                    total = self.window.num_groups()
                    newGroup = active + cols

            elif location == 'right':
                active = self.window.get_view_index(self.window.active_view())[0]
                total = self.window.num_groups()
                if cols > 1:
                    if active == total - 1:
                        self.window.set_layout(createLayout(rows, cols + 1))
                        newGroup = active + 1
                    else:
                        total = self.window.num_groups()
                        if active + 1 < total:
                            newGroup = active + 1
                        elif active - 1 >= 0:
                            newGroup = active - 1
                        else:
                            newGroup = active
                else:
                    self.window.set_layout(createLayout(rows, cols + 1))
                    newGroup = active + 1

            # And now move the file to the appropriate group
            self.window.run_command('move_to_group', {"group": newGroup})
            # Restore active view
            self.window.focus_view(activeView)


def createLayout(rows, cols):

    numCells = rows * cols
    rowIncrement = 1.0 / rows
    colIncrement = 1.0 / cols

    # Add initial layout arrays
    layoutRows = [0]
    layoutCols = [0]
    layoutCells = [[0] * 4] * numCells

    # Create rows array
    if rows > 1:
        for x in range(1, rows):
            increment = rowIncrement * x
            layoutRows.append(increment)

    layoutRows.append(1.0)

    # Create columns arraydown
    if cols > 1:
        for y in range(1, cols):
            increment = colIncrement * y
            layoutCols.append(increment)

    layoutCols.append(1.0)

    # Create cell definitions (a,b)
    counter = 0
    for a in range(rows):
        for b in range(cols):
            layoutCells[counter] = [b, a, b + 1, a + 1]
            counter += 1

    return {'cells': layoutCells, 'rows': layoutRows, 'cols': layoutCols}


    # Used to disable keymaps
def should_perform_clone(location):
        disabled_keymaps = settings.get('disabled_keymaps', '')

        if not disabled_keymaps:
            return True

        if disabled_keymaps == 'all':
            return False

        return location not in re.split(r'\s*,\s*', disabled_keymaps.strip())


class ActionContextHandler(sublime_plugin.EventListener):
    def on_query_context(self, view, key, op, operand, match_all):
        if not key.startswith('simpleclone_keymap_enabled.'):
            return None

        prefix, location = key.split('.')
        return should_perform_clone(location)


def plugin_loaded():
    global settings
    settings = sublime.load_settings('SimpleClone.sublime-settings')


if int(sublime.version()) < 3000:
    plugin_loaded()
