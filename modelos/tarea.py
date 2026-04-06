class Tarea:
    def _init_(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True
