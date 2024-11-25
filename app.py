from flask import Flask, render_template, request, flash, redirect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
import pymysql

from src.models.modelUser import ModelUser
from src.models.Modelformula import  ModelFormula
from src.models.ModelCategorias import ModelCategorias
from src.models.ModelProyectos import ModelProyectos
from src.models.ModelCalculos import ModelCalculos

from src.models.entidades.User import User
from src.models.entidades.Formula import Formula
from src.models.entidades.Categoria import Categoria
from src.models.entidades.Proyecto import Proyecto
from src.models.entidades.Calculos import Calculos

app = Flask(__name__)

db = pymysql.connect(host='localhost', user='root', password='', db ='gestion_construccion')

# configuracion de manejador de sesiones
login_manager_app = LoginManager(app)

# funcion para tener datos del usuario logueado
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_user_by_id(db, int(id))

@app.route('/')
def index():
    return 'biemdvenidos a mi sitio web'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(None, None, request.form.get('email'), request.form.get('password'), None)
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect('/home')
            else:
                flash('contraseña incorrecta')
                return render_template('auth/login.html')
        else:
            flash('el usuario no existe')
            return render_template('auth/login.html')   
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

@app.route('/home')
@login_required
def home():
    return render_template('web/home.html')


# Rutas de Formulas 

@app.route('/formula')
@login_required
def  Formula_index():
    formula_list = ModelFormula.get(db)
    return render_template('admin/formula/index.html' , formula_list = formula_list)
  

@app.route('/formula/create', methods=['GET', 'POST'])
@login_required
def Formula_create():
    return render_template('admin/formula/create.html')


@app.route('/formula/store', methods=['GET', 'POST'])
@login_required
def Formula_store():
    if request.method == 'POST':
        formula = Formula(None, request.form.get('nombre'), request.form.get('descripcion'), request.form.get('expresion'))
        formula_creada = ModelFormula.store(db, formula.to_dict())
        if formula_creada:
            flash('formula creada')
            return redirect('/formula')
        else:
            flash('error al crear la formula')
            return redirect('/formula')

@app.route('/formula/destroy/<id>')
@login_required
def Formula_destroy(id):   
        formula_ELIMINADA = ModelFormula.destroy(db, id)
        if formula_ELIMINADA:
            flash('formula Eliminada Exitosamente')
            return redirect('/formula')
        else:
            flash('error al eliminar la formula')
            return redirect('/formula')

# Fin de  Rutas de Formulas




#Rutas de Categorias
@app.route('/categorias')
@login_required
def categorias_index():
    categorias_list = ModelCategorias.get(db)
    return render_template('admin/categorias/index.html' , categorias_list = categorias_list)
  

@app.route('/categorias/create', methods=['GET', 'POST'])
@login_required
def categorias_create():
    return render_template('admin/categorias/create.html')


@app.route('/categorias/store', methods=['GET', 'POST'])
@login_required
def categorias_store():
    if request.method == 'POST':
        categoria = Categoria(None, request.form.get('nombre'), request.form.get('descripcion'))
        categoria_creada = ModelCategorias.store(db, categoria.to_dict())
        if categoria_creada:
            flash('categoria creada')
            return redirect('/categorias')
        else:
            flash('error al crear la categoria')
            return redirect('/categorias')

@app.route('/categorias/destroy/<id>')
@login_required
def categorias_destroy(id):   
        categoria_ELIMINADA = ModelCategorias.destroy(db, id)
        if categoria_ELIMINADA:
            flash('categoria Eliminada Exitosamente')
            return redirect('/categorias')
        else:
            flash('error al eliminar la categoria')
            return redirect('/categorias')

# Fin de Rutas de Categorias


# Rutas de proyectos

@app.route('/proyecto')
@login_required
def proyecto_index():
    proyectos_list = ModelProyectos.get(db) 
    return render_template('admin/proyectos/index.html' , proyectos = proyectos_list)
  

@app.route('/proyecto/create', methods=['GET', 'POST'])
@login_required
def proyecto_create():
    categorias_list = ModelCategorias.get(db)
    return render_template('admin/proyectos/create.html', categorias = categorias_list)
    


@app.route('/proyecto/store', methods=['GET', 'POST'])
@login_required
def proyecto_store():
    if request.method == 'POST':
        proyecto = Proyecto(None, request.form.get('categoria_id'), request.form.get('usuario_id'), request.form.get('titulo'), request.form.get('descripcion'), request.form.get('fecha_inicio'), request.form.get('fecha_fin'))
        proyecto_creada = ModelProyectos.store(db, proyecto.to_dict())
        if proyecto_creada:
            flash('Proyecto creado correctamente')
            return redirect('/proyecto')
        else:
            flash('Error al crear el Proyecto')
            return redirect('/proyecto')

@app.route('/proyecto/destroy/<id>')
@login_required
def proyecto_destroy(id):   
        Proyecto_ELIMINADO = ModelProyectos.destroy(db, id)
        if Proyecto_ELIMINADO:
            flash('Proyecto Eliminado Exitosamente')
            return redirect('/proyecto')
        else:
            flash('Error al eliminar el Proyecto')
            return redirect('/proyecto')
# Fin de Rutas de proyectos

# Rutas de calculo
@app.route('/calculo/<proyecto_id>', methods=['GET'])
@login_required
def calculo_index(proyecto_id):
    calculos_list = ModelCalculos.get(db, proyecto_id)
    formula_list = ModelFormula.get(db) 
    return render_template('admin/Calculos/index.html' , calculos = calculos_list, formulas = formula_list, proyecto_id = proyecto_id) 
  

@app.route('/calculo/create', methods=['GET', 'POST'])
@login_required
def calculo_create():
    calculos_list = ModelCalculos.get(db)
    return render_template('admin/calculos/create.html', calculos = calculos_list)
    


@app.route('/calculo/store', methods=['GET', 'POST'])
@login_required
def calculo_store():
    if request.method == 'POST':
        formula = ModelFormula.show(db, request.form.get('formula_id'))
        calculo = Calculos(None, request.form.get('proyecto_id'), request.form.get('formula_id'), Calculos.evaluar_formula(formula[0].get('expresion'), request.form.get('parametros')), request.form.get('parametros'))
        calculo_creada = ModelCalculos.store(db, calculo.to_dict())
        if calculo_creada:
            flash('Calculo creado correctamente')
            return redirect('/calculo/{}'.format(request.form.get('proyecto_id')))
        else:
            flash('Error al crear el Calculo')
            return redirect('/calculo/{}'.format(request.form.get('proyecto_id')))

@app.route('/calculo/destroy/<id>')
@login_required
def calculo_destroy(id):   
        Calculo_ELIMINADO = ModelProyectos.destroy(db, id)
        if Calculo_ELIMINADO:
            flash('Calculo Eliminado Exitosamente')
            return redirect('/calculo')
        else:
            flash('Error al eliminar el Calculo')
            return redirect('/calculo')



# Fin de ruta de calculo


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()