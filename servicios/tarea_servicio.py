from modelos.tarea import Tarea

class TareaServicio:
    def _init_(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        if descripcion.strip() != "":
            tarea = Tarea(descripcion)
            self.tareas.append(tarea)

    def obtener_tareas(self):
        return self.tareas

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
