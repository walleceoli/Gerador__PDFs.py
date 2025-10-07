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
        pdf.multi_cell(0, 7, limpar_texto(f"Pergunta: {q['pergunta']}\nAlternativas:"))
        for alt in q['alternativas']:
            pdf.multi_cell(0, 7, f"- {limpar_texto(alt)}")
        pdf.multi_cell(0, 7, limpar_texto(f"Resumo: {q['resumo']}\n"))
        pdf.ln(2)
    pdf.add_page()

# --------------------
# Atividade 1
# --------------------
atividade_1 = [
    {
        "pergunta":"O desenvolvimento economico de um pais ocorre devido a diversos fatores. Ha um termo que define um profissional que mantem em funcionamento o mercado, cria novos produtos, novos metodos de producao e novos mercados. Analise as afirmacoes e selecione a alternativa correta.",
        "alternativas":[
            "Empreendedor (Correta)",
            "Economista",
            "Administrador",
            "Gerente",
            "Encarregado"
        ],
        "resumo":"O termo correto e Empreendedor, pois ele e o agente de mudanca que cria novos produtos, processos e mercados, assumindo riscos e inovando para gerar desenvolvimento economico."
    },
    {
        "pergunta":"Ha pessoas que possuem caracteristicas e comportamentos que impactam o desenvolvimento economico de um determinado local. Analise as caracteristicas e selecione a alternativa correta.",
        "alternativas":[
            "Presidente",
            "Empreendedor (Correta)",
            "Gerente",
            "Diretor",
            "Jornalista"
        ],
        "resumo":"A resposta correta e Empreendedor, pois e a pessoa que identifica oportunidades, assume riscos, lidera e inova, contribuindo diretamente para o desenvolvimento economico."
    },
    {
        "pergunta":"O empreendedor na criacao e gestao da sua empresa precisa considerar muitos aspectos. Analise as afirmacoes e selecione a alternativa correta.",
        "alternativas":[
            "Apenas as afirmacoes IV e V estao corretas",
            "Todas as afirmacoes estao corretas (Correta)",
            "Apenas as afirmacoes III e IV estao corretas",
            "Apenas as afirmacoes II e V estao corretas",
            "Apenas as afirmacoes I e II estao corretas"
        ],
        "resumo":"Todas as afirmacoes estao corretas, pois a missao e visao orientam a empresa, a analise SWOT e essencial para identificar oportunidades e ameacas, e deve ser revisada continuamente para manter a estrategia alinhada ao mercado."
    },
    {
        "pergunta":"Analise as afirmacoes e selecione a resposta correta com base nos conceitos relativos a analise de SWOT.",
        "alternativas":[
            "Apenas as afirmacoes I, II, IV e V estao corretas (Correta)",
            "Apenas as afirmacoes III, IV e V estao corretas",
            "Apenas as afirmacoes I, II, III e IV estao corretas",
            "Apenas as afirmacoes IV e V estao corretas",
            "Apenas as afirmacoes III e IV estao corretas"
        ],
        "resumo":"A resposta correta e que apenas as afirmacoes I, II, IV e V estao corretas, pois forcas e fraquezas sao internas, consumidores e fornecedores sao fatores microambientais, e a missao deve considerar mercado, produto/servico e tecnologia."
    },
    {
        "pergunta":"O plano de negocios e um instrumento essencial para um empreendedor. Analise as afirmacoes e selecione a resposta correta.",
        "alternativas":[
            "Apenas as afirmacoes I, II e III estao corretas (Correta)",
            "Apenas as afirmacoes II e III estao corretas",
            "Apenas a afirmacao III esta correta",
            "Apenas a afirmacao I esta correta",
            "Apenas as afirmacoes I e II estao corretas"
        ],
        "resumo":"A resposta correta e que as afirmacoes I, II e III estao corretas, pois o plano de negocios funciona como um roteiro seguro, contem os principais topicos de analise e permite controle para acoes corretivas durante a execucao."
    }
]

