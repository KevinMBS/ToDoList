BASE_WIDGETS="#ECEBDE"
BG="#A59D84"
BTN="#C1BAA1"
import flet as ft
import todolist as tdl

def main(page: ft.Page):
    page.title="To do App"
    page.theme_mode=ft.ThemeMode.DARK
    tasks = []

    def add_new_task(e):
        new_tdl = tdl.Todolist(new_task_field.value)
        #salvar new_tdl no DB
        tasks.append(ft.Checkbox(label=new_task_field.value))
        tasks_view.controls = tasks
        new_task_field.value=""
        page.update()

    #Creating elements
    new_task_field=ft.TextField(hint_text="What's needs to be done?",border_color=BASE_WIDGETS,expand=True)
    btn_add_task=ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_new_task,bgcolor=BTN)
    tasks_view = ft.Column(scroll=True)
    insertion_fields=ft.Row(controls=[new_task_field,btn_add_task])
    visualization_fields=ft.Row(controls=[tasks_view])

    main_container = ft.Container(
        width=600,
        height=800,
        bgcolor= BG,
        padding=10,
        content=ft.Column(
            controls=[
            insertion_fields,
            visualization_fields
            ]
        )
    )

    #Adding elements
    page.add(main_container)
    page.update

if __name__ == '__main__':
    ft.app(target=main)