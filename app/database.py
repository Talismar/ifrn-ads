from app.entities import Artiche


class Database:
    def __init__(self) -> None:
        self.artiches: list[Artiche] = []

    def create_artiches(self, title: str, content: str):
        id = len(self.artiches)

        artiche = Artiche(id, title, content)
        self.artiches.append(artiche)

        return artiche

    def get_by_id(self, artiche_id: int):
        artiche: Artiche | None = None

        for item in self.artiches:
            if item.id == artiche_id:
                artiche = item
                break

        if artiche is None:
            raise Exception("Artiche not found")

        return artiche

    def delete_artiche(self, artiche_id: int):
        try:
            artiche_to_remove = self.get_by_id(artiche_id)
            self.artiches.remove(artiche_to_remove)
        except Exception as exception:
            raise exception
