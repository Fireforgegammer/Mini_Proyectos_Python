import string

def evaluar_password(password):
    puntuacion = 0

    if any(c in string.ascii_uppercase for c in password):
        puntuacion += 1
    if any(c in string.ascii_lowercase for c in password):
        puntuacion += 1
    if any(c in string.digits for c in password):
        puntuacion += 1
    if any(c in string.punctuation for c in password):
        puntuacion += 1

    if len(password) >= 12:
        puntuacion += 2
    elif len(password) >= 8:
        puntuacion += 1

    if puntuacion <= 2:
        return "❌ Débil"
    elif puntuacion == 3:
        return "⚠️ Media"
    elif puntuacion == 4:
        return "✅ Fuerte"
    else:
        return "🔥 Muy fuerte"