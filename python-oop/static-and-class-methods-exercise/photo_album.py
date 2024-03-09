class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(0, pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        if photos_count % 4 != 0:
            return cls(photos_count // 4 + 1)
        else:
            return cls(photos_count // 4)

    def add_photo(self, label: str):
        for i in range(0, len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i+1} slot {len(self.photos[i])}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            row = []
            for item in page:
                if item != " ":
                    row.append("[]")
            result += ' '.join(row)
            result += "\n-----------\n"
        return result.strip()
