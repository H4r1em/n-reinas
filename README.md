# ♛ N-Reinas Solver

## 🧑‍💻 Autores
- Argüello Nájera Juan Diego
- Diaz Aguilar Hans Uriel
- Palma Tellez Herzon


## 🚀 Requisitos

- Python ≥ 3.10
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (gestor de paquetes)
- [Cabal](https://www.haskell.org/cabal/) (para compilar el servidor Haskell)


## ▶️ Cómo ejecutar el proyecto

### 1. 🔧 Iniciar el servidor de Haskell

Desde la carpeta `/server`, compila el servidor y entra al intérprete:

```bash
cd server
cabal build
cabal repl
```

Dentro de ghci, ejecuta el servidor llamando al método main:
```haskell
main
```

### 2. 💻 Ejecutar la interfaz gráfica (GUI)
En otra terminal, desde la raíz del proyecto:
```bash
uv run flet run
```

Esto abrirá la aplicación gráfica en una ventana donde se pueden observar las soluciones dado un número n y cambiar entre estas.

