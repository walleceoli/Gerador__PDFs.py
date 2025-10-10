# Gerador__PDFs.py
Na necessidade de estudar para uma prova que iria abranger todos os conteúdos das avaliações feitas até o momento, que seria de 1 ano de faculdade, resolvi criar um sistema onde eu conseguisse passar todas as avaliações para PDFs, para facilitar os estudos, utilizando apenas IA, que no caso foi o Copilot e Python.


#  Gerador de PDF

Este projeto é um **gerador automático de PDFs** com *questões, alternativas e resumos de atividades*, desenvolvido em **Python** utilizando a biblioteca [`fpdf`](https://pyfpdf.github.io/fpdf2/).

O sistema lê listas de questões pré-formatadas no código e gera um arquivo PDF bem estruturado e pronto para impressão ou distribuição digital.

---

##  Funcionalidades

-  Geração automática de PDFs a partir de dados estruturados em listas/dicionários.  
-  Função de limpeza de texto (`limpar_texto`) para corrigir caracteres problemáticos e emojis.  
-  Organização do conteúdo em **atividades**, contendo:
  - Pergunta  
  - Lista de alternativas  
  - Resumo explicativo  
-  Criação de novas páginas automaticamente para cada atividade.  
-  Exportação final para um arquivo PDF (`nome_desejado.pdf`).

---

##  Prompt utilizado

-Extraia todas as perguntas, alternativas e destaque a resposta correta. Depois, para cada questão, faça um pequeno resumo explicando por que a resposta está correta.

-Quero tudo no formato que irei te passar abaixo (não utilize caracteres Unicode no texto):
atividade_1 = [ { "pergunta":"Dos pontos listados abaixo, qual deles é mais importante na aplicacao do Business Intelligence?", "alternativas":[ "Geracao de uma infinidade de graficos", "Fornecer suporte ao processo de tomada de decisao (Correta)", "Verificar se as previsoes feitas pelos gestores se concretizaram ou nao", "Transformar conhecimento em dados e em informacoes", "Geracao de uma infinidade de relatorios" ], "resumo":"O objetivo central do Business Intelligence (BI) e apoiar a tomada de decisao. Graficos e relatorios sao apenas ferramentas; o que realmente importa e transformar dados em insights que orientem escolhas estrategicas." }.

-Quero tudo em formato de codigo pronto para copiar e colar em um projeto python.

---





