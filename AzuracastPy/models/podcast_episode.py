class Links:
    def __init__(self_, self: str, public: str, download: str, art: str, media: str):
        self_.self = self
        self_.public = public
        self_.download = download
        self_.art = art
        self_.media = media

    def __repr__(self_):
        return (
            f"Links(self={self_.self!r}, public={self_.public!r}, download={self_.download!r}, "
            f"art={self_.art!r}, media={self_.media!r})"
        )

class Media:
    def __init__(self, id: str, original_name: str, length: int, length_text: str, path: str):
        self.id = id
        self.original_name = original_name
        self.length = length
        self.length_text = length_text
        self.path = path

    def __repr__(self):
        return (
            f"Media(id={self.id!r}, original_name={self.original_name!r}, length={self.length!r}, "
            f"length_text={self.length_text!r}, path={self.path!r})"
        )

class PodcastEpisode:
    def __init__(
            self, id: str, title: str, description: str, explicit: bool, publish_at: int, has_media: bool,
            media: Media, has_custom_art: bool, art: str, art_updated_at: int, links: Links
        ):
        self.id = id
        self.title = title
        self.description = description
        self.explicit = explicit
        self.publish_at = publish_at
        self.has_media = has_media
        self.media = media
        self.has_custom_art = has_custom_art
        self.art = art
        self.art_updated_at = art_updated_at
        self.links = links

    def __repr__(self):
        return (
            f"PodcastEpisode(id={self.id!r}, title={self.title!r}, description={self.description!r}, "
            f"explicit={self.explicit!r}, publish_at={self.publish_at!r}, has_media={self.has_media!r}, "
            f"media={self.media!r}, has_custom_art={self.has_custom_art!r}, art={self.art!r}, "
            f"art_updated_at={self.art_updated_at!r}, links={self.links!r})"
        )