import flet as ft

def input_user(n_ref, on_submit_callback):
    def on_submit(e):
        try:
            n_value = int(n_reinas_txt.value)
            if n_value < 4:
                n_reinas_txt.error_text = "n debe ser >= 4"
                n_reinas_txt.update()
            else:
                n_reinas_txt.error_text = None
                n_reinas_txt.update()
                on_submit_callback(e)
        except ValueError:
            n_reinas_txt.error_text = "Valor inválido"
            n_reinas_txt.update()

    def on_change(e):
        # Limpiar el mensaje de error
        n_reinas_txt.error_text = None
        n_reinas_txt.update()

    n_reinas_txt = ft.TextField(
        ref=n_ref,
        label="N Reinas",
        hint_text="n >= 4",
        autofocus=True,
        text_align=ft.TextAlign.CENTER,
        text_size=18,
        input_filter=ft.InputFilter(
            allow=True, regex_string=r"^[1-9][0-9]*$|^$", replacement_string=""),
        on_submit=on_submit,
        on_change=on_change,
        border_color=ft.Colors.BLUE_600,
        focused_border_color=ft.Colors.BLUE_100,
    )

    enviar_btn = ft.ElevatedButton(
        text="Enviar", 
        on_click=on_submit,
        width=90,
        height=40,
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD),
             shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )

    input_container = ft.Container(
        content=ft.Column(
            controls=[
                n_reinas_txt,
                ft.Row(
                    controls=[enviar_btn],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=180,
        height=150,
        padding=0,
        margin=0,
        border_radius=5,
        alignment=ft.alignment.center,
    )

    return input_container