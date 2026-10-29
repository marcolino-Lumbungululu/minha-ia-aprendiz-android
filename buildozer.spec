[app]

# (string) Title of your application
title = Minha IA Aprendiz

# (string) Package name
package.name = minhaiaaprendiz

# (string) Package domain (needed for android package naming)
package.domain = org.minhaia

# (string) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,db

# (list) List of directories to exclude
source.exclude_dirs = .git, __pycache__, venv, .buildozer

# (string) Application version
version = 1.0.0

# (list) Application requirements
# Note: É altamente recomendável incluir 'hostpython3' para a compilação funcionar corretamente
requirements = python3, hostpython3, kivy

# (string) Supported orientations
orientation = portrait

# (boolean) Fullscreen mode
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
# API 35 é a recomendada para as diretrizes atuais da Google Play
android.api = 35

# (int) Minimum API your APK will support.
android.minapi = 23

# (int) Android SDK version to use
# Deixar em branco ou fixar numa versão estável (ex: 34.0.0) evita que o Buildozer 
# tente descarregar versões Alpha/Beta instáveis (como a v37 que causou o erro)
android.build_tools_version = 34.0.0

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aab)
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
