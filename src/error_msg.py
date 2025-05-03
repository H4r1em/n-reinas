import flet as ft

def error_msg(mensaje: str) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    mensaje,
                    color=ft.Colors.RED,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    max_lines=3,
                    overflow=ft.TextOverflow.ELLIPSIS
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        width=180,
        height=120,
        padding=10,
        margin=0,
        border_radius=0,
        alignment=ft.alignment.center
    )
