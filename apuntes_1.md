### Apuntes de la Primera Clase de Programación desde el Final

#### Introducción
En nuestra primera clase, dimos los primeros pasos en el mundo de la programación utilizando Streamlit, una herramienta amigable para crear aplicaciones web interactivas con Python de manera sencilla. Nuestro primer programa fue tan simple como escribir "Hola inmundo!" en la interfaz de Streamlit, pero ofreció una excelente oportunidad para introducir conceptos clave de la programación y poner en contexto su importancia.

---

### Marco Histórico y Conceptual

#### 1. Primeros Programas de Computadoras
- El "Hola mundo!" es uno de los programas más emblemáticos en la historia de la programación. Su objetivo es enseñar los conceptos básicos de la sintaxis de un lenguaje de programación.
- El uso del "Hola mundo!" se popularizó con el libro "The C Programming Language" por Brian Kernighan y Dennis Ritchie, los creadores del lenguaje C a finales de los años 70.

#### 2. ¿Qué es un Programa?
- Un **programa** es una secuencia de instrucciones escritas en un lenguaje de programación que una computadora puede ejecutar. Estas instrucciones le dicen a la computadora **qué** hacer y **cómo** hacerlo.
- En Python, un programa puede ser tan simple como imprimir un texto en pantalla o tan complejo como controlar un sistema operativo.

#### 3. ¿Qué es un Dato?
- Un **dato** es cualquier valor que un programa puede manipular. Los datos pueden ser números, texto, imágenes, etc.
- En nuestro primer programa, el dato que estamos manejando es una cadena de texto que contiene "Hola inmundo!".

#### 4. Descripción Técnica del Primer Programa con Streamlit
- **`import streamlit as st`:** Este comando importa la biblioteca Streamlit y le asigna el nombre `st`.
- **`st.write("Hola inmundo!")`:** Este comando utiliza la función `st.write` de Streamlit para mostrar la cadena "Hola inmundo!" en la interfaz de la aplicación web.
  - **a. `st`:** Referencia a la biblioteca Streamlit previamente importada.
  - **b. `write`:** Es una función de Streamlit diseñada para mostrar texto y otros elementos en pantalla.
  - **c. `"Hola inmundo!"`:** Es el dato de tipo cadena de texto que queremos desplegar.

---

### Historia del Lenguaje Python en el Contexto de los Lenguajes de Programación

La programación de computadoras ha evolucionado significativamente desde sus inicios en la década de 1940. Aquí tienes un breve recorrido:

- **Década de 1940-1950**: Se desarrollaron las primeras computadoras electrónicas. Los primeros lenguajes eran extremadamente básicos y muy difíciles de usar, como el lenguaje de máquina que consiste en secuencias de ceros y unos.
- **1957**: Fortran fue uno de los primeros lenguajes de alto nivel desarrollados, permitiendo a los ingenieros escribir código en una forma más legible.
- **1970s-1980s**: Lenguajes como C y Pascal hicieron posible escribir programas más complejos de manera más estructurada.
- **1989**: Guido van Rossum, un programador holandés, comenzó a desarrollar Python con el objetivo de que sea un lenguaje fácil de leer y aprender, pero potente y flexible.

Python se ha convertido en uno de los lenguajes más populares debido a su simplicidad y versatilidad, ideal para principiantes y expertos.

**Lenguajes de Programación de Bajo Nivel vs Alto Nivel:**
- **Bajo Nivel:**
  - Lenguajes como Assembler y C son ejemplos de lenguajes de bajo nivel. Estos están más cerca del lenguaje máquina y permiten un control más directo del hardware.
  - Son más difíciles de leer y escribir, pero proporcionan un alto rendimiento y control sobre los recursos del sistema.
  
- **Alto Nivel:**
  - Python, Java, y JavaScript son ejemplos de lenguajes de alto nivel. Están diseñados para ser fáciles de leer y escribir.
  - Estos lenguajes son más abstractos y se encargan de muchas tareas complejas por debajo, lo que permite a los desarrolladores centrarse en resolver problemas a nivel de lógica de negocio.
  
