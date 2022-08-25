from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

""" class AlbumCancion(Base):
    __tablename__ = 'album_cancion'

    cancion = Column(
        Integer,
        ForeignKey('cancion.id'),
        primary_key=True)

    album = Column(
        Integer,
        ForeignKey('album.id'),
        primary_key=True) """


class Cancion(Base):
    __tablename__ = 'cancion'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)
    albumes = relationship('Album', secondary='album_cancion', back_populates="canciones")
    interpretes = relationship('Interprete', cascade='all, delete, delete-orphan')

