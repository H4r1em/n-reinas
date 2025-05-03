import flet as ft
import tablero as tb
from input_user import input_user
from navegador import navegador
from solver_remoto import resolver_n_reinas
from error_msg import error_msg

def main(page: ft.Page):
    page.title = "N-Reinas Solver"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 1100
    page.window.height = 750
    page.window.center()

    tablero_ref = ft.Ref[ft.Container]()
    n_ref = ft.Ref[ft.TextField]()
    navegador_ref = ft.Ref[ft.Container]()
    n_inicial = 4

    def actualizar_soluciones(n_value):
        if n_value >= 4:
            try:
                soluciones = resolver_n_reinas(n_value)
                if soluciones:
                    actualizar_tablero(soluciones[0])
                    navegador_ref.current.content = navegador(soluciones, actualizar_tablero)
                    navegador_ref.current.update()
                else:
                    actualizar_tablero([])
                    navegador_ref.current.content = navegador([], actualizar_tablero)
                    navegador_ref.current.update()
            except RuntimeError as e:
                actualizar_tablero([])
                navegador_ref.current.content = error_msg(str(e))
                navegador_ref.current.update()
        else:
            actualizar_tablero([])
            navegador_ref.current.content = navegador([], actualizar_tablero)
            navegador_ref.current.update()

    def actualizar_tablero(posiciones):
        if tablero_ref.current is not None:
            n_actual = int(n_ref.current.value) if n_ref.current.value.isdigit() else n_inicial
            tablero_ref.current.content = tb.tablero(n=n_actual, ubicaciones=posiciones)
            tablero_ref.current.update()

    def on_submit_n(e):
        if n_ref.current.value.isdigit():
            n_value = int(n_ref.current.value)
            actualizar_soluciones(n_value)
        else:
            actualizar_tablero([])
            navegador_ref.current.content = navegador([], actualizar_tablero)
            navegador_ref.current.update()

    input_n = input_user(n_ref, on_submit_n)

    contenido_central = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(ref=tablero_ref, content=tb.tablero(n=n_inicial, ubicaciones=[])),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Column(
                    controls=[
                        input_n,
                        ft.Container(ref=navegador_ref, content=navegador([], actualizar_tablero)),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        alignment=ft.alignment.center,
    )

    page.add(
        ft.SafeArea(
            contenido_central,
        )
    )

    def on_page_load(e):
        actualizar_tablero([])
        navegador_ref.current.content = navegador([], actualizar_tablero)
        navegador_ref.current.update()

    page.on_load = on_page_load

if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)