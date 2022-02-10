
![img](https://i.ibb.co/D80PqHF/lofo.png)

# Desarrollo de Software con Python
____
## 1 Introducción informal a Python

A continuación los *input* y *output* del intérprete son distinguidos por la presencia y ausencia de **>>>** y **...** respectivamente. Muchos ejemplos también incluyen comentarios. Los comentarios en Python empiezan con **#**.

### 1.1 Usando Python como una calculadura
El intérprete actúa como una simple calculadora: puedes escribir una expresión y escribirá el resultado. La sintaxis de expresión es sencilla: los operadores +, -, * y / funcionan como en la mayoría de los otros lenguajes (por ejemplo, Pascal o C); los paréntesis (()) se pueden utilizar para agrupar. Por ejemplo:

```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # División siempre regresa un flotante
1.6
```
Los números enteros (por ejemplo, 2, 4, 20) tienen el tipo **int**, los que tienen una parte fraccionaria (por ejemplo, 5.0, 1.6) tienen el tipo **float**. 

La división (/) siempre devuelve un **float**. Para hacer una división entera (descartando cualquier resultado fraccionario) puedes usar el operador **//**; para calcular el resto puedes utilizar **%**:

```python
>>> 17 / 3  # División clásica
5.666666666666667
>>> 17 // 3  # División entera
5
>>> 17 % 3  # Residuo
2
```

Para calcular potencias se utiliza el operador **\*\***:

```python
>>> 5 ** 2  
25
>>> 2 ** 7  
128
```

Se calcularon $5^2 $ y  $2^7 $ en el ejemplo anterior.

El operador **=** sirve para asignar un valor a una variable. El resultado no se muestra con esta operación:

```python
>>> masa = 100
>>> aceleracion = 20 
>>> masa*aceleracion
2000
```

Otras maneras útiles de asignar variables:

```python
>>> masa = 100; aceleracion = 20
>>> masa, aceleracion = 100, 20
```

```python
>>> a = 0; b = 0
>>> a = b = 0
```


Si una variable no está definida te dará un error:

```python
>>> n  # n no está definida
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

Se soportan las operaciones entre **int** y **float**:

```python
>>> 4 * 3.75 - 1
14.0
```

En el **modo interactivo** el último resultado se puede ocupar con la variable **_**. Esto permite que sigas utilizando Python como una calculadora.


```python
>>> iva = 0.16
>>> total = 1000
>>> iva*total
160
>>> total + _ # A la variable _ se le asignó el resultado anterior
1160
```

### 1.2 Strings

Apart de números, Python también manipula texto (strings) y pueden ser representados de muchas maneras. Puede ser con dobles comillas o comillas simples dando el mismo resultado. El caracter **\\** sirve para tomar caracteres especiales.

```python
>>> 'Hola mundo'  # Comillas simples
'Hola mundo'
>>> 'doesn\'t'  # Si se necesita utilizar el caracter de comillas
"doesn't"
>>> "doesn't"  # O simplemente utilizar comillas diferentes
"doesn't"
```

A veces en el modo interactivo, los caracteres especiales son mostrados de diferente manera. Para ver una salida más legible se utiliza la función **print()**:



```python
>>> s = 'Primer linea.\nSegunda linea.'  # \n es salto de linea
>>> s  # Sin print(), el \n es incluido
'First line.\nSecond line.'
>>> print(s)  # Con print(), \n produce una nueva linea
First line.
Second line.

```

Los caracteres especiales pueden causar problemas, por ejemplo:
```python
>>> print('C:\some\name')  # Aqui \n significa nueva linea
C:\some
ame

```

Para ignorar los caracteres especiales, puedes poner una **r** antes de la primer comilla. Esto se le llama *raw strings*.


```python
>>> print(r'C:\some\name')  # nota la r antes de la comilla
C:\some\name
```

Los strings pueden ser creados en multiples lineas utilizando triples comillas (simples o dobles). Los saltos de línea son agregados automáticamente, pero es posible quitarlos añadiendo un **\\** al final de la línea:


```python
>>> print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

Puedes imprimir variables con print de la siguiente manera:

```python
>>> nacimiento = 2000; actual = 2021
>>> edad = actual - nacimiento
>>> print("Tienes", edad, "años" ) 
"Tienes 21 años"
```
De hecho puedes saltar el paso de la asignación de *edad*, poniendo la operación dentro del print:

```python
>>> nacimiento = 2000; actual = 2021
>>> print("Tienes", actual - nacimiento, "años" )
"Tienes 21 años"
```

Print puede recibir todos los strings y todas las variables que quieras.

Otra manera de mostrar variables dentro de strings es añadiendo una **f** antes de la primer comilla y escribiendo las variables dentro de llaves **{}**:

```python
>>> nacimiento = 2000; actual = 2021
>>> edad = actual - nacimiento
>>> frase = f"Tienes {edad} años"
>>> print(frase)
"Tienes 21 años"
```
De igual manera puedes resumir todo dentro del print:

```python
>>> nacimiento = 2000; actual = 2021
>>> print(f"Tienes {actual - nacimiento} años")
"Tienes 21 años"
```


Puedes pegar (concatenar) strings con el operador $+$ y repetirlos con el operador $*$: 

```python
>>> # 3 veces 'un', seguido de 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

Dos o más strings pueden ser concatenados si están juntos

```python
>>> 'Py' 'thon'
'Python'

```

Este feature es muy útil cuando tienes que escribir mucho texto. Puedes abrir paréntesis y poner los siguientes strings en diferentes lineas:
```python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'

```

Esto solo funciona con dos literales, no con variables o expresiones. Para concatenar dos variables que contienen un string utiliza $+$.
```python
>>> a = 'hola'
>>> b = ' mundo'
>>> a + b
"hola mundo"
```


Los Strings contienen métodos especiales muy útiles:

```python
>>> a = 'hola'
>>> a.replace('o','a')
"hala"
```

```python
>>> a.upper()
"HOLA"
```

```python
>>> a.capitalize()
"Hola   "
```

Y más que estaremos revisando más adelante.
___
Los strings pueden ser indexados, teniendo el primer elemento la posición 0. No existe el tipo de dato **caracter** en Python, simplemente es un string con longitud 1.
```python
>>> word = 'Python'
>>> word[0]  # caracter en posición 0
'P'
>>> word[5]  # caracter en posición 5
'n'
```

Los índices pueden ser negativos, empezando a contar desde la derecha:

```python
>>> word[-1]  # ultimo caracter
'n'
>>> word[-2]  # penultimo caracter
'o'
>>> word[-6]
'P'

```
Nota que -0 es igual a 0, los índices negativos empiezan desde -1.

En adición a la indexación, también se soporta *slicing*. Mientras que la idexación te permite obtener caracteres, slicing te permite obtener *substrings*.

```python
>>> word[0:2]  # caracteres desde 0 (incluído) a 2(excluído)
'Py'
>>> word[2:5]  # caracteres desde 2 (incluído) a 5(excluído)
'tho'
```

Los slices tienen valores por defecto muy útiles:


```python
>>> word[:2]   # substring desde el principio hasta caracter 2(excluído)
'Py'
>>> word[4:]   # caracteres desde 4 (incluído) hasta el final
'on'
>>> word[-2:]  # caracteres desde la penultima posición hasta el final
'on'

```
Observa que el primer valor siempre es incluyente y el segundo valor es excluyente. Esto hace que ```s[:i] + s[:i]``` siempre sea igual a s.


```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'

```

Usando indíces muy grandes (mayores a la longitud del string) provoca un error:


```python
>>> word[42]  # El string solo tiene 6 caracteres
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

Usando Slicing no causa error:
```python
>>> word[4:42]
'on'
>>> word[42:]
''
```

Los strings de Python son inmutables:

```python
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

La función **len** regresa el tamaño de una lista:

```python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```


### 1.3 Programación estructurada


A continuación veremos sentencias de control como los condicionales y los bucles.

Antes de continuar repasemos la lógica booleana en Python y el concepto de indentación.

**Lógica booleana**
Algunas operaciones:

```python
>>> True and False
False
>>> True or False
True
>>> not False # Negación
True
>>> 'hola' in 'hola mundo' # Contención de substrings
True
>>> 1 > 0
True
>>> 1 > 0 and  0 == 0
True
```
Así como en C, cualquier valor en memoria diferente de 0 o con longitud mayor a cero es True:
```python
>>> bool(2)
True
>>> bool('h')
True
>>> bool(3.4)
True
>>> bool('') #Caracter vacío
False
>>> bool(0)
False
>>> bool(None) 
False
```
**Indentación**
La sangría es la forma en que Python agrupa las declaraciones. En el indicador interactivo, debe escribir una tabulación o espacio (s) para cada línea con sangría. En la práctica, prepararás entradas más complicadas para Python con un editor de texto; Todos los editores de texto decentes tienen una función de sangría automática. Cuando una declaración compuesta se ingresa de forma interactiva, debe ir seguida de una línea en blanco para indicar que se completó (ya que el analizador no puede adivinar cuándo has escrito la última línea). Ten en cuenta que cada línea dentro de un bloque básico debe tener la misma sangría.

En C la sangría era opcional, era lo mismo tener el siguiente código

```c
for(int i=0; i<10; i++){
printf("%d", i);
}
```
al siguiente
```c
for(int i=0; i<10; i++){
    printf("%d", i);
}
```

ya que C utiliza las llaves para definir lo que está adentro no es necesario que se utilize la indentación (sangría).

En Python se ocupa la identación en lugar de las llaves, como lo veremos en las siguientes sntencias

#### 1.3.1 Sentencia if

Probablemente la sentancia más conocida es **if**, por ejemplo:
```python
>>> x = int(input("Por favor ingresa un número: "))
Por favor ingresa un número: 42
>>> if x < 0:
...     x = 0
...     print('Negativo cambiado a cero')
... elif x == 0:
...     print('Cero')
... elif x == 1:
...     print('Uno')
... else:
...     print('Más')
...
Más
```

La palabra reservada **elif** es en otros lenguajes **else if**.
Pueden existir cero o muchos **elif**, y el **else** es opcional.

Como lo vimos antes en Python, como en C, cualquier valor entero distinto de cero es verdadero; cero es falso. La condición también puede ser una cadena o un valor de lista, de hecho, cualquier secuencia; cualquier cosa con una longitud distinta de cero es verdadera, las secuencias vacías son falsas. La prueba utilizada en el ejemplo es una comparación simple. Los operadores de comparación estándar se escriben igual que en C: <(menor que),> (mayor que), == (igual a), <= (menor o igual que), > = (mayor o igual que) y! = (no igual a).

Un bloque muy usado en programación es la asignación condicionada, por ejemplo:


```python
>>> edad = 18
>>> if edad < 18:
...    mayorEdad = False
... else:
...    mayorEdad = True
>>> mayorEdad
True
```
En Python se puede simplificar usando la asignación condicionada con la siguiente sintaxis:

```python
>>> edad = 18
>>> mayorEdad = True if edad < 18 else False
```

#### 1.3.2 Sentencia While

El bucle se terminará cuando a sea igual a 10. Observa que el contenido del bucle está indentado de igual manera:


```python
>>> a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8

```

Una situación muy común es recorrer una estructura en un bucle, por ejemplo:

```python
>>> frase = 'hola'
>>> i = 0
>>> while i < len(frase):
...     print(frase[i])
...     i+=1
...
"h"
"o"
"l"
"a"
```
Pero es mucho más eficiente hacerlo con un bucle for.

### 1.3.3 For
La instrucción for en Python difiere un poco de lo que puedes estar acostumbrado en C o Pascal. En lugar de iterar siempre sobre una progresión aritmética de números (como en Pascal), o darle al usuario la capacidad de definir tanto el paso de iteración como la condición de detención (como C), la declaración for de Python itera sobre los elementos de cualquier secuencia (una lista o una cadena), en el orden en que aparecen en la secuencia. Por ejemplo:

```python
>>> frase = 'hola'
>>> for letra in frase:
...    print(letra)
...
"h"
"o"
"l"
"a"
```

Da exactamente el mismo resultado que el ejemplo anterior de While.

Intenta correr el ejemplo anterior entrando a [este enlace](https://pythontutor.com/live.html#mode=edit).




## 1.4 Estructuras de datos

Python incluye varios tipos de datos compuestos, que se utilizan para agrupar otros valores. La más versátil es la lista, que se puede escribir como una lista de valores (elementos) separados por comas entre corchetes. Las listas pueden contener elementos de diferentes tipos, pero por lo general todos los elementos tienen el mismo tipo.

### 1.4.1 Listas

Sintáxis:

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]

```

Las listas se comportan muy parecido a los strings, es decir, se puede hacer indexación y slicing:


```python
>>> squares[0]  # indexación regresa un elemento
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing regresa una sublista
[9, 16, 25]
```
Todas las operaciones de slicing devuelven una nueva lista que contiene los elementos solicitados. Esto significa que el siguiente segmento devuelve una **copia superficial** de la lista:

```python
>>> cuadrados [:]
[1, 4, 9, 16, 25]
```

Las listas también admiten operaciones como la concatenación y el producto con enteros:

```python
>>> cuadrados + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> cuadrados * 2
[1, 4, 9, 16, 25, 1, 4, 9, 16, 25]

```
A diferencia de las cadenas, que son inmutables, las listas son de tipo mutable, es decir, es posible cambiar su contenido:

```python
>>> cubes = [1, 8, 27, 65, 125]  # Algo está mal aquí
>>> 4 ** 3  # el cube of 4 es 64, no 65
64
>>> cubes[3] = 64  # Se cambia el valor
>>> cubes
[1, 8, 27, 64, 125]

```
También puedes agregar nuevos elementos al final de la lista, utilizando el método **append** (veremos más sobre los métodos más adelante): 

```python
>>> cubes.append(216)  # Agregando el cubo de 6
>>> cubes.append(7 ** 3)  # y el cubo de 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]

```

La asignación a slices también es posible, y esto incluso puede cambiar el tamaño de la lista o borrarla por completo:

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```
Sustituyendo valores:

```python
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
```
Eliminando valores:
```python
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
```
Eliminando todos los valores:
```python
>>> letters[:] = []
>>> letters
[]
```
La función **len** también aplica a listas, en si a cualquier *objeto iterable*

```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

Existe algo conocido como listas paralalelas, un ejemplo común es relacionar una lista con nombres y otra lista con las edades, se dice que son paralelas porque la posición hace que se relacionen:

```python
>>> nombres = ["Juan", "Carlos", "Jorge"]
>>> edades = [18, 20, 34]
```
En este ejemplo Juan tiene 18 años, Carlos 20 y Jorge 34, es por eso que el orden de las listas está hecha tal que la primer posición haga referencia al mismo objeto.

```python
>>> f'{nombres[0]} tiene {edades[0]} años'
"Juan tiene 18 años"
```

#### 1.4.1.2 Recorrimiento de listas en un for

Utilizando el ejemplo anterior
```python
>>> nombres = ["Juan", "Carlos", "Jorge"]
>>> edades = [18, 20, 34]
```

Podemos iterar sobre una lista como lo hacíamos con un string:

```python
>>> for nombre in nombres:
...    print(nombre)
...
Juan 
Carlos 
Jorge 
```
Pero también se puede iterar en las dos listas al mismo tiempo con un for utilizando la función **zip**:
```python
>>> for nombre, edad in zip(nombres, edades):
...    print(f'{nombre} tiene {edad} años')
...
Juan tiene 18 años
Carlos tiene 20 años
Jorge tiene 34 años
```
### 1.4.2 Diccionarios
Otro tipo de datos útil integrado en Python es el diccionario.

Es mejor pensar en un diccionario como un conjunto de pares **llave: valor**, con el requisito de que las llaves sean **únicas** (dentro de un diccionario). Un par de llaves crea un diccionario vacío: {}. 
    
```python
>>> dict = {}
```


Al colocar una lista separada por comas de pares llave: valor entre llaves, se agregan pares llave: valor iniciales al diccionario; esta es también la forma en que se escriben los diccionarios en la salida.
    
```python
>>> dicc = {'Juan':18, 'Carlos':20, 'Jorge':34}
```
Para extraer elementos:

```python
>>> dicc['Juan']
18
```
Ejecutando list(d) en un diccionario retornará una lista con todas las claves usadas en el diccionario, en el orden de inserción. 

```python
>>> list(dicc) # Salida SIMILAR:
['Juan', 'Carlos', 'Jorge']
```

Para comprobar si una clave está en el diccionario usa la palabra clave in.

```python
>>> 'Juan' in dicc
True
>>> 'Pedro' in dicc
False
```
Al igual que las listas, los diccionarios son mutables, es decir, se pueden re-escribir y crear nuevas llaves:

```python
>>> dicc = {'Juan':18, 'Carlos':20, 'Jorge':34}
>>> dicc['Juan'] = 30
>>> dicc
{'Juan':30, 'Carlos':20, 'Jorge':34}
```
Observa que como Juan ya existe, se sobreescribió el dato.
Ahora crearemos una nueva llave:

```python

>>> dicc['José'] = 10
>>> dicc
{'Juan':20, 'Carlos':20, 'Jorge':34, 'José':10}

```

## 1.5 Técnicas de iteración

Cuando iteramos sobre diccionarios, se pueden obtener al mismo tiempo la clave y su valor correspondiente usando el método items().



```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for key, vvalue in knights.items():
...     print(key, value)
...
gallahad the pure
robin the brave

```
Cuando se itera sobre una secuencia, se puede obtener el índice de posición junto a su valor correspondiente usando la función enumerate().

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```
Como recordatorio, para iterar sobre dos o más secuencias al mismo tiempo, los valores pueden emparejarse con la función zip().

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

Si se necesita iterar sobre una secuencia de números, es apropiado utilizar la función integrada range(), la cual genera progresiones aritméticas:

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```
El valor final dado nunca es parte de la secuencia; range(10) genera 10 valores, los índices correspondientes para los ítems de una secuencia de longitud 10. Es posible hacer que el rango empiece con otro número, o especificar un incremento diferente (incluso negativo; algunas veces se lo llama “paso”):

```python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]
```


Para iterar sobre una secuencia en orden inverso, se especifica primero la secuencia al derecho y luego se llama a la función **reversed()**.

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1

```
Para iterar sobre una secuencia ordenada, se utiliza la función **sorted()** la cual retorna una nueva lista ordenada dejando a la original intacta.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```
El uso de **set()** en una secuencia elimina los elementos duplicados. El uso de **sorted()** en combinación con **set()** sobre una secuencia es una forma idiomática de recorrer elementos únicos de la secuencia en orden ordenado.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear

```


