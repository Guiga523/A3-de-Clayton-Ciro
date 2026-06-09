import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("Light")  

VERDE_SAUDE = "#2A9D8F"
BRANCO_CLINICO = "#FFFFFF"
CINZA_NEUTRO = "#E9ECEF"
AZUL_SERENO = "#264653"

def calcular_imc():
    try:
        peso = float(entry_peso.get().replace(",", "."))
        altura = float(entry_altura.get().replace(",", "."))
        
        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            classificacao = "Abaixo do peso"
            imagem_atual = img_magro
        elif 18.5 <= imc < 25:
            classificacao = "Peso normal"
            imagem_atual = img_normal
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
            imagem_atual = img_sobrepeso
        else:
            classificacao = "Obesidade"
            imagem_atual = img_obesidade

        label_resultado.configure(
            text=f"Seu IMC é: {imc:.2f}\nStatus: {classificacao}",
            text_color=AZUL_SERENO  
        )
        label_boneco.configure(image=imagem_atual)
    except ValueError:
        label_resultado.configure(
            text="Por favor, digite números válidos!",
            text_color="#ef4444"  
        )

#INTERFACE GRÁFICA

app = ctk.CTk()
app.geometry("550x550")
app.title("Calculando o IMC")
app.resizable(False, False)
app.configure(fg_color=CINZA_NEUTRO) 

img_magro = ctk.CTkImage(light_image=Image.open("imagens/img_magro.png"), size=(120, 120))
img_normal = ctk.CTkImage(light_image=Image.open("imagens/img_feliz.png"), size=(120, 120))
img_sobrepeso = ctk.CTkImage(light_image=Image.open("imagens/img_gordinho.png"), size=(120, 120))
img_obesidade = ctk.CTkImage(light_image=Image.open("imagens/img_mtogordinho.png"), size=(120, 120))

titulo = ctk.CTkLabel(app, text="Calculadora de IMC", font=("Arial", 24, "bold"), text_color=AZUL_SERENO)
titulo.pack(pady=(40, 20))

label_peso = ctk.CTkLabel(app, text="Peso (kg):", font=("Arial", 14, "bold"), text_color=AZUL_SERENO)
label_peso.pack(pady=(10, 0))

entry_peso = ctk.CTkEntry(app, placeholder_text="Ex: 70,5", width=280, height=38, 
                          fg_color=BRANCO_CLINICO, text_color=AZUL_SERENO, border_color=VERDE_SAUDE)
entry_peso.pack(pady=5)

label_altura = ctk.CTkLabel(app, text="Altura (m):", font=("Arial", 14, "bold"), text_color=AZUL_SERENO)
label_altura.pack(pady=(10, 0))

entry_altura = ctk.CTkEntry(app, placeholder_text="Ex: 1,75", width=280, height=38, 
                            fg_color=BRANCO_CLINICO, text_color=AZUL_SERENO, border_color=VERDE_SAUDE)
entry_altura.pack(pady=5)

botao = ctk.CTkButton(app, text="Calcular IMC", font=("Arial", 14, "bold"), width=280, height=42, 
                      fg_color=VERDE_SAUDE, text_color=BRANCO_CLINICO, hover_color=AZUL_SERENO, command=calcular_imc)
botao.pack(pady=25)

label_boneco = ctk.CTkLabel(app, text="")
label_boneco.pack(pady=5)

label_resultado = ctk.CTkLabel(app, text="", font=("Arial", 16, "bold"))
label_resultado.pack(pady=10)

app.mainloop()