import time
import winsound



minimum_wody_dziennie = 2000 #podajemy wartość w mililitrach
wypita_dzis = 0
ile_wypiles_ostatnio = 0
czas_alarmu = 5 * 1



while wypita_dzis < minimum_wody_dziennie:
    time.sleep(czas_alarmu)
    winsound.Beep(700, 1000)
    time.sleep(1)
    winsound.Beep(600, 1000)
    time.sleep(1)
    winsound.Beep(800, 1000)
    czy_sie_napiles = input("Czy od ostatniego zerknięcia do aplikacji napiłeś/aś się wody?: ")
    
    
    
    if czy_sie_napiles == "Tak" or czy_sie_napiles == "tak":
        ile_wypiles_ostatnio = int(input("Ile mililitrów wypiłeś ostatnio?: "))
        wypita_dzis += ile_wypiles_ostatnio 
    else:
        print("Napij się teraz!!!!")
        
        ile_wypiles_ostatnio = int(input("Ile teraz wypiłeś/aś?: "))
        wypita_dzis += ile_wypiles_ostatnio 
        
    print(f"Wypiłeś/aś dziś {wypita_dzis} ml wody. ")
        