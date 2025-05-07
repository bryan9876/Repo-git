import os
import subprocess
from datetime import datetime, timedelta
import random

# Datos del autor
AUTHOR_NAME = "bryan9876"
AUTHOR_EMAIL = "bryanalejandrom744@gmail.com"

# Archivo simulado
FILENAME = "activity.txt"

# Rango de fechas
start_date = datetime(2024, 6, 15)
end_date = datetime(2025, 5, 7)

# Asegúrate de estar en un repositorio Git
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])

# Asegura que el archivo exista
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("Registro de actividad falsa\n")

# Itera día por día
current_date = start_date
while current_date <= end_date:
    weekday = current_date.weekday()  # 0 = lunes, 6 = domingo

    # Define commits por día
    if weekday >= 5:  # sábado y domingo
        commits_today = random.randint(3, 7)
    else:  # lunes a viernes
        commits_today = random.randint(1, 4)

    for i in range(commits_today):
        # Simula cambio en archivo
        with open(FILENAME, "a") as f:
            f.write(f"Commit simulado {i+1} en {current_date.strftime('%Y-%m-%d')}\n")

        # Agrega archivo
        subprocess.run(["git", "add", FILENAME])

        # Hora aleatoria realista
        hour = random.randint(9, 18)
        minute = random.randint(0, 59)
        commit_time = current_date.replace(hour=hour, minute=minute, second=0)
        date_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")

        # Entorno para git
        env = os.environ.copy()
        env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
        env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
        env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
        env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str

        # Commit
        subprocess.run(
            ["git", "commit", "-m", f"Commit simulado {i+1} en {current_date.strftime('%Y-%m-%d')}"],
            env=env
        )

    # Siguiente día
    current_date += timedelta(days=1)

print("✅ Commits simulados generados con éxito.")