"""Representar los miembros de una familia
Se ha formado una tabla familias con 1000 componentes numerados desde 1. Cada componente contiene un dato de tipo PERSONA.
La asociación reflexiva en la entidad PERSONA, designada en el diagrama por «es el hijo de», significa que una instancia de PERSONA es hija (hijo) de ninguna, de una o de dos instancias de PERSONA.
1. Definir el tipo PERSONA. ¿Cómo declarar la tabla familias?
Cuando una persona registrada en la tabla no tiene padre o madre registrado, el atributo correspondiente es HUÉRFANO. Cuando una celda no está ocupada porque la persona que contenía se ha borrado, su identificador es BORRADO. Las celdas que nunca han recibido valor, cuando hay menos de 1000 personas registradas, tienen un identificador igual a VACÍO.
2. Dar la lista de todas las personas registradas con una edad de 20 a 30 años.
3. Envejecer 1 año a todas las personas registradas.
4. Establecer la lista de todos los huérfanos de menos de 15 años.
5. Hacer un algoritmo que determina la identidad del padre de ’Jaime MARTÍN’.
6. Hacer un algoritmo que establezca la lista de los hermanos y hermanas de ’Jaime MARTÍN’."""