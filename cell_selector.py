import tkinter as tk

ROWS = 10
COLUMNS = 8

class CellSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cell Selector")
        self.cells = []  # store (row_var, [cell_vars])
        for r in range(ROWS):
            row_vars = []
            row_var = tk.IntVar()
            row_cb = tk.Checkbutton(self, text=f"Row {r+1}", variable=row_var,
                                    command=lambda r=r, v=row_var: self.toggle_row(r, v))
            row_cb.grid(row=r, column=0, padx=5, pady=5, sticky="w")
            for c in range(COLUMNS):
                var = tk.IntVar()
                cb = tk.Checkbutton(self, variable=var,
                                    command=lambda r=r, c=c, v=var: self.cell_changed(r, c, v))
                cb.grid(row=r, column=c+1, padx=2, pady=2)
                row_vars.append(var)
            self.cells.append((row_var, row_vars))

        action_btn = tk.Button(self, text="Print Selection", command=self.print_selection)
        action_btn.grid(row=ROWS, column=0, columnspan=COLUMNS+1, pady=10)

    def toggle_row(self, row, row_var):
        state = row_var.get()
        for var in self.cells[row][1]:
            var.set(state)

    def cell_changed(self, row, col, var):
        row_var, vars = self.cells[row]
        if all(v.get() for v in vars):
            row_var.set(1)
        else:
            row_var.set(0)

    def print_selection(self):
        selected = []
        for r in range(ROWS):
            for c in range(COLUMNS):
                if self.cells[r][1][c].get():
                    selected.append((r+1, c+1))
        print("Selected cells:", selected)

if __name__ == "__main__":
    app = CellSelector()
    app.mainloop()
