from django.shortcuts import render
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.db import connection
# import pandas as pd
# from django.contrib.auth import logout

# @login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

# @login_required
def historial_view(request):
    return render(request, 'historial.html')

# def logout_view(request):
#     logout(request)
#     return redirect('login')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')  # Redirige si ya está autenticado
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')

# @login_required
def estadisticas_view(request):
    # Ejemplo de consulta SQL
# query = """
# SELECT DAYNAME(fecha) as dia, HOUR(fecha) as hora, COUNT(*) as asistencias
# FROM asistencia
# GROUP BY dia, hora;
# """

# df_raw = pd.read_sql(query, connection)

# # Transformar en formato de tabla tipo [hora][día] = asistencia
# df = df_raw.pivot(index='hora', columns='dia', values='asistencias').fillna(0)

  # 🔶 PASO 1: Datos simulados de actividad (día x hora)
    dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie']
    horas = [f'{h}:00' for h in range(8, 21)]  # De 8:00 a 20:00
    data = np.random.randint(0, 20, size=(len(horas), len(dias)))  # MockData

    # 🔶 PASO 2: Crear DataFrame (esto facilitará el reemplazo por datos reales)
    df = pd.DataFrame(data, index=horas, columns=dias)

    # 🔶 PASO 3: Generar el heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df, cmap='YlOrRd', linewidths=0.3, linecolor='gray', annot=True, fmt='d')
    plt.title('Mapa de Calor de Asistencia', fontsize=14)
    plt.xlabel('Día de la semana')
    plt.ylabel('Hora del día')
    plt.tight_layout()

    # 🔶 PASO 4: Convertir a imagen base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    heatmap_base64 = base64.b64encode(image_png).decode('utf-8')
    plt.close()

    return render(request, 'estadisticas.html', {'heatmap': heatmap_base64})