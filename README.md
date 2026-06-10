```markdown
# ⚖️ Calculadora de IMC com CustomTkinter

Uma aplicação desktop moderna, minimalista e intuitiva para cálculo do **Índice de Massa Corporal (IMC)**. O projeto foi desenvolvido em Python utilizando a biblioteca **CustomTkinter** para uma interface gráfica (GUI) elegante e responsiva, além de um feedback visual dinâmico com alteração de imagens baseadas no resultado obtido.

---

## 🚀 Funcionalidades

- **Cálculo Preciso:** Processa o peso (kg) e a altura (m) informados para calcular o IMC.
- **Tratamento de Entradas:** Aceita tanto o ponto (`.`) quanto a vírgula (`,`) como separadores decimais para evitar erros comuns de digitação.
- **Feedback Visual Dinâmico:** Altera uma ilustração (boneco) na tela de acordo com a classificação do IMC (Abaixo do peso, Peso normal, Sobrepeso ou Obesidade).
- **Interface Moderna:** Utiliza a biblioteca CustomTkinter com uma paleta de cores harmoniosa ("Verde Saúde", "Branco Clínico", "Cinza Neutro" e "Azul Sereno").
- **Validação de Erros:** Caso o usuário digite letras ou caracteres inválidos, a aplicação exibe uma mensagem de alerta amigável.

---

## 🎨 Paleta de Cores do Projeto

| Cor | Hex | Conceito |
| :--- | :--- | :--- |
| **Verde Saúde** | `#2A9D8F` | Botão principal e bordas de destaque. |
| **Branco Clínico** | `#FFFFFF` | Fundos dos campos de texto (inputs). |
| **Cinza Neutro** | `#E9ECEF` | Cor de fundo da aplicação (Light Mode). |
| **Azul Sereno** | `#264653` | Textos, títulos e efeito hover do botão. |

---

## 📦 Pré-requisitos e Dependências

Para rodar este projeto localmente, você precisará ter o **Python 3.x** instalado e as seguintes bibliotecas:

1. **CustomTkinter:** Para a interface gráfica moderna.
2. **Pillow (PIL):** Para o processamento e exibição correta das imagens.

### Como instalar as dependências:

```bash
pip install customtkinter pillow
