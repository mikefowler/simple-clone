import sublime
import sublime_plugin

class SimpleCloneCommand(sublime_plugin.WindowCommand):  
    def run(self, direction):
    
        activeGroup = self.window.active_group()
        layout = self.window.get_layout()
        rows = len(layout['rows']) - 1
        cols = len(layout['cols']) - 1
    
        # Start by cloning the file...
        self.window.run_command('clone_file')

        # Now modify the layout if necessary...
        if direction == 'down':
            active = self.window.get_view_index(self.window.active_view())[0]
            total = self.window.num_groups()
            
            if rows > 1:
                if active == total - 1:
                    self.window.set_layout(self.createLayout(rows + 1, cols))
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
                self.window.set_layout(self.createLayout(rows + 1, cols))
                total = self.window.num_groups()
                newGroup = active + cols

        elif direction == 'right':
            active = self.window.get_view_index(self.window.active_view())[0]
            total = self.window.num_groups()
            if cols > 1:
                if active == total - 1:
                    self.window.set_layout(self.createLayout(rows, cols + 1))
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
                self.window.set_layout(self.createLayout(rows, cols + 1))
                newGroup = active + 1

        # And now move the file to the appropriate group
        self.window.run_command('move_to_group', { "group" : newGroup })

    def createLayout(self, rows, cols):

        numCells = rows * cols
        rowIncrement = 1.0/rows
        colIncrement = 1.0/cols

        # Add initial layout arrays
        layoutRows = [0]
        layoutCols = [0]
        layoutCells = [[0]*4]*numCells

        # Create rows array
        if rows > 1:
            for x in xrange(1, rows):
                increment = rowIncrement * x
                layoutRows.append(increment)

        layoutRows.append(1.0)

        # Create columns array
        if cols > 1:
            for y in xrange(1, cols):
                increment = colIncrement * y
                layoutCols.append(increment)

        layoutCols.append(1.0)

        # Create cell definitions (a,b)
        counter = 0
        for a in range(rows):
            for b in range(cols):
                layoutCells[counter] = [b, a, b+1, a+1]
                counter+=1

        return { 'cells': layoutCells, 'rows': layoutRows, 'cols': layoutCols }