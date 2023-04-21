---
title: "Metodos Computacionales 2023"
subtitle: "Trabajo Práctico Regresión Lineal Múltiple"
author: "Bonás Valentín y De Fino Lucas"
description: "Trabajo Práctico Metodos Computacionales"
institute: "UTDT"
date: "21/04/2023"
---

### Ideas Generales con respecto al trabajo

<br>

Nuestro objetivo en este trabajo práctico es estudiar el comportamiento de una variable dependiente en relación al un conjunto de variables explicativas para lo cual recurrimos a un modelo de Regresión Lineal Múltiple, en el proceso de plantear este modelo debemos encontrar la fórmula para la solución óptima de $\beta^\ast$ (formula para el coeficiente general de las variables explicativas)

<br>

### Primera parte. El objetivo de esta sección es deducir una fórmula para la solución óptima $\beta^\ast$ siguiendo los pasos a continuación:

<br>

- a) Mostrar que el espacio columna de la matriz $X$ es un subespacio vectorial de $R^n$: $Col(X)$ = {b en $R^n$ tales que $b=X\beta$ con $\beta$ variando en $R^p$}

    - Para probar que el espacio columna de la matriz $X$ es un subespacio vectorial de $R^n$ debemos ver que:

      - El vector cero pertenece a $Col(X)$

        - Esto es verdadero pues podemos notar que si uno reemplaza $\beta$ por cero ( **0** $\in R^p$), la ecuación resultado será $X0 = b = 0$. Esto podría pasar en una hipotética situación en donde mi ecuación resultado quedaría de la siguiente manera.

        $$y = x_10 + x_20 + ... + x_n0 = 0$$

      - Para cada **u** y **v** en $Col(X)$, la suma **u** $+$ **v** está en $Col(X)$

        - Siendo $u=X\beta_u$ y $v=X\beta_v$ , vemos que $u+v = X\beta_u + X\beta_v = X(\beta_u + \beta_v)$ y como sabemos que $\beta \in R^p$ afirmamos que $\beta_u + \beta_v = \beta_{u+v} \in R^p$.

        - Por lo tanto $u+v = X\beta_{u+v}$ seguro está en $Col(X)$

      - Para cada **u** en $Col(X)$ y cada escalar $c$, el vector $c$**u** está en $Col(X)$

        - Siendo $cu=cX\beta_u$ puedo afirmar que, como $\beta \in R^p$, $c\beta \in R^p$.
        
        - Por lo tanto $cX\beta_u = cu \in Col(X)$

<br>

- b) Supongamos que cuando hablamos de vectores en $R^n$ nos referimos a vectores columna de $R^{nx1}$. Mostrar en ese caso que el producto escalar entre dos vectores u, v en Rn puede calcularse como: $u \cdot v = v^Tu$ donde operación en el lado derecho de la igualdad es el producto de matrices usual.

    - Sabiendo que el producto escalar entre dos vectores $u,v$ es:

    $$u \cdot v = \sum_{i=1}^{n} u_iv_i = u_1v_1 + u_2v_2 + ... + u_nv_n$$
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    Y sabiendo que la multiplicacion $v^Tu$ es:

    $$\begin{bmatrix}v_1 & v_2 & ... & v_n\end{bmatrix} \begin{bmatrix}u_1 \\ u_2 \\ ... \\ u_n\end{bmatrix} = u_1v_1 + u_2v_2 + ... + u_nv_n$$
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    Gracias a esto podemos ver ambos lados de la ecuacion concluyen en el mismo resultado.

<br>

- c) Aplicando el teorema tomando como subespacio $S$ el subespacio del ítem (a), el punto $y$ de $R^n$ como el vector de la variable dependiente, y el vector $b$ como $b=X\beta^\ast$, convertir esta ecuación de optimalidad:

  $$||y-X\beta^\ast|| = \max_{\beta \in R^p} ||y-X\beta||$$

  en la condición de ortogonalidad que corresponde a la equivalencia 2 del teorema.

    - Segun lo establecido en el ítem (a) podemos decir que como el subespacio S es igual a Col(X) podemos entender todo valor s $\in$ S como $X\beta = s$

    - Además, por enunciado podemos decir que $X\beta^\ast = b$

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    Por lo tanto, la ecuación luego de los reemplazos termina siendo la siguiente:

  $$||y-b|| = \max_{s \in S} ||y-s||$$

    Esta ecuacion corresponde a la equivalencia 1 del teorema, demostrando que la misma se cumple para estos parametros. Como llegamos a ver que esta parte del teorema se cumple, podemos afirmar que la equivalencia 2 del mismo teorema también se cumple.

<br>

- d) A la ecuación obtenida en el ítem (c), aplicarle la identidad del producto escalar vista en el item (b), para llegar a la ecuación:

  $$X^T(y - X\beta^\ast)\cdot \beta = 0$$


  - La ecuacion obtenida en el item (c) es la siguiente:
    
  $$(y-b) \cdot s = 0 \; \forall \; s \in S$$

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  que es igual a, por lo visto en el item (c):

  $$(y-X\beta^\ast) \cdot X\beta = 0$$

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  y al aplicarle la identidad del producto escalar, se trasnforma en:

  $$X^T \cdot (y-X\beta^\ast) \cdot \beta = 0$$

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  que es lo que queriamos.

