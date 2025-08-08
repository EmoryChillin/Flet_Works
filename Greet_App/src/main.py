import flet as ft
from flet import (
Page,
app,
Button,
TextField,
ElevatedButton
)


def main(page: ft.Page):
    page.title = "To Do Work"
    page.bgcolor = ft.Colors.GREY_100

    
    #Taking first and last name
    f_name = ft.TextField(label="First Name", autofocus= True)
    l_name = ft.TextField(label="Last Name", autofocus = True)

    #Button defin
    def btn_click (e):
        greetings.controls.append(ft.Text(f"Helloo  {f_name.value} {l_name.value}"))
        f_name.value = ""
        l_name.value = ""
        f_name.focus()
        page.update()

    #Greetings
    greetings = ft.Column()


    #Button
    say_hello = ft.ElevatedButton("Welcome", on_click = btn_click)

    page.update()
    page.add(
        f_name,
        l_name,
        say_hello
    )

if __name__ == "__main__":
    app(target=main, assets_dir="assets")