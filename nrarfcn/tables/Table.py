class Table:
    def __init__(self, id: str, release_3gpp: int, ts: str, name: str, header: list, data: list):
        self.id = id
        self.release_3gpp = release_3gpp
        self.ts = ts
        self.name = name
        self.header = header
        self.data = data

    def get_column(self, column_name: str) -> list:
        idx = self.header.index(column_name)
        return [row[idx] for row in self.data]

    def get_cell(self, row: list, key: str):
        idx = self.header.index(key)
        return row[idx]
