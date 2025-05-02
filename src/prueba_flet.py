import flet as ft

def main(page: ft.Page):
    page.title = "Prueba Flet"
    page.add(ft.Text("¡Hola, Flet está funcionando!"))

if __name__ == "__main__":
    ft.app(target=main)