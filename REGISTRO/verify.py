from models import Corso, Partecipante, Presenza
from data_manager import DataManager
import os
import uuid

def test_flow():
    test_file = "test_data.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("Testing Models...")
    # Use explicit UUIDs for testing
    cid = str(uuid.uuid4())
    pid1 = str(uuid.uuid4())
    pid2 = str(uuid.uuid4())
    
    corso = Corso("Python", cid, 100)
    p1 = Partecipante("Giacomo", "Leopardi", pid1)
    p2 = Partecipante("Alessandro", "Manzoni", pid2)
    
    # Iscrizione
    p1.iscrivi_corso(corso)
    p2.iscrivi_corso(corso)
    assert len(corso.lista_partecipanti) == 2
    assert cid in p1.lista_corsi
    
    # Presenze
    p1.registra_presenza(cid, "2023-10-01", 1) # Presente
    p1.registra_presenza(cid, "2023-10-02", 0) # Assente
    
    stats = p1.presenze_corsi[cid].get_presenze()
    assert stats["2023-10-01"] == 1
    assert stats["2023-10-02"] == 0
    assert p1.presenze_corsi[cid].calcola_ore_assenza() == 1
    
    print("Models OK.")
    
    print("Testing Persistence...")
    DataManager.salva_dati([corso], [p1, p2], test_file)
    
    loaded_corsi, loaded_parts = DataManager.carica_dati(test_file)
    
    assert len(loaded_corsi) == 1
    assert len(loaded_parts) == 2
    
    lc = loaded_corsi[0]
    assert lc.nome == "Python"
    assert len(lc.lista_partecipanti) == 2 # Check linkage
    
    lp1 = next(p for p in loaded_parts if p.matricola == pid1)
    assert cid in lp1.lista_corsi
    # Check if attendance is preserved
    assert lp1.presenze_corsi[cid].get_presenze().get("2023-10-01") == 1
    
    print("Persistence OK.")
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)

if __name__ == "__main__":
    try:
        test_flow()
        print("ALL TESTS PASSED")
    except Exception as e:
        print(f"TEST FAILED: {e}")
