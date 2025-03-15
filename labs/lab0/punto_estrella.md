## Tarea Estrella

Opcionalmente, y con la posibilidad de que se otorguen puntos extras en la evaluación parcial, se pide investigar qué mecanismos permiten funcionar a nombres de dominio como:
- http://中文.tw/
- https://💩.la

    Ayuda: investigue sobre el término “encoding”.


Los nombres de dominio como http://中文.tw/ o https://💩.la  utilizan un mecanismo de codificación de caracteres para poder funcionar. 
El método que utilizan se llama **"Punycode"**. Es un algoritmo de Encoding (proceso por el cual se transforma información textual humana,  en un conjunto más reducido para ser almacenado, por ejemplo asignandole números) Lo que hace es convertir caracteres Unicode (estandar de codificación de caracteres que incluye letras en diferentes idiomas, emojis, etc) en una representación ASCII que es compatible con el DNS.

Lo que hace es lo siguiente: 
1. Conversión a Unicode (el nombre del dominio se convierte a Unicode)
2. Mapeo a valores númericos (A cada caracter unicode se le asigna valores númericos siguiendo el estándar de punycode)
3. Concatenación (se concatenan los números separados por un guión)
4. Prefijo ACE (se le agrega al principio xn-- para indicair que el nombre de dominio esta codificado)
5. Conversión a ASCII (Por último esa cadena se covierte a ASCII)