**Ventajas del Lenguaje Python:**
- **Simplicidad y Legibilidad:** Python tiene una sintaxis clara y concisa, lo que lo hace adecuado para principiantes y permite escribir y mantener código de manera eficiente.
- **Productividad:** Gracias a su sintaxis sencilla y una vasta biblioteca estándar, los desarrolladores pueden realizar tareas complejas con menos líneas de código.
- **Portabilidad:** Python es un lenguaje multiplataforma, lo que significa que el código escrito en Python puede ejecutarse en casi cualquier sistema operativo con pocas o ninguna modificación.
- **Versatilidad:** Se usa en diversos campos como desarrollo web, ciencia de datos, inteligencia artificial, automatización, y más.

---

### Comparación con Otros Lenguajes de Programación

**Python vs Lenguajes de Bajo Nivel (como C):**
- **Sintaxis y Abstracción:** Python proporciona una mayor abstracción y una sintaxis más simple y legible en comparación con C. C permite manipulación directa de memoria, lo que puede ser crucial en aplicaciones que requieren un rendimiento muy alto.
- **Uso:** C es muy utilizado en sistemas embebidos y aplicaciones que requieren un control muy fino y optimización del hardware, mientras que Python se usa en un mayor espectro de aplicaciones debido a su simplicidad y versatilidad.

**Python vs Otros Lenguajes de Alto Nivel:**
- **Python vs Java:** Python es más simple y tiene una curva de aprendizaje más baja en comparación con Java, que es más verborrágico y estricto. Java, sin embargo, sobresale en aplicaciones empresariales y en el desarrollo de sistemas Android.
- **Python vs JavaScript:** Aunque ambos lenguajes son fáciles de aprender y utilizar, Python se destaca más en ciencia de datos y automatización, mientras que JavaScript es fundamental para el desarrollo web y aplicaciones frontend con frameworks como React y Angular.

---

### Ejecutando y Terminando el Programa

Para volver a ejecutar nuestro primer programa en Streamlit en tu máquina, sigue los siguientes pasos:

1. **Abre tu Command Prompt:**
   - Presiona `Win + R`, escribe `cmd` en el cuadro de diálogo y presiona `Enter`.

2. **Navega a la Carpeta del Proyecto:**
   - Usa el comando `cd` seguido de la ruta a tu carpeta del proyecto. En este caso, la ruta es `\Users\maria\Documents`. Escribe el siguiente comando y presiona `Enter`:
     ```cmd
     cd \Users\maria\Documents
     ```

3. **Ejecuta el Programa:**
   - Una vez que estés en la carpeta correcta, ejecuta el siguiente comando:
     ```cmd
     streamlit run hola.py
     ```
     Aquí `hola.py` es el nombre del archivo que contiene tu programa de Streamlit.

4. **Ver la Aplicación:**
   - Después de ejecutar el comando `streamlit run hola.py`, Streamlit creará un servidor web local. Un servidor web es un programa que provee contenido web, como páginas HTML, imágenes, etc., a través de la red.
   - Streamlit abrirá automáticamente una nueva pestaña en tu navegador web por defecto mostrando la aplicación Streamlit con el mensaje "Hola mundo!".
   - La URL que Streamlit abre generalmente tiene el formato `http://localhost:8501`. `localhost` es un nombre de dominio que significa "esta computadora", y `8501` es el puerto en el que el servidor está escuchando.

5. **Terminar la Ejecución del Programa:**
   - Para detener la ejecución de tu programa en el Command Prompt donde ejecutaste `streamlit run hola.py`, simplemente presiona `Ctrl + C`. Esto enviará una señal de interrupción que detendrá el servidor de Streamlit y cerrará tu aplicación web.

---

### Conclusión

En esta primera clase, has dado tus primeros pasos en el mundo de la programación. A medida que avancemos, veremos cómo estos conceptos básicos se aplican en la creación de programas más complejos y útiles. Si sientes emoción y curiosidad, estás en el camino correcto.

Para la próxima clase, prepararemos un entorno de desarrollo en tu computadora y veremos cómo se pueden manipular diferentes tipos de datos. Si tienes alguna pregunta o algo no quedó claro, no dudes en mencionarlo en nuestro próximo encuentro.

¡Bien hecho, Mane! Este es el inicio de un viaje fascinante en el mundo de la programación.
