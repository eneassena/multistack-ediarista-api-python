class Hateoas:
    def __init__(self) -> None:
        self.links: list = []

    def add_get(self, rel, uri) -> None:
        self.add('GET', rel, uri)

    def add_post(self, rel, uri) -> None:
        self.add('POST', rel, uri)

    def add_put(self, rel, uri) -> None:
        self.add('PUT', rel, uri)

    def add_patch(self, rel, uri) -> None:
        self.add('PATCH', rel, uri)

    def add_delete(self, rel, uri) -> None:
        self.add('DELETE', rel, uri)

    def add(self, _type: str, rel, uri) -> None:
        self.links.append({
            'type': _type,
            'rel': rel,
            'uri': uri
        })

    def to_array(self) -> list:
        return self.links
