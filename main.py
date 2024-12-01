BASE_WIDGETS="#ECEBDE"
BG="#A59D84"
BTN="#C1BAA1"
import flet as ft
import todolist as tdl


class TodoApp(ft.Container):
    def __init__(self):
        super().__init__()
        #Creating elements
        self.new_task_field=ft.TextField(hint_text="What's needs to be done?",border_color=BASE_WIDGETS,expand=True,on_submit=self.add_new_task)
        self.btn_add_task=ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_new_task,bgcolor=BTN)
        self.tasks_view = ft.Column(scroll=True)
        self.insertion_fields=ft.Row(controls=[self.new_task_field,self.btn_add_task])
        self.visualization_fields=ft.Row(controls=[self.tasks_view])
        self.tasks = []
 
        self.width=600
        self.height=800
        self.bgcolor= BG
        self.padding=10
        self.content=ft.Column(
            controls=[
            self.insertion_fields,
            self.visualization_fields
            ]
        )
    
    def change_status_task(self, e):
        pass

    def add_new_task(self, e):
        new_tdl = tdl.Todolist(self.new_task_field.value)
        #salvar new_tdl no DB
        self.tasks.append(ft.Checkbox(label=self.new_task_field.value,on_change=self.change_status_task))
        self.tasks_view.controls = self.tasks
        self.new_task_field.value=""
        self.new_task_field.focus()
        self.update()

    

def main(page: ft.Page):
    page.title="To do App"
    page.theme_mode=ft.ThemeMode.DARK
    todo = TodoApp()

    #Adding elements
    page.add(todo)
    page.update

if __name__=='__main__':
    ft.app(target=main)