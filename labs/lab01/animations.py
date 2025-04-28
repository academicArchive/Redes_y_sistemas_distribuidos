from manim import *

class AgregarPeliculaAnimation(Scene):
    def construct(self):
        # Texto del código
        codigo = """def agregar_pelicula():
    \"\"\"Añade una nueva película.\"\"\"
    datos = request.json
    if 'titulo' not in datos or 'genero' not in datos:
        return jsonify({'error': 'Faltan datos'}), 400
    nueva_pelicula = {
        'id': obtener_nuevo_id(),
        'titulo': request.json['titulo'],
        'genero': request.json['genero']
    }
    peliculas.append(nueva_pelicula)
    print(peliculas)
    return jsonify(nueva_pelicula), 201"""
        
        # Crear título
        titulo = Text("Función agregar_pelicula()", font_size=36, color=BLUE)
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        # Separar líneas del código
        lineas = codigo.split('\n')
        objetos_texto = VGroup()
        
        # Crear texto para cada línea
        for i, linea in enumerate(lineas):
            texto = Text(linea, font='Monospace', font_size=24)
            texto.shift(UP * (3 - i * 0.6))  # Posicionar líneas verticalmente
            objetos_texto.add(texto)
        
        # Colores para resaltado
        colores = [BLUE, YELLOW, GREEN, RED, ORANGE, PURPLE, PINK, TEAL, GOLD, MAROON, PINK]
        
        # Explicaciones para cada línea (asegúrate de que coincida con el número de líneas)
        explicaciones = [
            "Definir función para agregar películas",
            "Descripción del método con docstring",
            "Obtener datos de la solicitud JSON",
            "Validar campos obligatorios (título y género)",
            "Preparar respuesta de error si faltan datos",
            "Crear diccionario con detalles de la película",
            "Generar ID único para la película",
            "Obtener título de la solicitud",
            "Obtener género de la solicitud",
            "Agregar película a la lista de películas",
            "Imprimir lista actualizada de películas",
            "Retornar respuesta JSON con la nueva película"
        ]
        
        # Animación de escritura de líneas
        for i, texto in enumerate(objetos_texto):
            # Crear rectángulo de resaltado
            highlight = SurroundingRectangle(
                texto, 
                color=colores[i % len(colores)],
                buff=0.1,
                stroke_width=2,
                fill_opacity=0.2
            )
            
            # Crear explicación (asegurarse de no exceder el índice)
            explicacion = Text(
                explicaciones[i] if i < len(explicaciones) else "...", 
                font_size=24, 
                color=WHITE
            ).next_to(texto, DOWN)
            
            # Animaciones
            self.play(
                Write(texto),
                run_time=0.5
            )
            
            self.play(
                Create(highlight),
                Write(explicacion),
                run_time=0.5
            )
            
            self.wait(1)
            
            # Limpiar resaltado
            self.play(
                FadeOut(highlight),
                FadeOut(explicacion),
                run_time=0.3
            )
        
        # Animación final
        self.play(
            *[obj.animate.set_color_by_gradient(BLUE, GREEN) for obj in objetos_texto],
            run_time=2
        )
        
        self.wait(2)


from manim import *

