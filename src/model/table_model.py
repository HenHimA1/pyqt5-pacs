from PyQt5.QtCore import Qt, QAbstractTableModel


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self.init_data(data)

    def init_data(self, data):
        self._data = [list(_dataLine.values()) for _dataLine in data]
        self._data_column = data and list(data[0].keys())
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data and self._data[0])

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data_column[section])

            if orientation == Qt.Vertical:
                return section + 1
        return super(TableModel, self).headerData(section, orientation, role)
