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



