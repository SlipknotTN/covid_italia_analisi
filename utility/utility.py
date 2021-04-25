def get_colore(articolo: str) -> str:
    if articolo == "art.1":
        return "yellow"
    elif articolo == "art.2":
        return "orange"
    elif articolo == "art.3":
        return "red"
    else:
        raise Exception(f"{articolo} non supportato")
