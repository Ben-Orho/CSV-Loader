class CSVLoader:
    def __init__(self, file_path: str):

        with open(file_path, "r+") as file:
            self.raw_data = file.read()
        
        self.data = self.raw_data.split("\n")

        self.data_rows = [ ]
        for data_row in self.data:
            self.data_rows.append(data_row.split(","))

    def load_list(self) -> list:
        return self.data_rows

    def load_header(self) -> list:

        return self.data_rows[0]

    def load_data(self) -> list:
        
        return self.data_rows[1:]
