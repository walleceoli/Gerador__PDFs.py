from fpdf import FPDF

# Função para limpar caracteres problemáticos
def limpar_texto(texto):
    return (texto.replace("→", "->")
                 .replace("–", "-")
                 .replace("“", '"')
                 .replace("”", '"')
                 .replace("‘", "'")
                 .replace("’", "'")
                 .replace("✅", "(Correta)")
                 .replace("❌", "(Incorreta)"))

# Criando o PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Nome-do-PDF", ln=True, align="C")
pdf.ln(10)

# Função para adicionar atividade
def adicionar_atividade(titulo, questoes):
    pdf.set_font("Arial", 'B', 14)
    pdf.multi_cell(0, 8, limpar_texto(titulo))
    pdf.ln(2)
    pdf.set_font("Arial", '', 12)
    for q in questoes:
        pdf.multi_cell(0, 7, limpar_texto(f"Pergunta: {q['Pergunta']}\nAlternativas:"))
        for alt in q['Alternativas']:
            pdf.multi_cell(0, 7, f"- {limpar_texto(alt)}")
        pdf.multi_cell(0, 7, limpar_texto(f"Resumo: {q['Resumo']}\n"))
        pdf.ln(2)
    pdf.add_page()

# --------------------
# Atividade 1
# --------------------
atividade_1 = [
    {
        "Pergunta":"insira a pergunta desejada.",
        "Alternativas":[
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo":"Conteudo do resumo."
    },
    {
        "Pergunta":"insira a pergunta desejada.",
        "Alternativas":[
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo":"Conteudo do resumo."
    },
    {
        "Pergunta":"insira a pergunta desejada.",
        "Alternativas":[
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo":"Conteudo do resumo."
    },
    {
        "Pergunta":"insira a pergunta desejada.",
        "Alternativas":[
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo":"Conteudo do resumo."
    },
    {
        "Pergunta":"insira a pergunta desejada.",
        "Alternativas":[
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo":"Conteudo do resumo."
    }
]

# --------------------
# Atividade 2
# --------------------
atividade_2 = [
    {
        "Pergunta":"insira a pergunta desejada.",
        "Alternativas":[
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo":"Conteudo do resumo."
    },
    {
        "Pergunta": "insira a pergunta desejada.",
        "Alternativas": [
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo": "Conteudo do resumo."
    },
    {
        "Pergunta": "insira a pergunta desejada.",
        "Alternativas": [
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo": "Conteudo do resumo."
    },
    {
        "Pergunta":"insira a pergunta desejada.",
        "Alternativas":[
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo":"Conteudo do resumo."
    },
    {
        "Pergunta":"insira a pergunta desejada.",
        "Alternativas":[
            "Alternativa_1",
            "Alternativa_2",
            "Alternativa_3",
            "Alternativa_4",
            "Alternativa_5"
        ],
        "Resumo":"Conteudo do resumo."
    }
]
# --------------------
# Adicionando todas as atividades
# --------------------
adicionar_atividade("Atividade 1", atividade_1)
adicionar_atividade("Atividade 2", atividade_2)
# Salvando PDF
pdf.output("Nome-do-PDF.pdf")
print("PDF gerado com sucesso!")
