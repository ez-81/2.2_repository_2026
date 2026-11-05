def naam_opvragen() -> str:
    naam = input("Wat is jouw naam? ")
    return naam


def leeftijd_opvragen() -> int:
    leeftijd = int(input("Wat is jouw leeftijd? "))
    return leeftijd


def gebruiker_begroeten(naam: str) -> None:
    bericht = f"Hallo {naam}, welkom bij dit programma!"
    print(bericht)


def leeftijd_verhogen(leeftijd: int) -> int:
    verhoogde_leeftijd = leeftijd + 10
    return verhoogde_leeftijd


def main() -> None:
    naam = naam_opvragen()
    leeftijd = leeftijd_opvragen()
    gebruiker_begroeten(naam)
    verhoogde_leeftijd = leeftijd_verhogen(leeftijd)
    bericht = f"Je bent nu {leeftijd} jaar oud. Over 10 jaar ben je {verhoogde_leeftijd} jaar oud."
    print(bericht)


if __name__ == "__main__":
    main()
