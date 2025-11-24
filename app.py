import flet as ft 
import csv
from login_utils import verificar_login, mostrar_tela_sucesso

def main(page:ft.Page):
    page.title = "Cadastro Login"
    page.theme_mode ="dark"
    page.vertical_alignment ="center"
    page.horizontal_alignment ="center"
    page.window.center()
    page.window.width = 600
    page.window.height = 800

    def clique(e):
        valor_login = texto_login.value
        valor_senha = texto_senha.value

        with open(r"Relatorios\dados.csv", "a", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([valor_login, valor_senha])
        
        page.open(ft.SnackBar(ft.Text(f"Conta cadastrada! Bem vindo(a) {valor_login}", color="white"),bgcolor="green", duration=1.7))

        page.update()
    
    def entrar(e):
        login = texto_login.value
        senha = texto_senha.value

        if verificar_login(login,senha):
            mostrar_tela_sucesso(page,login)
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Login ou senha incorretos!", color ="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()

    titulo = ft.Text("Login", color = "white", size = 40)
    texto_login = ft.TextField(label = "Login",
                               focused_border_color= "GREEN",
                               width=300,
                               autofocus=True)
    texto_senha = ft.TextField(label = "Senha",
                               focused_border_color= "GREEN",
                               password= True,
                               can_reveal_password =True,
                               width= 300)
    botao_cadastro = ft.ElevatedButton("Cadastro",
                             on_click=clique,
                             width=100,
                             bgcolor="BLUE",
                             color="white")
    botao_entrar= ft.ElevatedButton("Entrar",
                             on_click= entrar,
                             width=100,
                             bgcolor = "GREEN",
                             color="white")
    page.add(titulo,texto_login,texto_senha,
             ft.Row([botao_cadastro,botao_entrar],alignment="center"))
    
ft.app(target=main)