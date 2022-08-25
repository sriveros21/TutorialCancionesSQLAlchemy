from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.album import Album, Medio
from src.modelo.albumCancion import AlbumCancion
from src.modelo.declarative_base import Session, engine, Base
from sqlalchemy import delete

if __name__ == '__main__':


  Base.metadata.drop_all(engine)
  # session = Session()
  # cancion2 = session.query(Album).get(7)
  # session.delete(cancion2)
  # cancion2 = session.query(Album).get(8)
  # session.delete(cancion2)
  # session.commit()
  # session.close()