# --------------------
# Atividade 2
# --------------------
atividade_2 = [
    {
        "pergunta":"Descrever sobre a empresa no Plano de Negocio ajuda a definir a visao, missao, objetivos e localizacao do negocio. Analise as afirmacoes e selecione a resposta correta:",
        "alternativas":[
            "Apenas a afirmacao IV esta correta.",
            "Apenas a afirmacao I esta correta.",
            "Apenas as afirmacoes I, II e IV estao corretas.",
            "Apenas as afirmacoes II, III e IV estao corretas.",
            "Apenas as afirmacoes II e III estao corretas (Correta)"
        ],
        "resumo":"A missao reflete a razao de existir da empresa (II) e os objetivos/metas sao definidos em conjunto com parceiros estrategicos (III). Afirmacoes I e IV estao incorretas porque localizacao nao precisa ser em avenida principal e a visao nao deve ser composta de metas faceis."
    },
    {
        "pergunta":"O plano de marketing considera analisar o produto, praca, preco e promocao dentro dos criterios e abordagem do marketing. Analise as afirmacoes e selecione a resposta correta:",
        "alternativas":[
            "Apenas a afirmacao IV esta correta.",
            "Apenas a afirmacao I esta correta.",
            "Apenas as afirmacoes II e IV estao corretas (Correta)",
            "Apenas as afirmacoes I, II e IV estao corretas.",
            "Apenas as afirmacoes I, II e III estao corretas."
        ],
        "resumo":"A afirmacao II esta correta porque o plano de marketing deve considerar mercado fornecedor, concorrente e consumidor. A afirmacao IV tambem esta correta, pois o preco pode ser percebido como indicador de qualidade. A I esta incorreta (confunde promocao com praca) e a III nao e regra geral."
    },
    {
        "pergunta":"De acordo com o topico Plano de Negocio - Processo de Vendas, sobre o plano de marketing, fazemos a previsao de vendas e, para elaborar o plano, e necessaria uma avaliacao dos objetivos e metas de vendas. Para que isso seja possivel, o empreendedor deve fazer alguns questionamentos. Analise as afirmacoes e selecione a alternativa correta:",
        "alternativas":[
            "Apenas a alternativa I esta correta.",
            "Nenhuma alternativa esta correta.",
            "Apenas a alternativa II esta correta.",
            "Todas as alternativas estao corretas (Correta)",
            "Apenas a alternativa III esta correta."
        ],
        "resumo":"Todas as alternativas estao corretas porque o empreendedor deve avaliar preco, metodos de venda, perfil do cliente, produto, motivacao da equipe e custos envolvidos. Esses pontos sao essenciais para um plano de vendas consistente."
    },
    {
        "pergunta":"O processo de venda e composto por quantas fases?",
        "alternativas":[
            "7",
            "5 (Correta)",
            "6",
            "4",
            "8"
        ],
        "resumo":"O processo de venda e tradicionalmente estruturado em 5 fases: prospeccao, abordagem, apresentacao, fechamento e pos-venda. Por isso a alternativa correta e 5."
    },
    {
        "pergunta":"Uma boa equipe de vendas deve ser construida todos os ____.",
        "alternativas":[
            "dias (Correta)",
            "meses",
            "anos",
            "finais de semanas",
            "sabados"
        ],
        "resumo":"A construcao de uma boa equipe de vendas e um processo continuo, que exige acompanhamento e desenvolvimento diario. Por isso a resposta correta e 'dias'."
    }
]

# --------------------
# Atividade 3
# --------------------
atividade_3 = [
    {
        "pergunta":"O processo de vendas e essencial para uma empresa que necessita vender os seus produtos ou servicos. Analise as afirmacoes:",
        "alternativas":[
            "Apenas as afirmacoes I e III estao corretas (Correta)",
            "Apenas as afirmacoes III e IV estao corretas",
            "Apenas as afirmacoes II e III estao corretas",
            "Apenas as afirmacoes II e IV estao corretas",
            "Todas as afirmacoes estao corretas"
        ],
        "resumo":"As afirmacoes I e III estao corretas porque destacam pontos fundamentais: o pos-venda garante a satisfacao do cliente e a estrutura de vendas deve se adequar ao porte da empresa. As demais afirmacoes trazem erros conceituais sobre conhecimento do produto e escolha aleatoria da equipe."
    },
    {
        "pergunta":"Ha pessoas que possuem caracteristicas e comportamentos que impactam o desenvolvimento economico de um determinado local. Analise as afirmacoes:",
        "alternativas":[
            "Apenas as afirmacoes III e IV estao corretas",
            "Apenas as afirmacoes I e V estao corretas (Correta)",
            "Todas as afirmacoes estao corretas",
            "Apenas as afirmacoes II e V estao corretas",
            "Apenas as afirmacoes I e II estao corretas"
        ],
        "resumo":"As afirmacoes I e V estao corretas porque definem corretamente o conceito de empreendedor e o empreendedorismo dentro de organizacoes, onde os riscos sao assumidos pela empresa. As demais afirmacoes apresentam distorcoes, como negar o risco ou generalizar que todo gerente e empreendedor."
    },
    {
        "pergunta":"O empreendedor necessita possuir algumas habilidades e ter a capacidade de identificar oportunidades. Analise as afirmacoes e selecione a alternativa correta:",
        "alternativas":[
            "Apenas as afirmacoes III e IV estao corretas",
            "Apenas as afirmacoes I e II estao corretas",
            "Apenas as afirmacoes II e IV estao corretas",
            "Todas as afirmacoes estao corretas (Correta)",
            "Apenas a afirmacao IV esta correta"
        ],
        "resumo":"Todas as afirmacoes estao corretas porque descrevem de forma completa as habilidades tecnicas, gerenciais e pessoais do empreendedor, sua capacidade de buscar recursos, analisar cenarios e transformar oportunidades em resultados."
    },
    {
        "pergunta":"As oportunidades de negocio estao distribuidas em quatro grandes areas: manufatura, atacado, varejo e servicos. Analise as afirmacoes e selecione a resposta correta:",
        "alternativas":[
            "Todas as afirmacoes estao corretas (Correta)",
            "Apenas as afirmacoes III e IV estao corretas",
            "Apenas a afirmacao IV esta correta",
            "Apenas as afirmacoes II e IV estao corretas",
            "Apenas as afirmacoes I e II estao corretas"
        ],
        "resumo":"Todas as afirmacoes estao corretas porque descrevem adequadamente as quatro grandes areas de oportunidades de negocio, o papel das empresas de servicos e exemplos praticos como desenvolvimento de software e treinamento profissional."
    },
    {
        "pergunta":"No planejamento das acoes mercadologicas no mix de marketing, define-se o produto, preco, promocao e ponto. Portanto, quais sao as variaveis que precisam ser analisadas para definir o ponto?",
        "alternativas":[
            "Nao e necessario avaliar nenhuma variavel",
            "Tendencia populacional, visibilidade e tamanho",
            "Acesso, limpeza, preco do aluguel e comodidade do empreendedor",
            "Apenas o preco precisa ser analisado",
            "Potencial de Mercado, Acesso, Visibilidade, tamanho, infraestrutura e questoes legais (Correta)"
        ],
        "resumo":"A resposta correta envolve analisar Potencial de Mercado, Acesso, Visibilidade, Tamanho, Infraestrutura e Questões Legais, pois o ponto de venda deve considerar fatores estrategicos que garantam atratividade, viabilidade e conformidade legal."
    }
]

