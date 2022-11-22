from modules.csvloader import CSVLoader
from tkinter import ttk
from tkinter.messagebox import showerror 
import tkinter.filedialog as fd
import tkinter as tk

class CSVLoaderUI(tk.Tk):

    def __init__(self):
        super().__init__() # Calling Parent class constructor

        #--------------------------------------------------------------------------------
        #---------------------ROOT WINDOW CONFIGURATIONS---------------------------------
        #--------------------------------------------------------------------------------

        self.title("CSV Loader")
        self.geometry("700x550")
        # self.resizable(False,False)
        self.attributes("-alpha", 0.95)

        #-------------------------------------------------------------------------------
        #-------------------------------ATTRIBUTES--------------------------------------
        #-------------------------------------------------------------------------------
        self.filetypes = (
            ("csv files", "*.csv"),   
        )

        #--------------------------------------------------------------------------------
        self.__initial_build()
        self.__bind_events()
        self.mainloop()

    def __load_path(self):
        path = fd.askopenfilename(
            title="Open csv",
            initialdir="\\",
            filetypes=self.filetypes
        )
        return path
    
    def __initial_build(self):

        Button = ttk.Button
        Frame = ttk.Frame

        button_view = Frame(self)
        self.button = Button(button_view, text="load csv", command=lambda: self.load_table(self.__load_path()))
        self.button.pack(anchor="center", ipadx=15, ipady=15, pady=200,)
        button_view.place(relwidth=1, relheight=1)

    def __load_table(self, file_path: str):
        TreeView = ttk.Treeview
        Scrollbar = ttk.Scrollbar

        self.button.destroy()

        self.loader = CSVLoader(file_path)

        #--------------------------------------------------------------------------------
        #                    TREEVIEW WIDGET CONFIGURATION
        #--------------------------------------------------------------------------------

        headers = self.loader.load_header()
        column_id = []
        for header in headers:
            col_id = header.remove(" ") if (" " in header) else header
            column_id.append(col_id)
        else:
            column_id = tuple(column_id)
            del header
        
        table = TreeView(
            self, columns=column_id, show="headings"
        )

        for (col_id, header) in zip(column_id, headers):
            table.heading(col_id, text=header)
        
        for row in self.loader.load_data():
            table.insert("", 'end', values=row)

        table.pack(expand=True, fill="both", side="left", anchor="e", padx=5, ipadx=5)

        #---------------------------------------------------------------------------------
        #                           SCROLLBAR CONFIG
        #---------------------------------------------------------------------------------

        scroll_bar_x = Scrollbar(
            self, orient="vertical", command=table.yview
        )
        table["yscrollcommand"] = scroll_bar_x.set
        scroll_bar_x.pack(
            side="right", fill="y"
        )

    def load_table(self, fp: str):
        if (fp):
            self.__load_table(fp)
        else:
            showerror(
                title="csv load error",
                message="Choose an appropiate csv file"
            )
    def __bind_events(self):
        self.bind(
            "<BackSpace>", lambda event=None: self.__initial_build(), add="+"
        )
        self.bind(
            "<Alt-Left>", lambda event=None: self.__initial_build(), add="+"
        )
        self.bind(
            "<Control-W>", lambda event=None: self.destroy(), add="+"
        )
        self.bind(
            "<Control-w>", lambda event=None: self.destroy(), add="+"
        )
    
if __name__ == "__main__":

    CSVLoaderUI()