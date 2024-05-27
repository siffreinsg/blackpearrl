from pydantic import BaseModel


class SonarrSeries(BaseModel):
    id: int
    title: str
    path: str
    tvdbId: int
    tvMazeId: int
    type: str
    year: int

class SonarrEpisode(BaseModel):
    id: int
    episodeNumber: int
    seasonNumber: int
    title: str
    seriesId: int
    tvdbId: int

class SonarrDeletedItem(BaseModel):
    series: list[SonarrSeries]
    episodes: list[SonarrEpisode]
    eventType: str = "OnDelete"
    instanceName: str
    applicationUrl: str
