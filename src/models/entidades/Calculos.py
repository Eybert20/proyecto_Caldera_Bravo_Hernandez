class Calculos:
    def __init__(self, id, proyecto_id, formula_id, resultado, parametros) -> None:
        self.id = id
        self.proyecto_id = proyecto_id
        self.formula_id = formula_id
        self.resultado = resultado
        self.parametros = parametros
        
    
    def to_dict(self):
        return {
            'id': self.id,
            'proyecto_id': self.proyecto_id,
            'formula_id': self.formula_id,
            'resultado': self.resultado,
            'parametros': self.parametros
    }
    @classmethod
    def evaluar_formula(self, formula, valores):

    # Paso 3: Convertir los valores a una lista de números
       valores = list(map(float, valores.split(',')))

    # Paso 4: Crear un diccionario con los valores para las variables (a, b, etc.)
       variables = {}
       for i, var in enumerate('abcdefghijklmnopqrstuvwxyz'):
          if var in formula:
             variables[var] = valores[i]

    # Paso 5: Reemplazar las letras en la fórmula por sus valores
       for var, valor in variables.items():
          formula = formula.replace(var, str(valor))

    # Paso 6: Evaluar la fórmula usando eval
       resultado = eval(formula)

       return resultado
        