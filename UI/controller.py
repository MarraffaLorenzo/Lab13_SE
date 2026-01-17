import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        self._model.build_graph()
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(
            f"Numero di vertici: {self._model.G.number_of_nodes()} Numero di vertici: {self._model.G.number_of_edges()}"))
        massimo,minimo=self._model.get_max_min()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(
            f"Infromazioni sui pesi degli archi - valore minimo: {minimo} e valore massimo: {massimo}"))
        self._view.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        self._view.lista_visualizzazione_2.controls.clear()
        soglia=float(self._view.txt_name.value)
        if soglia>=3.0 and soglia<=7.0:
            n_maggiori,n_minori=self._model.get_pesi_soglia(soglia)
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {n_maggiori}"))
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {n_minori}"))
        else:
            self._view.show_alert(f"Inserire un numero compreso tra 3 e 7")
        self._view.update()

    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        soglia = float(self._view.txt_name.value)
        percorso,peso=self._model.get_percorso(soglia)
        self._view.lista_visualizzazione_3.controls.clear()
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f"Numero archi percorso più lungo: {len(percorso)-1}"))
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f"Peso cammino massimo: {peso}"))
        for i in range(len(percorso)-1):
            nodo1=percorso[i]
            nodo2=percorso[i+1]
            w=self._model.G[nodo1][nodo2]['weight']
            self._view.lista_visualizzazione_3.controls.append(ft.Text(
                f"{nodo1} --> {nodo2} : {w}"))
        self._view.update()