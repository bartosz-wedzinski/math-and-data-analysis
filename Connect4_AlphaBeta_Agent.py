import math
import copy

# --- KONFIGURACJA ---
WIERSZE = 6
KOLUMNY = 7
PUSTE = 0
GRACZ_AI = 1        
GRACZ_LUDZKI = 2   
DLUGOSC_OKNA = 4

class Connect4AI_Turbo:
    def __init__(self):
        self.plansza = [[PUSTE for _ in range(KOLUMNY)] for _ in range(WIERSZE)]
        # Stała kolejność sprawdzania kolumn: od środka na zewnątrz
        # Dla planszy szerokości 7 to: [3, 2, 4, 1, 5, 0, 6]
        self.kolejnosc_kolumn = sorted(range(KOLUMNY), key=lambda k: abs(k - KOLUMNY // 2))

    def drukuj_plansze(self):
        print("\n--- AKTUALNA SYTUACJA ---")
        for rzad in range(WIERSZE - 1, -1, -1):
            linia = [str(i) for i in self.plansza[rzad]]
            print(" | ".join(linia))
        print("-" * 25)
        print(" 0   1   2   3   4   5   6  (Numery kolumn)")
        print()

    def sprawdz_czy_poprawny_ruch(self, kolumna):
        return self.plansza[WIERSZE - 1][kolumna] == PUSTE

    def znajdz_pierwszy_wolny_wiersz(self, kolumna):
        for r in range(WIERSZE):
            if self.plansza[r][kolumna] == PUSTE:
                return r
        return None

    def wykonaj_ruch(self, rzad, kolumna, pionek):
        self.plansza[rzad][kolumna] = pionek

    def cofnij_ruch(self, rzad, kolumna):
        self.plansza[rzad][kolumna] = PUSTE

    def sprawdz_wygrana_lokalna(self, r, c, pionek):
        """
        Sprawdza wygraną TYLKO wokół ostatnio położonego żetonu (r, c).
        Oszczędza mnóstwo czasu procesora.
        """
        plansza = self.plansza
        
        # Kierunki: [poziomo, pionowo, skos /, skos \]
        # (delta_row, delta_col)
        kierunki = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for dr, dc in kierunki:
            count = 1  # Zliczamy aktualny pionek
            
            # Sprawdź w jedną stronę (np. w prawo)
            for i in range(1, 4):
                nr, nc = r + dr * i, c + dc * i
                if 0 <= nr < WIERSZE and 0 <= nc < KOLUMNY and plansza[nr][nc] == pionek:
                    count += 1
                else:
                    break
            
            # Sprawdź w drugą stronę (np. w lewo - przeciwny zwrot wektora)
            for i in range(1, 4):
                nr, nc = r - dr * i, c - dc * i
                if 0 <= nr < WIERSZE and 0 <= nc < KOLUMNY and plansza[nr][nc] == pionek:
                    count += 1
                else:
                    break
            
            if count >= 4:
                return True
        return False

    def ocena_okna(self, okno, pionek):
        score = 0
        przeciwnik = GRACZ_LUDZKI if pionek == GRACZ_AI else GRACZ_AI

        if okno.count(pionek) == 4:
            score += 100000
        elif okno.count(pionek) == 3 and okno.count(PUSTE) == 1:
            score += 100
        elif okno.count(pionek) == 2 and okno.count(PUSTE) == 2:
            score += 10

        if okno.count(przeciwnik) == 3 and okno.count(PUSTE) == 1:
            score -= 1000 

        return score

    def ocena_pozycji(self, pionek):
        """Heurystyka oceniająca statyczny stan planszy."""
        score = 0
        plansza = self.plansza

        # Preferuj środek
        srodek_array = [plansza[r][KOLUMNY // 2] for r in range(WIERSZE)]
        score += srodek_array.count(pionek) * 3

        # Skanuj okna (uproszczone skanowanie całej planszy tylko w liściach drzewa)
        # Poziomo
        for r in range(WIERSZE):
            row = plansza[r]
            for c in range(KOLUMNY - 3):
                score += self.ocena_okna(row[c:c+4], pionek)
        # Pionowo
        for c in range(KOLUMNY):
            col = [plansza[r][c] for r in range(WIERSZE)]
            for r in range(WIERSZE - 3):
                score += self.ocena_okna(col[r:r+4], pionek)
        # Skosy
        for r in range(WIERSZE - 3):
            for c in range(KOLUMNY - 3):
                okno = [plansza[r+i][c+i] for i in range(4)]
                score += self.ocena_okna(okno, pionek)
                okno = [plansza[r+3-i][c+i] for i in range(4)]
                score += self.ocena_okna(okno, pionek)

        return score

    def pobierz_posortowane_ruchy(self):
        """Zwraca listę wolnych kolumn posortowaną wg priorytetu środka."""
        # Filtrujemy self.kolejnosc_kolumn sprawdzając czy ruch jest możliwy
        return [c for c in self.kolejnosc_kolumn if self.plansza[WIERSZE-1][c] == PUSTE]

    # --- MINIMAX Z ALPHA-BETA ---
    def minimax(self, glebokosc, alpha, beta, maxymalizujacy_gracz, ostatni_ruch):
        """
        ostatni_ruch: krotka (rzad, kolumna), która doprowadziła do tego stanu.
        Służy do szybkiego sprawdzenia czy gra się zakończyła.
        """
        
        # 1. Sprawdzenie czy ostatni ruch zakończył grę
        if ostatni_ruch is not None:
            r, c = ostatni_ruch
            # Kto zrobił ostatni ruch?
            # Jeśli teraz jest tura MAX (AI), to ostatni ruch robił MIN (Człowiek).
            # Jeśli MIN wygrał, zwracamy bardzo niską wartość.
            if maxymalizujacy_gracz: 
                if self.sprawdz_wygrana_lokalna(r, c, GRACZ_LUDZKI):
                    return (None, -100000000000 - glebokosc)
            else: # Tura MIN (Człowiek), ostatni ruch robił MAX (AI)
                if self.sprawdz_wygrana_lokalna(r, c, GRACZ_AI):
                    return (None, 100000000000 + glebokosc)

        # Sprawdzenie remisu (brak ruchów)
        prawidlowe_ruchy = self.pobierz_posortowane_ruchy()
        if not prawidlowe_ruchy:
            return (None, 0)

        # 2. Baza rekurencji (głębokość 0)
        if glebokosc == 0:
            return (None, self.ocena_pozycji(GRACZ_AI))

        # 3. Rekurencja
        if maxymalizujacy_gracz:
            wartosc = -math.inf
            # Domyślnie pierwsza wolna z posortowanych (najbliżej środka)
            najlepsza_kolumna = prawidlowe_ruchy[0]

            for kol in prawidlowe_ruchy:
                rzad = self.znajdz_pierwszy_wolny_wiersz(kol)
                
                # RUCH
                self.wykonaj_ruch(rzad, kol, GRACZ_AI)
                
                # REKURENCJA (przekazujemy (rzad, kol) jako ostatni ruch)
                nowy_wynik = self.minimax(glebokosc - 1, alpha, beta, False, (rzad, kol))[1]
                
                # COFNIĘCIE RUCHU 
                self.cofnij_ruch(rzad, kol)

                if nowy_wynik > wartosc:
                    wartosc = nowy_wynik
                    najlepsza_kolumna = kol
                
                alpha = max(alpha, wartosc)
                if alpha >= beta:
                    break
            return (najlepsza_kolumna, wartosc)

        else: # Gracz minimalizujący (Ludzki)
            wartosc = math.inf
            najlepsza_kolumna = prawidlowe_ruchy[0]

            for kol in prawidlowe_ruchy:
                rzad = self.znajdz_pierwszy_wolny_wiersz(kol)
                
                # RUCH
                self.wykonaj_ruch(rzad, kol, GRACZ_LUDZKI)
                
                # REKURENCJA
                nowy_wynik = self.minimax(glebokosc - 1, alpha, beta, True, (rzad, kol))[1]
                
                # COFNIĘCIE RUCHU
                self.cofnij_ruch(rzad, kol)

                if nowy_wynik < wartosc:
                    wartosc = nowy_wynik
                    najlepsza_kolumna = kol
                
                beta = min(beta, wartosc)
                if alpha >= beta:
                    break
            return (najlepsza_kolumna, wartosc)

# --- PĘTLA GRY ---
def graj():
    gra = Connect4AI_Turbo()
    koniec_gry = False
    tura = 0 
    
    # Do śledzenia ostatniego ruchu (potrzebne do sprawdzenia wygranej w głównej pętli)
    ostatni_ruch_main = None 

    gra.drukuj_plansze()

    while not koniec_gry:
        # TURA CZŁOWIEKA
        if tura == 0:
            try:
                wybor = int(input("Twój ruch (0-6): "))
                if wybor < 0 or wybor > 6:
                    print("Błędna kolumna.")
                    continue
            except ValueError:
                continue

            if gra.sprawdz_czy_poprawny_ruch(wybor):
                rzad = gra.znajdz_pierwszy_wolny_wiersz(wybor)
                gra.wykonaj_ruch(rzad, wybor, GRACZ_LUDZKI)
                
                # Szybkie sprawdzenie wygranej
                if gra.sprawdz_wygrana_lokalna(rzad, wybor, GRACZ_LUDZKI):
                    gra.drukuj_plansze()
                    print("BRAWO! Wygrałeś :3")
                    koniec_gry = True
                
                tura = 1
                gra.drukuj_plansze()
            else:
                print("Kolumna pełna!")

        # TURA AI
        else:
            print("AI myśli...")
            glebokosc = 7
            kolumna, _ = gra.minimax(glebokosc, -math.inf, math.inf, True, None)

            if gra.sprawdz_czy_poprawny_ruch(kolumna):
                rzad = gra.znajdz_pierwszy_wolny_wiersz(kolumna)
                gra.wykonaj_ruch(rzad, kolumna, GRACZ_AI)

                if gra.sprawdz_wygrana_lokalna(rzad, kolumna, GRACZ_AI):
                    gra.drukuj_plansze()
                    print("AI Wygrało :c")
                    koniec_gry = True
                
                tura = 0
                gra.drukuj_plansze()

if __name__ == "__main__":
    graj()
    
    
# Zaprezentowana powyżej wersja "turbo" jest mocno zoptymalizowanym wariantem pierwotnego kodu. Zmieniono kopiowanie tabeli przy każdym analizowanym wariancie na modyfikację w miejscu z cofaniem oraz sprawdzanie, czy jest już wygrana z całej planszy na jedynie okolicę ostatniego włożonego żetonu. Pozwoliło to na uzyskanie podobnego czasu odpowiedzi dla głębokości = 7, co dla pierwotnego kodu przy głębokości = 5. Dodatkowo zmieniono wartości premii na lepiej działające, wybieranie kolumny z losowo wybranej na priorytetowo kolumny centralne oraz uwzględniono preferencje, co do szybszej wygranej i późniejszej przegranej (dotychczasowo wygrana AI za 5 ruchów była tyle samo punktowana, co za 1, więc mogło wybrać pierwszą opcję, co jest nieintuicyjne i bezsensowne).

# W celu zmiany trudności rozgrywki można zmienić wartość głębokości. Obecnie zastosowana wartość równa 7 jest więcej, niż wystarczająca do pokonania zdecydowanej większości graczy, a jednocześnie najwyższą możliwą, by uzyskiwać relatywnie szybkie odpowiedzi przez całość partii.
    

    
