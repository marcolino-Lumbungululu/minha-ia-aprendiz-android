[app]

title = Minha IA Aprendiz
package.name = minhaiaaprendiz
package.domain = org.minhaia

source.dir = .
source.include_exts = py,db
source.exclude_dirs = .git,__pycache__,venv

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 35
android.minapi = 23
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
