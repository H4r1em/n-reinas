# main.py
import flet as ft
import tablero as tb
from input_user import input_user
from navegador import navegador
from solver_remoto import resolver_n_reinas

def main(page: ft.Page):
    page.title = "N-Reinas Solver (Socket Síncrono)"
    page.window.center()
    page.window.width = 1100
    page.window.height = 750

    tablero_ref   = ft.Ref[ft.Container]()
    navegador_ref = ft.Ref[ft.Container]()
    n_ref         = ft.Ref[ft.TextField]()

    def actualizar_tablero(posiciones: list[int]):
        widget = tb.tablero(n=len(posiciones), ubicaciones=posiciones)
        tablero_ref.current.content = widget
        tablero_ref.current.update()

    def actualizar_soluciones(n_value: int):
        try:
            soluciones = resolver_n_reinas(n_value)
        except RuntimeError as err:
            page.snack_bar = ft.SnackBar(ft.Text(str(err)))
            page.snack_bar.open = True
            page.update()
            return

        if soluciones:
            actualizar_tablero(soluciones[0])
            navegador_ref.current.content = navegador(soluciones, actualizar_tablero)
        else:
            actualizar_tablero([])
            navegador_ref.current.content = navegador([], actualizar_tablero)
        navegador_ref.current.update()

    def on_submit_n(e):
        val = n_ref.current.value
        if val.isdigit() and int(val) >= 4:
            actualizar_soluciones(int(val))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Introduce un entero válido ≥ 4"))
            page.snack_bar.open = True
            page.update()

    input_n = input_user(n_ref, on_submit_n)

    layout = ft.Row(
        controls=[
            ft.Column([ ft.Container(ref=tablero_ref, content=tb.tablero(0, [])) ]),
            ft.Column([
                input_n,
                ft.Container(ref=navegador_ref,
                             content=navegador([], actualizar_tablero))
            ])
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    page.add(layout)
    page.on_load = lambda e: actualizar_tablero([])

if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)