# --------------------
# Atividade 4
# --------------------
atividade_4 = [
    {
        "pergunta":"O Direito e uma ciencia social e juridica que estuda o individuo em seu contexto territorial. Analise as afirmacoes e selecione a resposta correta:",
        "alternativas":[
            "Todas as afirmacoes estao corretas. (Correta)",
            "Apenas as afirmacoes I,II e III estao corretas.",
            "Apenas as afirmacoes I,II e IV estao corretas.",
            "Apenas a afirmacao IV esta correta.",
            "Apenas a afirmacao I esta correta."
        ],
        "resumo":"Todas as afirmacoes estao corretas porque abordam a origem do termo Direito, sua variacao entre paises, sua funcao etica e moral, e a necessidade de evolucao para garantir harmonia social."
    },
    {
        "pergunta":"A Constituicao Federal brasileira tem principios fundamentais que norteiam o ordenamento juridico. Analise as afirmacoes e selecione a resposta correta:",
        "alternativas":[
            "Todas as afirmacoes estao corretas. (Correta)",
            "Apenas a afirmacao I esta correta.",
            "Apenas a afirmacao III esta correta.",
            "Apenas as afirmacoes I e III estao corretas.",
            "Apenas as afirmacoes I e II estao corretas."
        ],
        "resumo":"Todas as afirmacoes estao corretas porque a Constituicao e criada pelo povo, garante a dignidade da pessoa humana e assegura valores sociais do trabalho e da livre iniciativa."
    },
    {
        "pergunta":"A palavra direito advem do latim rectum e significa aquilo que e certo e correto. Analise as afirmacoes e selecione a resposta correta:",
        "alternativas":[
            "Apenas a afirmacao III esta correta. (Correta)",
            "Apenas as afirmacoes I e III estao corretas.",
            "Apenas a afirmacao I esta correta.",
            "Todas as afirmacoes estao corretas.",
            "Apenas as afirmacoes I e II estao corretas."
        ],
        "resumo":"Apenas a afirmacao III esta correta, pois descreve corretamente o Direito Constitucional. As afirmacoes I e II estao invertidas: Direito Publico regula relacoes do Estado e Direito Privado regula relacoes entre particulares."
    },
    {
        "pergunta":"Contrato e a manifestacao de vontade que cria, modifica ou extingue relacoes juridicas. Quais os tipos de contratos existem?",
        "alternativas":[
            "Verbal e escrito.",
            "Somente contrato escrito e pela Internet.",
            "Verbal, escrito, eletronicos na web e telematico. (Correta)",
            "Verbal, por escrito e aceite.",
            "Somente contrato verbal e por escrito."
        ],
        "resumo":"A resposta correta e 'Verbal, escrito, eletronicos na web e telematico', pois os contratos podem assumir diferentes formas, inclusive digitais, desde que expressem a vontade das partes."
    },
    {
        "pergunta":"A analise SWOT e uma ferramenta util para planejamento estrategico. Analise as afirmacoes e selecione a resposta correta:",
        "alternativas":[
            "Apenas a afirmacao I esta correta.",
            "Apenas a afirmacao IV esta correta.",
            "Todas as afirmacoes estao corretas. (Correta)",
            "Apenas as afirmacoes I,II e IV estao corretas.",
            "Apenas as afirmacoes I,II e III estao corretas."
        ],
        "resumo":"Todas as afirmacoes estao corretas porque a analise SWOT contempla forcas, fraquezas, oportunidades e ameacas, permitindo identificar a posicao estrategica da empresa."
    }
]

# --------------------
# Adicionando todas as atividades
# --------------------
adicionar_atividade("Atividade 1", atividade_1)
adicionar_atividade("Atividade 2", atividade_2)
adicionar_atividade("Atividade 3", atividade_3)
adicionar_atividade("Atividade 4", atividade_4)

# Salvando PDF
pdf.output("Nome-do-PDF.pdf")
print("PDF gerado com sucesso!")
