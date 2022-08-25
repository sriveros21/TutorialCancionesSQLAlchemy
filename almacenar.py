from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.album import Album, Medio
from src.modelo.albumCancion import AlbumCancion
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
   #Creacion de la base de datos
   Base.metadata.create_all(engine)

   #Abre la sesión
   session = Session()

   #Crear intérpretes
   #Se debe anotar que no se asignaron identificadores a la propiedad id de la clase, 
   # ya que al almacenarlos se generan los identificadores de los intérpretes.

   #Creacion de los objetos
   interprete1 = Interprete(nombre = "Samuel Torres", texto_curiosidades = "Es colombiano y vive en NY")
   interprete2 = Interprete(nombre = "Aldo Gavilan", texto_curiosidades = "Cantó a Cuba")
   interprete3 = Interprete(nombre = "Buena Vista Social club")
   interprete4 = Interprete(nombre = "Arturo Sandoval", texto_curiosidades = "No sabía quien era")

   #Adicionar objetos creados a la sesion definida
   #Al ejecutar la instrucción `session.add`, los intérpretes fueron provistos de un valor en su propiedad id, 
   # por lo que se puede utilizar este identificador para crear las relaciones con las canciones.
   session.add(interprete1)
   session.add(interprete2)
   session.add(interprete3)
   session.add(interprete4)

   #Completar el almacenamiento de los objetos creados
   session.commit()

   # Crear álbumes
   album1 = Album(titulo = "Latin Jazz Compilation", ano = 2021, descripcion = "Album original", medio = Medio.DISCO)
   album2 = Album(titulo = "Bandas sonoras famosas", ano = 2021, descripcion = "Compilación", medio = Medio.DISCO)
   session.add(album1)
   session.add(album2)


   # Crear canciones
   cancion1 = Cancion(titulo = "Ajiaco", minutos = 3, segundos = 1, compositor = "Samuel Torres")
   cancion2 = Cancion(titulo = "Forced Displacement", minutos = 3, segundos = 12, compositor = "Desconocido")
   cancion3 = Cancion(titulo = "Alegría", minutos = 4, segundos = 27, compositor = "AU")
   session.add(cancion1)
   session.add(cancion2)
   session.add(cancion3)

   # Relacionar albumes con canciones
   album1.canciones = [cancion1, cancion2]
   album2.canciones = [cancion1, cancion3]

   # Relacionar canciones con intérpretes
   cancion1.interpretes = [interprete1]
   cancion2.interpretes = [interprete2]
   cancion3.interpretes = [interprete3, interprete4]
   session.commit()

   session.commit()
   session.close()