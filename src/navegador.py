import flet as ft

def navegador(res, on_change):
    cont = ft.Ref[int]()
    cont.value = 0

    label = ft.Text(
        spans=[
            ft.TextSpan("Solución "),
            ft.TextSpan(
                str(cont.value + 1) if res else "0",
                ft.TextStyle(
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_100
                ),
            ),
            ft.TextSpan(" de "),
            ft.TextSpan(
                str(len(res)),
                ft.TextStyle(
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_100
                ),
            ),
        ],
        text_align=ft.TextAlign.CENTER,
        size=16
    )

    def actualizar_tablero():
        if res:
            i = cont.value
            label.spans[1].text = str(i + 1)
            on_change(res[i])
        else:
            label.spans[1].text = "0"
            on_change([])
        label.update()

    def siguiente(e):
        if res and cont.value < len(res) - 1:
            cont.value += 1
            actualizar_tablero()

    def anterior(e):
        if res and cont.value > 0:
            cont.value -= 1
            actualizar_tablero()

    return ft.Container(
        content=ft.Column(
            controls=[
                label,
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=anterior),
                        ft.IconButton(icon=ft.Icons.ARROW_FORWARD, on_click=siguiente),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        width=180, 
        height=100,
        padding=10,
        margin=0,
        border_radius=0,
        alignment=ft.alignment.center
    )