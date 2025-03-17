# webscrappingACG
Un código de Python que permite escanear páginas en html para encontrar los comentarios y correos dentro de la página.
Primero, se obtiene el código html de la página mediante la clase request, después, se crea un objeto de la clase BeautifulSoup.
Ahora, mediante el método find_all, buscamos todos los strings de la página que coincidan con la expresión regular indicada,
la cual permite que comience con cualquier letra del abecedario, números e incluso caracteres especiales como _, seguido de un @, y
después letras del abecedarios o números para el dominio (gmail,hotmail,etc.), permitiendo varios dominios. 
Después, se imprimen los correos.
Ahora, mediante el método find_all, buscamos todos los strings pero esta vez sean una instancia de la clase Comment, que es la que
se usa para representar los comentarios. Por último, se imprimen los comentarios. 
