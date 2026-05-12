# PROYECTO — Intérprete Java Reducido

Intérprete de un subconjunto de Java implementado en Python con sly. Procesa ficheros `.txt` con código Java simplificado: declara variables enteras, realiza operaciones aritméticas, evalúa condiciones y muestra resultados por consola.

---

### Cómo se relacionan los módulos

```
fichero.txt
 lexer.py          Convierte el texto en tokens (palabras del lenguaje)
 parser.py         Construye el AST (árbol sintáctico abstracto)
 interprete.py     Recorre el AST y ejecuta cada nodo
 salida por consola
```
---

## Cómo ejecutar

### Ejecución básica

```bash
python main.py <fichero.txt>
```

### Ejecución mostrando el árbol AST

```bash
python main.py <fichero.txt> --ast
```

### Ejemplos con los ficheros de prueba

```bash
python main.py test_basico.txt
python main.py test_basico.txt --ast

python main.py test_negativos.txt
python main.py test_negativos.txt --ast

python main.py test_condicionales.txt
python main.py test_condicionales.txt --ast

python main.py test_operaciones.txt
python main.py test_operaciones.txt --ast

python main.py test_comentarios.txt
python main.py test_complejo.txt
```

### Ejecutar todos los tests seguidos

---

## Sintaxis del lenguaje

### Declaración de variables

Solo se admite el tipo `int`. Toda variable debe declararse con valor inicial.

```java
int x = 5;
int resultado = x * 2;
int negativo = -3;
```

### Reasignación

Una vez declarada, la variable puede reasignarse sin indicar el tipo.

```java
x = 10;
x = x + 1;
```

### Operaciones aritméticas

| Operador | Descripción         |
|----------|---------------------|
| `+`      | Suma                |
| `-`      | Resta               |
| `*`      | Multiplicación      |
| `/`      | División entera     |
| `-expr`  | Negación unaria     |

Se respeta la precedencia estándar. Se pueden usar paréntesis.

```java
int a = (3 + 2) * -4;
int b = 10 / 3;        // resultado: 3 (división entera)
```

### Print

Imprime por consola el valor de una expresión.

```java
print(x);
print(x + 1);
print(-x);
```

### Condicionales

Se admite `if` con o sin `else`. La condición debe ir entre paréntesis y el cuerpo entre llaves.

```java
if (x > 0) {
    print(x);
}

if (x == y) {
    print(1);
} else {
    print(0);
}
```

#### Operadores de comparación

| Operador | Significado       |
|----------|-------------------|
| `==`     | Igual             |
| `!=`     | Distinto          |
| `<`      | Menor que         |
| `>`      | Mayor que         |
| `<=`     | Menor o igual     |
| `>=`     | Mayor o igual     |

### Comentarios

**Una línea:**
```java
// Esto es un comentario
```

**Multilínea:**
```java
/*
   Esto es un comentario
   que ocupa varias líneas
*/
```

El contenido de los comentarios es completamente ignorado por el intérprete.

---

## Limitaciones conocidas

- **Solo entero:** 
- **No hay bucles**
- **No hay funciones**
- **If sin llaves no válido** `if (x > 0) print(x);` no es sintaxis válida.
- **Variable no declarada no da error** si se usa una variable que no existe, el intérprete devuelve `0`.
- **Declaración sin valor inicial no válida** 

