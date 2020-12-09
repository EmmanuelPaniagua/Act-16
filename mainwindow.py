from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from Libreria_Part.administrador import Administrador
from Libreria_Part.particula import Particula
from PySide2.QtGui import QPen, QColor, QTransform
import os 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.administrador = Administrador()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.actionId_ascendente.triggered.connect(self.action_ordenar_id)
        self.ui.actionDistancia_descendente.triggered.connect(self.action_ordenar_distancia)
        self.ui.actionVelocidad_ascendente.triggered.connect(self.action_ordenar_velocidad)

        self.ui.actionGrafo.triggered.connect(self.action_crear_grafo)

        self.ui.actionAmplitud.triggered.connect(self.recorrido_amplitud)
        self.ui.actionProfundidad.triggered.connect(self.recorrido_profundidad)

        self.grafo = {}

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def recorrido_amplitud(self):
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        if not self.administrador.amplitud(self.grafo, origen_x, origen_y):
            QMessageBox.warning(
                self,
                "Aviso",
                "No es posible leer los valores"
            )
        else:
            os.system("cls")
            amplitud = self.administrador.amplitud(self.grafo, origen_x, origen_y)
            print("Amplitud: ")
            for i in amplitud:
                print(i)

    @Slot()
    def recorrido_profundidad(self):
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        if not self.administrador.profundidad(self.grafo, origen_x, origen_y):
            QMessageBox.warning(
                self,
                "Aviso",
                "No es posible leer los valores"
            )
        else:
            os.system("cls")
            profundidad = self.administrador.profundidad(self.grafo, origen_x, origen_y)
            print("Profundidad: ")
            for i in profundidad:
                print(i)

    @Slot()
    def action_crear_grafo(self):
        self.ui.salida.clear()
        self.grafo.clear()
        grafo = self.administrador.dictionary(self.grafo)
        self.ui.salida.insertPlainText(grafo)

    @Slot()
    def action_ordenar_id(self):
        self.ui.salida.clear()
        self.ui.tabla.clear()
        headers = ["Id", "Origen_x", "Origen_y", "Destino_x", "Destino_y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.administrador))

        particulas = []
        for particula in self.administrador:
            particulas.append(particula)
        particulas.sort(key = lambda particula: particula.id, reverse=False)

        row = 0
        for particula in particulas:
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(particula.velocidad)
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem (row, 0, id_widget)
            self.ui.tabla.setItem (row, 1, origen_x_widget)
            self.ui.tabla.setItem (row, 2, origen_y_widget)
            self.ui.tabla.setItem (row, 3, destino_x_widget)
            self.ui.tabla.setItem (row, 4, destino_y_widget)
            self.ui.tabla.setItem (row, 5, velocidad_widget)
            self.ui.tabla.setItem (row, 6, red_widget)
            self.ui.tabla.setItem (row, 7, green_widget)
            self.ui.tabla.setItem (row, 8, blue_widget)
            self.ui.tabla.setItem (row, 9, distancia_widget)
 
            row += 1

        for  particula in particulas:
            self.ui.salida.insertPlainText(str(particula))

    @Slot()
    def action_ordenar_distancia(self):
        self.ui.salida.clear()
        self.ui.tabla.clear()
        headers = ["Id", "Origen_x", "Origen_y", "Destino_x", "Destino_y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.administrador))

        particulas = []
        for particula in self.administrador:
            particulas.append(particula)
        particulas.sort(key = lambda particula: particula.distancia, reverse=True)

        row = 0
        for particula in particulas:
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(particula.velocidad)
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem (row, 0, id_widget)
            self.ui.tabla.setItem (row, 1, origen_x_widget)
            self.ui.tabla.setItem (row, 2, origen_y_widget)
            self.ui.tabla.setItem (row, 3, destino_x_widget)
            self.ui.tabla.setItem (row, 4, destino_y_widget)
            self.ui.tabla.setItem (row, 5, velocidad_widget)
            self.ui.tabla.setItem (row, 6, red_widget)
            self.ui.tabla.setItem (row, 7, green_widget)
            self.ui.tabla.setItem (row, 8, blue_widget)
            self.ui.tabla.setItem (row, 9, distancia_widget)
 
            row += 1

        for  particula in particulas:
            self.ui.salida.insertPlainText(str(particula))

    @Slot()
    def action_ordenar_velocidad(self):
        self.ui.salida.clear()
        self.ui.tabla.clear()
        headers = ["Id", "Origen_x", "Origen_y", "Destino_x", "Destino_y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.administrador))

        particulas = []
        for particula in self.administrador:
            particulas.append(particula)
        particulas.sort(key = lambda particula: particula.velocidad, reverse=False)

        row = 0
        for particula in particulas:
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(particula.velocidad)
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem (row, 0, id_widget)
            self.ui.tabla.setItem (row, 1, origen_x_widget)
            self.ui.tabla.setItem (row, 2, origen_y_widget)
            self.ui.tabla.setItem (row, 3, destino_x_widget)
            self.ui.tabla.setItem (row, 4, destino_y_widget)
            self.ui.tabla.setItem (row, 5, velocidad_widget)
            self.ui.tabla.setItem (row, 6, red_widget)
            self.ui.tabla.setItem (row, 7, green_widget)
            self.ui.tabla.setItem (row, 8, blue_widget)
            self.ui.tabla.setItem (row, 9, distancia_widget)
 
            row += 1

        for  particula in particulas:
            self.ui.salida.insertPlainText(str(particula))

    @Slot()
    def dibujar (self):
        pen = QPen ()
        pen.setWidth(2)
        
        for particula in self.administrador:
            r = particula.red
            g = particula.green
            b = particula.blue
            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(particula.origen_x,particula.origen_y,3,3, pen)
            self.scene.addEllipse(particula.destino_x,particula.destino_y,3,3, pen)
            self.scene.addLine(particula.origen_x+3,particula.origen_y+3,particula.destino_x,particula.destino_y, pen)
        

    @Slot()
    def limpiar (self):
        self.scene.clear()

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.administrador:
            if id == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(particula.id)
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(particula.velocidad)
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem (0, 0, id_widget)
                self.ui.tabla.setItem (0, 1, origen_x_widget)
                self.ui.tabla.setItem (0, 2, origen_y_widget)
                self.ui.tabla.setItem (0, 3, destino_x_widget)
                self.ui.tabla.setItem (0, 4, destino_y_widget)
                self.ui.tabla.setItem (0, 5, velocidad_widget)
                self.ui.tabla.setItem (0, 6, red_widget)
                self.ui.tabla.setItem (0, 7, green_widget)
                self.ui.tabla.setItem (0, 8, blue_widget)
                self.ui.tabla.setItem (0, 9, distancia_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning (
                self, 
                "Atención",
                f'La particula con el id "{id}" no fue encontrada'
            )
    
    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen_x", "Origen_y", "Destino_x", "Destino_y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.administrador))

        row = 0
        for particula in self.administrador:
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(particula.velocidad)
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem (row, 0, id_widget)
            self.ui.tabla.setItem (row, 1, origen_x_widget)
            self.ui.tabla.setItem (row, 2, origen_y_widget)
            self.ui.tabla.setItem (row, 3, destino_x_widget)
            self.ui.tabla.setItem (row, 4, destino_y_widget)
            self.ui.tabla.setItem (row, 5, velocidad_widget)
            self.ui.tabla.setItem (row, 6, red_widget)
            self.ui.tabla.setItem (row, 7, green_widget)
            self.ui.tabla.setItem (row, 8, blue_widget)
            self.ui.tabla.setItem (row, 9, distancia_widget)

            row += 1

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administrador.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo" + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print (ubicacion)
        if self.administrador.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo"
            )

    @Slot()
    def click_mostrar(self):
        #self.administrador.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administrador))

    @Slot()
    def click_agregar(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.administrador.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.administrador.agregar_inicio(particula)
