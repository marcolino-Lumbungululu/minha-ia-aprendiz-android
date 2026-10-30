[app]

# Nome da aplicação
title = Minha IA Aprendiz

# Identificação do pacote
package.name = minhaiaaprendiz
package.domain = org.minhaia

# Directório do código-fonte
source.dir = .

# Extensões dos ficheiros incluídos
source.include_exts = py,db

# Directórios excluídos
source.exclude_dirs = .git, __pycache__, venv, .buildozer, bin

# Versão da aplicação
version = 1.0.0

# Dependências da aplicação
# Nota: Adicionado hostpython3 para estabilizar a compilação cruzada
requirements = python3, kivy, hostpython3

# Orientação do ecrã
orientation = portrait

# Modo de ecrã inteiro
fullscreen = 0

# Permissões Android
android.permissions = INTERNET

# Versões da API Android
android.api = 35
android.minapi = 23

# Versão do Android NDK
# 26b ou 27b são as mais estáveis para APIs 34/35
android.ndk = 27b

# Aceitar automaticamente as licenças do SDK
android.accept_sdk_license = True

# Arquitectura Android
# arm64-v8a é o padrão actual
android.archs = arm64-v8a

# Formato de compilação
android.debug_artifact = apk


[buildozer]

# Nível de registo
# 0 = apenas erros, 1 = informação, 2 = detalhes de depuração
log_level = 2

# Mostrar aviso se o Buildozer for executado como root
# 0 = Não, 1 = Sim
warn_on_root = 1
