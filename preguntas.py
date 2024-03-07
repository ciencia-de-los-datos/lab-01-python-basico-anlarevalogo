"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv", 'r') as file:
        sum_col = 0
    
        for line in file:
            elements = line.strip().split('\t')
            sum_col += int(elements[1])

pregunta_01()



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv", 'r') as file:
        count_by_letter = {}
        
        for line in file:
            elements = line.strip().split('\t')
            first_letter = elements[0]
            if first_letter in count_by_letter:
                count_by_letter[first_letter] += 1
            else:
                count_by_letter[first_letter] = 1

    sorted_counts = sorted(count_by_letter.items())
    return sorted_counts

pregunta_02()

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv", 'r') as file:
        sum_by_letter = {}
        for line in file:
            elements = line.strip().split('\t')
            first_letter = elements[0]
            second_column_value = int(elements[1])
            
            if first_letter in sum_by_letter:
                sum_by_letter[first_letter] += second_column_value
            else:
                sum_by_letter[first_letter] = second_column_value

    sorted_sums = sorted(sum_by_letter.items())

    return sorted_sums

pregunta_03()

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", 'r') as file:
        count_by_month = {}
        
        for line in file:
            elements = line.strip().split('\t')
            
            date = elements[2]
            month = date.split('-')[1]

            if month in count_by_month:
                count_by_month[month] += 1
            else:
                count_by_month[month] = 1

    count_by_month = sorted(count_by_month.items())

    return count_by_month

pregunta_04()

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", 'r') as file:
        max_min_values = {}
        
        for line in file:
            elements = line.strip().split('\t')
            
            letter = elements[0]
            column_2_value = int(elements[1])
            
            if letter in max_min_values:
                current_max, current_min = max_min_values[letter]
                max_min_values[letter] = (max(current_max, column_2_value), min(current_min, column_2_value))
            else:
                max_min_values[letter] = (column_2_value, column_2_value)

    result_list = sorted(max_min_values.items())
    result_list = [(key, value[0], value[1]) for key, value in result_list]

    return result_list

pregunta_05()


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv", 'r') as file:
        min_max_values = {}

        for line in file:
            elements = line.strip().split('\t')
            dictionary_string = elements[4]
            pairs = dictionary_string.split(',')

            for pair in pairs:
                key, value = pair.split(':')
                if key in min_max_values:
                    current_min, current_max = min_max_values[key]
                    min_max_values[key] = (min(current_min, int(value)), max(current_max, int(value)))
                else:
                    min_max_values[key] = (int(value), int(value))

    result_list = sorted(min_max_values.items())
    result_list = [(key, min_max[0], min_max[1]) for key, min_max in result_list]

    return result_list

pregunta_06()

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", 'r') as file:
        values_associated = {}

        for line in file:
            elements = line.strip().split('\t')
            
            value_col2 = int(elements[1])
            letter_col1 = elements[0]
            
            if value_col2 in values_associated:
                values_associated[value_col2].append(letter_col1)
            else:
                values_associated[value_col2] = [letter_col1]

    result_list = sorted([(value, letters) for value, letters in values_associated.items()])
    return result_list

pregunta_07()


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", 'r') as file:
        values_associated = {}

        for line in file:
            elements = line.strip().split('\t')
            
            value_col2 = int(elements[1])
            letter_col1 = elements[0]
            
            if value_col2 in values_associated:
                values_associated[value_col2].append(letter_col1)
            else:
                values_associated[value_col2] = [letter_col1]
    
    result_list = sorted([(value, sorted(set(letters))) for value, letters in values_associated.items()])
    return result_list

pregunta_08()


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    clave_count = {}

    with open("data.csv", 'r') as file:
        for line in file:
            elements = line.strip().split('\t')
            column_5 = elements[4]
            pairs = column_5.split(',')
            for pair in pairs:
                key, _ = pair.split(':')
                if key in clave_count:
                    clave_count[key] += 1
                else:
                    clave_count[key] = 1
    
    clave_count = dict(sorted(clave_count.items()))
    return clave_count

pregunta_09()

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    tuplas_resultantes = []
    with open("data.csv", 'r') as file:
        for line in file:
            elements = line.strip().split('\t')
            
            letra_columna_1 = elements[0]
            elementos_columna_4 = len(elements[3].split(','))
            elementos_columna_5 = len(elements[4].split(','))

            tuplas_resultantes.append((letra_columna_1, elementos_columna_4, elementos_columna_5))
    #tuplas_resultantes = sorted(tuplas_resultantes)
    return tuplas_resultantes

pregunta_10()


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    sum_columna_2 = {}

    with open("data.csv", 'r') as file:
        for line in file:
            elements = line.strip().split('\t')
            
            letras_columna_4 = elements[3].split(',')
            valor_columna_2 = int(elements[1])

            for letra in letras_columna_4:
                if letra in sum_columna_2:
                    sum_columna_2[letra] += valor_columna_2
                else:
                    sum_columna_2[letra] = valor_columna_2

    sum_columna_2 = dict(sorted(sum_columna_2.items()))
    return sum_columna_2

pregunta_11()


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_columna_5 = {}
    with open("data.csv", 'r') as file:
        for line in file:
            elements = line.strip().split('\t')
            
            letra_columna_1 = elements[0]
            valores_columna_5 = elements[4].split(',')
            
            suma_valores_columna_5 = sum(int(valor.split(':')[1]) for valor in valores_columna_5)
            
            if letra_columna_1 in suma_columna_5:
                suma_columna_5[letra_columna_1] += suma_valores_columna_5
            else:
                suma_columna_5[letra_columna_1] = suma_valores_columna_5
    
    suma_columna_5 = dict(sorted(suma_columna_5.items()))
    return suma_columna_5

pregunta_12()