class ObtenerNuevoIdAnimation(Scene):
    def construct(self):
        # Texto del código
        codigo = """id_disponible: list[int] = []
def obtener_nuevo_id():
    \"\"\"Genera un nuevo ID para una película.\"\"\"
    if len(peliculas) > 0:
        if len(id_disponible) > 0:
            return id_disponible.pop()
        else:
            ultimo_id = peliculas[-1]['id']
            return ultimo_id + 1
    else:
        return 1"""
        
        # Crear título
        titulo = Text("Función obtener_nuevo_id()", font_size=36, color=BLUE)
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        # Separar líneas del código
        lineas = codigo.split('\n')
        objetos_texto = VGroup()
        
        # Crear texto para cada línea
        for i, linea in enumerate(lineas):
            texto = Text(linea, font='Monospace', font_size=24)
            texto.shift(UP * (3 - i * 0.6))  # Posicionar líneas verticalmente
            objetos_texto.add(texto)
        
        # Colores para resaltado
        colores = [PURPLE, BLUE, YELLOW, GREEN, RED, ORANGE, PINK, TEAL, GOLD, MAROON]
        
        # Explicaciones para cada línea
        explicaciones = [
            "Declaración de lista para IDs disponibles",
            "Definición de función para generar nuevo ID",
            "Descripción del método con docstring",
            "Verificar si hay películas existentes",
            "Comprobar si hay IDs disponibles en la lista",
            "Reutilizar un ID disponible si existe",
            "Si no hay IDs disponibles",
            "Obtener el último ID de la lista de películas",
            "Incrementar el último ID en 1",
            "Si no hay películas, comenzar con ID 1"
        ]
        
        # Animación de escritura de líneas
        for i, texto in enumerate(objetos_texto):
            # Crear rectángulo de resaltado
            highlight = SurroundingRectangle(
                texto, 
                color=colores[i % len(colores)],
                buff=0.1,
                stroke_width=2,
                fill_opacity=0.2
            )
            
            # Crear explicación (asegurarse de no exceder el índice)
            explicacion = Text(
                explicaciones[i] if i < len(explicaciones) else "...", 
                font_size=24, 
                color=WHITE
            ).next_to(texto, DOWN)
            
            # Animaciones
            self.play(
                Write(texto),
                run_time=0.5
            )
            
            self.play(
                Create(highlight),
                Write(explicacion),
                run_time=0.5
            )
            
            self.wait(1)
            
            # Limpiar resaltado
            self.play(
                FadeOut(highlight),
                FadeOut(explicacion),
                run_time=0.3
            )
        
        # Diagrama de flujo para explicar la lógica
        self.create_flow_diagram()
        
        # Animación final
        self.play(
            *[obj.animate.set_color_by_gradient(BLUE, GREEN) for obj in objetos_texto],
            run_time=2
        )
        
        self.wait(2)
    
    def create_flow_diagram(self):
        # Crear un diagrama de flujo para explicar la lógica de obtener_nuevo_id()
        flow_title = Text("Lógica de obtener_nuevo_id()", font_size=30, color=BLUE)
        flow_title.to_edge(UP)
        
        # Crear nodos del diagrama de flujo
        peliculas_existe = Text("¿Hay películas?", font_size=24)
        ids_disponibles = Text("¿Hay IDs disponibles?", font_size=24)
        usar_id_disponible = Text("Usar ID de lista", font_size=24)
        incrementar_ultimo_id = Text("Incrementar último ID", font_size=24)
        id_inicial = Text("Iniciar con ID 1", font_size=24)
        
        # Posicionar nodos
        peliculas_existe.move_to(ORIGIN)
        ids_disponibles.move_to(RIGHT * 3)
        usar_id_disponible.move_to(RIGHT * 3 + DOWN * 2)
        incrementar_ultimo_id.move_to(RIGHT * 3 + DOWN * 4)
        id_inicial.move_to(LEFT * 3 + DOWN * 2)
        
        # Crear flechas
        arrow1 = Arrow(peliculas_existe.get_right(), ids_disponibles.get_left(), color=GREEN)
        arrow2 = Arrow(ids_disponibles.get_bottom(), usar_id_disponible.get_top(), color=GREEN)
        arrow3 = Arrow(ids_disponibles.get_bottom(), incrementar_ultimo_id.get_top(), color=RED)
        arrow4 = Arrow(peliculas_existe.get_left(), id_inicial.get_top(), color=RED)
        
        # Grupo de elementos
        flow_group = VGroup(
            flow_title, 
            peliculas_existe, ids_disponibles, 
            usar_id_disponible, incrementar_ultimo_id, id_inicial,
            arrow1, arrow2, arrow3, arrow4
        )
        
        # Animación del diagrama de flujo
        self.play(Write(flow_title))
        self.play(
            Write(peliculas_existe),
            run_time=0.5
        )
        self.wait(0.5)
        
        self.play(
            GrowArrow(arrow1),
            Write(ids_disponibles),
            run_time=0.5
        )
        self.wait(0.5)
        
        self.play(
            GrowArrow(arrow2),
            Write(usar_id_disponible),
            run_time=0.5
        )
        self.wait(0.5)
        
        self.play(
            GrowArrow(arrow3),
            Write(incrementar_ultimo_id),
            run_time=0.5
        )
        self.wait(0.5)
        
        self.play(
            GrowArrow(arrow4),
            Write(id_inicial),
            run_time=0.5
        )
        self.wait(1)
        
        # Limpiar diagrama
        self.play(FadeOut(flow_group))

from manim import *

class RecomendarPeliculaAnimation(Scene):
    def construct(self):
        # Texto del código
        codigo = """def recomendar_para_holiday(genero: str):
    \"\"\"Recomienda una película según el género para el próximo feriado.\"\"\"
    holiday = NextHoliday()
    holiday.fetch_holidays()
    nextholiday = holiday.holiday
    peli = pelicula_aleatoria_por_genero(genero)
    if isinstance(peli, tuple) and peli[1] == 404:
        return jsonify({'mensaje': 'No hay películas de ese género'}), 404
    peli = peli[0].json
    res = {
        'dia': str(day_of_week(
            nextholiday['dia'],
            nextholiday['mes'],
            holiday.year
        )) + ' ' + str(nextholiday['dia']),
        'mes': nextholiday['mes'],
        'motivo': str(nextholiday['motivo']),
        'pelicula': str(peli['titulo']),
        'genero': str(peli['genero'])
    }
    return jsonify(res), 200"""
        
        # Separar líneas del código
        lineas = codigo.split('\n')
        objetos_texto = VGroup()
        
        # Crear texto para cada línea
        for i, linea in enumerate(lineas):
            texto = Text(linea, font='Monospace', font_size=24)
            texto.shift(UP * (3 - i * 0.6))  # Posicionar líneas verticalmente
            objetos_texto.add(texto)
        
        # Colores para resaltado
        colores = [BLUE, RED, GREEN, YELLOW, ORANGE]
        
        # Líneas a resaltar (0-based index)
        lineas_a_resaltar = [0, 5, 2, 3, 4]
        
        # Animación de escritura de líneas
        for i, texto in enumerate(objetos_texto):
            if i in lineas_a_resaltar:
                # Crear rectángulo de resaltado
                highlight = SurroundingRectangle(
                    texto, 
                    color=colores[lineas_a_resaltar.index(i)],
                    buff=0.1,
                    stroke_width=2,
                    fill_opacity=0.2
                )
                
                # Animaciones
                self.play(
                    Write(texto),
                    run_time=0.5
                )
                
                self.play(
                    Create(highlight),
                    run_time=0.5
                )
                
                self.wait(1)
                
                # Limpiar resaltado
                self.play(
                    FadeOut(highlight),
                    run_time=0.3
                )
            else:
                # Escribir líneas sin resaltar
                self.play(
                    Write(texto),
                    run_time=0.5
                )
        
        # Animación final
        self.play(
            *[obj.animate.set_color_by_gradient(BLUE, GREEN) for obj in objetos_texto],
            run_time=2
        )
        
        self.wait(2)