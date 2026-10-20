import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Inventario - UGB")
        self.setGeometry(100, 100, 1000, 700)
        
        self.df = pd.read_csv('datos.csv')
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout_principal = QHBoxLayout(self.central_widget)
        
        self.layout_izq = QVBoxLayout()
        self.label_titulo = QLabel("<b>Inventario General de Sucursales</b>")
        self.layout_izq.addWidget(self.label_titulo)
        
        self.tabla = QTableWidget()
        self.cargar_tabla()
        self.layout_izq.addWidget(self.tabla)
        
        self.btn_actualizar = QPushButton("Actualizar Gráficos")
        self.btn_actualizar.clicked.connect(self.actualizar_graficos)
        self.layout_izq.addWidget(self.btn_actualizar)
        
        self.layout_principal.addLayout(self.layout_izq, 1)
        
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvas(self.fig)
        self.layout_principal.addWidget(self.canvas, 1)
        
        self.generar_grafico()

    def cargar_tabla(self):
        self.tabla.setRowCount(len(self.df))
        self.tabla.setColumnCount(len(self.df.columns))
        self.tabla.setHorizontalHeaderLabels(self.df.columns)
        
        for i in range(len(self.df)):
            for j in range(len(self.df.columns)):
                self.tabla.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

    def generar_grafico(self):
        self.ax.clear()
        stock_por_sucursal = self.df.groupby('sucursal')['stock'].sum()
        stock_por_sucursal.plot(kind='bar', ax=self.ax, color='skyblue', edgecolor='black')
        self.ax.set_title("Stock Total por Sucursal")
        self.ax.set_xlabel("Sucursal")
        self.ax.set_ylabel("Unidades en Stock")
        self.ax.tick_params(axis='x', rotation=45)
        self.fig.tight_layout()
        self.canvas.draw()

    def actualizar_graficos(self):
        self.generar_grafico()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())