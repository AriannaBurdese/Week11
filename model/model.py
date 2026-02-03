from database.DAO import DAO
import networkx as nx
from model.connessione import Connessione
class Model:
    def __init__(self):
        self._objects_list = []
        self.getObjects()
        # mi posso creare anche un dizionario di Object
        self._objects_dict = {} # è la idMap di Object
        for o in self._objects_list:
            self._objects_dict[o.object_id] = o

        self._grafo = nx.Graph()


    def getObjects(self):
        self._objects = DAO.readObjects()

    def buildGrafo(self):
        #nodi
        self._grafo.add_nodes_from(self._objects_list)
        #archi

        #modo 1 (80k x 80k query sql, dove 80k sono i nodi)
        """"
        for o in self._objects_list:
            for v in self._objects_list:
                DAO.readEdges(u,v) #da scrivere """

        # modo 2 (usare una query sola per estrarre le connessioni)
        connessioni = DAO.readConnessioni()
        #leggo le connessioni del Dao
        for c in connessioni:
            self._grafo.add_edge(c.o1, c.o2, peso=c.peso)

    def calcolaConnessa(self, id_nodo):
        nodo_sorgente = self._objects_dict[id_nodo]
        successori = nx.dfs_successors(self._grafo, nodo_sorgente)
        print(f"successori:{successori}")
        