from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

class AlbumCancion(Base):
    __tablename__ = 'album_cancion'

    cancion = Column(
        Integer,
        ForeignKey('cancion.id'),
        primary_key=True)

    album = Column(
        Integer,
        ForeignKey('album.id'),
        primary_key=True)