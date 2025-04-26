import flet as ft

def tablero(n=4, size_tab=750, ubicaciones = []):
    cell_size = int(size_tab * 0.8) // n if n > 0 else 50
    board_width = cell_size * n
    ubis = [x - 1 if x > 0 else x for x in ubicaciones]

    rows = []
    for i in range(n):
        row_celdas = []
        for j in range(n):
            es_clara = (i + j) % 2 == 0
            color = ft.Colors.BLUE_300 if es_clara else ft.Colors.BLUE_700

            hay_reina = i < len(ubis) and ubis[i] == j
            contenido = ft.Text("♛", size=int(cell_size*0.7), text_align= ft.TextAlign.CENTER ) if hay_reina else None

            celda = ft.Container(
                width=cell_size,
                height=cell_size,
                bgcolor=color,
                alignment=ft.alignment.center,
                adaptive=True,
                content=contenido,
                margin=0,
                padding=0
            )
            row_celdas.append(celda)
        row = ft.Row(controls=row_celdas, spacing=0, alignment=ft.MainAxisAlignment.CENTER)
        rows.append(row)

    tablero_container = ft.Column(
        controls=rows,
        spacing=0,
        alignment=ft.MainAxisAlignment.CENTER

    )

    contenedor = ft.Container(
        content=tablero_container,
        width=board_width,
        height=board_width,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.GREY_200,
        padding=0,
        margin=0,
        border_radius= 3,
    )

    return contenedor