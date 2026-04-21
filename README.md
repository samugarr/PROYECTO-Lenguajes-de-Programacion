# PROYECTO - Lenguajes de Programación | Intérprete Java Reducido

## Cosas que se pueden hacer

### Declaración de variables

**Sintaxis:**
```text
<tipo> <id> = <asignación> ;
```

**Ejemplo:**
```java
int x = 5;
```

### Display de información por consola

**Sintaxis:**
```text
<print>(<variable>);
```

**Ejemplos:**
```java
print(x);
print(10);
```

### Comentarios

#### Comentarios de una línea

```java
// <comentario>
// Esto es un ejemplo de comentario
```

#### Comentarios multilínea

**Sintaxis:**
```java
//* <comentario_multilinea> *//
```

**Ejemplo:**
```java
//* 
// Esto es un comentario multilínea
//*
```

También pueden contener instrucciones que serán ignoradas por el intérprete:

```java
//* <declaración_de_variable/print> *//
```

**Ejemplo:**
```java
//* 
// int x = 8
// print(x)
//*
```

---

## Cosas que NO se pueden hacer

### Declaración de variables con operaciones

No se permite realizar operaciones en la asignación.

**Sintaxis:**
```text
<tipo> <id> = <operación> ;
```

**Ejemplos NO válidos:**
```java
int x = 2 + 4;
int x = x + y;
int x = y + z;
```

### Declaración sin asignación

No se permite declarar variables sin inicializarlas.

**Sintaxis:**
```text
<tipo> <id> ;
```

**Ejemplo NO válido:**
```java
int z;
```

### Comentarios multilínea mal cerrados

**Ejemplo NO válido:**
```java
//* 
// <declaración_de_variable> 
*//
```
