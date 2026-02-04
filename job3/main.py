class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = "à faire"
    
    def marquer_faite(self):
        self.__statut = "terminé"
    
    def get_titre(self):
        return self.__titre
    
    def get_statut(self):
        return self.__statut

    def get_infos(self):
        print(self.__titre, self.__description, self.__statut)
        return (self.__titre, self.__description, self.__statut)

class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def ajouter_tache(self, Tache):
        self.__taches.append(Tache)

    def supprimer_tache(self, tache: str): 
        if tache in self.__taches: 
            self.__taches.remove(tache) 
            print(f"tache {tache.get_titre()} supprimée")
            
    def afficher_taches(self): 
        if not self.__taches: 
            print("Aucune tâche à afficher.") 
        else: 
            for i, t in enumerate(self.__taches, start=1): 
                print(f"{i}. {t.get_titre()}") 
                
    def vider_liste(self): 
        self.__taches.clear() 
            
    def get_taches(self): 
        return list(self.__taches)

    def filtrer_liste(self, statut):
        liste = []
        for t in self.__taches:
            if t.get_statut() == statut:
                liste.append(t.get_titre())
        print(liste)
        return liste


a = Tache("1", "manger")
b = Tache("2", "dormir")
c = Tache("3", "sport")

l = ListeDeTaches()

l.ajouter_tache(a)
l.ajouter_tache(b)
l.ajouter_tache(c)

l.afficher_taches()

l.supprimer_tache(c)
l.afficher_taches()

a.get_infos()
a.marquer_faite()
a.get_infos()

l.filtrer_liste("terminé")
