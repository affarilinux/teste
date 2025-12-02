import flet as ft


def view():
    # Retorna um controle Flet simples
    container = ft.Column([
        ft.Text("Módulo Principal: OK", size=18),
        ft.Text("Este módulo foi carregado dinamicamente.", size=12),
        ft.Row([
            ft.ElevatedButton("Ação local", on_click=lambda e: print("Ação do módulo executada")),
            ft.ElevatedButton("Mostrar hora", on_click=lambda e: e.page.snack_bar.open()),
        ])
    ])
    return container
