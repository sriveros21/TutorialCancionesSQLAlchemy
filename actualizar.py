from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.albumCancion import AlbumCancion
from src.modelo.album import Album
from src.modelo.declarative_base import Session, engine, Base


if __name__ == '__main__':
  session = Session()
  #Se trae la cancion con el id=2
  cancion = session.query(Cancion).get(2)
  #Se trae el interprete con el id=4
  interprete = session.query(Interprete).get(4)

  cancion.minutos = 5
  cancion.segundos = 30
  cancion.compositor = "Pedro Pérez"
  cancion.interpretes.append(interprete)
  session.add(cancion)
  session.commit()
  session.close()