<br>

- e) Se sabe que el único vector que es ortogonal a todo vector $v$ de $R^n$ es el vector nulo. Es decir, si $u$ es un vector fijo tal que $u\cdot v = 0$ para todo $v$ en $R^n$, entonces $u = 0$. Usando esto y la ecuación obtenida en el ítem (d), llegar a la fórmula: $X^TX\beta^\ast$ $=$ $X^Ty$

    - La ecuacion obtenida en el item (d) es la siguiente:
    
  $$X^T \cdot (y-X\beta^\ast) \cdot \beta = 0$$

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Como sabemos que $\beta$ es un vector en $R^n$ podemos afirmar por la propiedad de la consigna que:

  $$X^T \cdot (y-X\beta^\ast) = 0$$

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  De esta ecuacion podemos simplemente distribuir la multiplicación de la matriz $X^T$, reordenar los termino y llegar a la ecuación objetivo:

  $$ X^TX\beta^\ast = X^Ty $$

<br>

- f) Finalmente, suponiendo que las columnas de $X$ son linealmente independientes, se tiene que la matriz $X^TX$ es invertible. Despejar $\beta^\ast$ de la ecuación del ítem (e) para llegar a la fórmula de la solución óptima al problema de regresión.

  - La ecuacion obtenida en el item (e) es la siguiente:
    
  $$ X^TX\beta^\ast = X^Ty $$

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Gracias a que $X^TX$ es invertible podemos transformarla en:

  $$ \beta^\ast = (X^TX)^{-1} \cdot X^Ty  $$

  Que es la formula de la solución óptima al problema de regresión.

<br>

### Segunda parte. En esta sección la idea es realizar regresión lineal en $R^2$ y analizar como se comportan las soluciones obtenidas.

<br>

1. Usando los datos del archivo ejercicio_1.csv:
    
    - a) Graficar todos los puntos en el plano xy. 
    <center>
     <img src='imagen1.png' border="5px" ></img> 

    En el gráfico podemos ver todas las observaciones de nuestra muestra. Se puede notar una posible relación lineal entre ambas variables.

    </center>

    - b) Utilizando los conceptos teóricos desarrollados en la primera parte, hallar la recta que mejor aproxima a los datos.
    
    <img src='imagen2.png'></img>

    La recta que mejor aproxima a mis datos será $y = X\hat{\beta}$, como $\hat{\beta}$ está en $R^1$ mi recta quedará de la siguiente manera $y = x\hat{\beta_1}$ siendo $\hat{\beta_1}$ la estimación del coeficiente de la primera variable independiente.

    - c) Realizar nuevamente los incisos (a) y (b) pero considerando los puntos {$(x_i, y_i + 12)$ con $i=1\dots n$} donde $(x_i, y_i)$ eran los puntos originales. ¿Es buena la aproximación realizada?, ¿cuál es el problema?

      - Esta aproximacion no es buena. El problema con esta es que cuando se hace este tipo de regresion, no se esta teniendo el cuenta la ordenada al origen. Como todos los puntos aumentan en 12 unidades en la cordenanda Y, la ordenada al origen tambien aumenta en 12. En nuestra modelo de regresión no tenemos ningun parametro para la ordenada al origen.

    - d) ¿Cómo se podría extender el modelo para poder aproximar cualquier recta en el plano?

      - Esto se podria solucionar agregando un $\beta_0$ que sea la ordenada al origen para poder estabilizar el gráfico.

      <br>

      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      Para calcular $\beta_0$ agregamos una columna de unos adelante de la matriz $X$. Agregamos una columna de unos para que cuando hagamos $X\beta$ $\Rightarrow$
      $$\begin{bmatrix}\beta_0 + \beta_1x_{11} + ... + \beta_px_{1p} \\ \beta_0 + \beta_1x_{21} + ... + \beta_px_{2p} \\ ... \\ \beta_0 + \beta_1x_{n1} + ... + \beta_px_{np}\end{bmatrix}$$

      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      En este caso solo tendriamos $\beta_0$ y $\beta_1$:

      $$\begin{bmatrix}\beta_0 + \beta_1x_{11} \\ \beta_0 + \beta_1x_{21} \\ ... \\ \beta_0 + \beta_1x_{n1}\end{bmatrix}$$

<br>

2. Usando los datos del archivo ejercicio_2.csv:

    - a) Graficar y aproximar los puntos con una recta.
    
    <img src='imagen3.png'></img>

    En el gráfico podemos ver todas las observaciones de nuestra muestra. Se puede notar una relacion lineal negativa entre ambas variables.

    - b) Imaginemos que los datos forman parte de mediciones de algún tipo, como por ejemplo la temperatura de un procesador a lo largo del tiempo, y queremos predecir cuál va a ser la temperatura en el futuro. ¿Es buena la aproximación que realizamos?, ¿cuál fue el problema en este caso?

      - Si agarramos un valor de $x$ muy elevado, generaria un valor de $y$ muy bajo. Si por ejemplo, se estuviese midiendo la temperatura, un valor muy grande en los numeros negativos no tendria sentido, por lo tanto, podríamos decir que nuestro modelo de regresión solamente funciona para parametrso relativamente chicos. Ese punto con un $x$ muy grande seria un Outlier.


