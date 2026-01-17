import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G=nx.DiGraph()
        self.lista_geni=[]
        self.dict_geni={}
        self.lista_cromosomi=[]
        self.lista_connessioni=[]
        self.percorso_migliore = []
        self.peso_migliore = 0

    def build_graph(self):
        self.G.clear()
        self.lista_geni = []
        self.dict_geni = {}
        self.lista_cromosomi = []
        self.lista_connessioni = []
        geni=DAO.get_geni()
        for gene in geni:
            self.lista_geni.append(gene)
            self.dict_geni[gene.id]=gene
        cromosomi=DAO.get_cromosomi()
        for c in cromosomi:
            self.lista_cromosomi.append(c)
        self.G.add_nodes_from(self.lista_cromosomi)
        connessioni=DAO.get_connessioni()
        for connessione in connessioni:
            self.lista_connessioni.append(connessione)
        self.G.add_weighted_edges_from(self.lista_connessioni)

    def get_max_min(self):
        massimo=float("-inf")
        minimo=float("inf")
        for u,v,w in self.G.edges(data="weight"):
            if w>massimo:
                massimo=w
            if w<minimo:
                minimo=w

        return massimo, minimo

    def get_pesi_soglia(self,soglia):
        count_maggiori=0
        count_minori=0
        for u,v,w in self.G.edges(data="weight"):
            if w<soglia:
                count_minori+=1
            elif w>soglia:
                count_maggiori+=1
        return count_maggiori, count_minori

    def get_percorso(self,soglia):
        self.percorso_migliore=[]
        self.peso_migliore=0
        for nodo in self.G.nodes():
            self.ricorsione(soglia,[nodo],[],0)
        return self.percorso_migliore,self.peso_migliore

    def ricorsione(self,soglia,parziale, archi_visitati,peso_tot):
        ultimo=parziale[-1]
        if peso_tot>self.peso_migliore:
            self.peso_migliore=peso_tot
            self.percorso_migliore=parziale.copy()

        vicini=self.G.neighbors(ultimo)
        for vicino in vicini:
            w=self.G[ultimo][vicino]["weight"]
            arco_corrente=(ultimo,vicino)
            if w>soglia and arco_corrente not in archi_visitati:
                parziale.append(vicino)
                archi_visitati.append(arco_corrente)
                self.ricorsione(soglia,parziale,archi_visitati,peso_tot+w)
                parziale.pop()
                archi_visitati.pop()



























