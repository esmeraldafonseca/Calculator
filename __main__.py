import customtkinter as ctk

class Calculadora:

    def __init__(self):    
        self.app = ctk.CTk()
        self.app.title("Calculadora")
        self.app.geometry("370x540")
        self.app.resizable(False, False)

        self.expressao = ""

        main=ctk.CTkFrame(self.app, bg_color="#363636", fg_color="#363636")
        main.pack(fill="both", expand=True)

        frame1 = ctk.CTkFrame(main, bg_color="#363636", fg_color="transparent",
                                border_color="#00008B", border_width=3)
        frame1.pack(fill="x", padx=10, pady=10)
        
        self.panel =ctk.CTkLabel(frame1, text="", bg_color="#363636", font=("Arial", 16))
        self.panel.pack(fill="both", expand=True, padx=10, pady=20)

        self.resultado = ctk.CTkLabel(frame1, text="", bg_color="#363636", font=("Arial", 28, "bold"))
        self.resultado.pack(fill="both", expand=True, padx=10, pady=30)


        frame2 = ctk.CTkFrame(main, bg_color="#363636", fg_color="#363636" )
        frame2.grid_columnconfigure((0,1,2,3), weight=1)
        frame2.pack(fill="both", expand=True)

        botoes = [
            ["1", "2", "3", "+"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "x"],
            ["0", "C", "=", "/"]
        ]

        for linha, valores in enumerate(botoes):
            for coluna, texto in enumerate(valores):

                btn = ctk.CTkButton(frame2, text=texto, fg_color="#1E90FF", height=80, 
                                    font=("Arial", 28, "bold"), command=lambda t=texto: self.clique(t))

                btn.grid(row=linha, column=coluna, padx=5, pady=5)
    def clique(self, valor):

        if valor == "C":
            self.expressao = ""
            self.panel.configure(text="")
            self.resultado.configure(text="0")
            return

        if valor == "=":
            self.calcular()
            return

        if valor == "x":
            valor = "*"

        self.expressao += valor

        self.panel.configure(
            text=self.expressao.replace("*", "x")
        )

    def calcular(self):

        try:
            resultado = eval(self.expressao)

            self.resultado.configure(text=str(resultado))

            self.expressao = str(resultado)

            self.panel.configure(text=self.expressao.replace("*", "x"))

        except Exception:
            self.resultado.configure(text="Erro")
            self.expressao = ""

    def executar(self):
        self.app.mainloop()


if __name__ == "__main__":
    app=Calculadora()
    app.executar()
    