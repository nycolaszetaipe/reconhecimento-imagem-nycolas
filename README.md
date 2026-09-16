# Repositório de Projetos - Nycolas

Este repositório contém uma coleção de projetos e experimentos variados, abrangendo Inteligência Artificial, Desenvolvimento Web, Desenvolvimento de Jogos e Qualidade de Código. O repositório foi organizado para abrigar múltiplos subprojetos de forma estruturada.

## 📁 Estrutura do Repositório

O repositório é composto pelos seguintes subprojetos:

### 1. [Reconhecimento de Imagem (Teachable Machine)](./reconhecimento-imagem/)
Uma aplicação web que utiliza **TensorFlow.js** e o modelo treinado no **Teachable Machine** do Google para realizar predições de imagens em tempo real através da webcam.
- **Tecnologias:** HTML, CSS (Bootstrap), JavaScript, TensorFlow.js.
- **Sugestões de Melhoria:**
  - **Upload de Imagens:** Adicionar a opção de fazer upload de uma imagem do computador, não limitando apenas ao uso da webcam.
  - **Histórico:** Salvar o histórico das últimas predições (com as maiores porcentagens) utilizando o `localStorage` do navegador.
  - **Seletor de Modelos:** Permitir que o usuário insira a URL de outros modelos do Teachable Machine para testar no mesmo layout.

### 2. [TaskFlow - Todo App](./todo-app/)
Um gerenciador de tarefas moderno com design baseado em *Glassmorphism*. O projeto apresenta telas de Login, Registro e um Dashboard interativo.
- **Tecnologias:** HTML, Tailwind CSS, JavaScript.
- **Sugestões de Melhoria:**
  - **Integração com Backend:** Implementar um banco de dados (ex: Firebase, Supabase ou Node.js com MongoDB) para que as contas e tarefas sejam salvas na nuvem e acessíveis em diferentes dispositivos.
  - **Drag and Drop:** Adicionar a capacidade de reordenar as tarefas arrastando e soltando.
  - **Prazos e Alertas:** Incluir a opção de definir datas de vencimento para as tarefas, com alertas visuais para tarefas atrasadas.

### 3. [Space Shooter](./space_shooter/)
Um jogo 2D de nave espacial desenvolvido em Python, onde o jogador deve atirar e desviar de obstáculos/inimigos.
- **Tecnologias:** Python, Pygame.
- **Sugestões de Melhoria:**
  - **Sistema de Pontuação Máxima (High Score):** Salvar o recorde do jogador em um arquivo local (`.json` ou `.txt`) para persistir entre as sessões.
  - **Power-ups e Upgrades:** Introduzir itens que caem da tela para melhorar o tiro, adicionar escudos ou recuperar vida.
  - **Áudio:** Incluir efeitos sonoros para os tiros, explosões e uma música de fundo para maior imersão.

### 4. [Testes de Código (Assistent Code)](./teste-assistent-code/)
Uma coleção de scripts focados em resolução de algoritmos, refatoração e debugging em Python (ex: verificação de números primos).
- **Tecnologias:** Python.
- **Sugestões de Melhoria:**
  - **Testes Automatizados:** Implementar testes unitários utilizando o `pytest` ou `unittest` para garantir que as refatorações não quebrem o comportamento original.
  - **Type Hints:** Adicionar anotações de tipo (`typing`) nas funções para melhorar a legibilidade e facilitar a identificação de erros por linters.

---

## 🛠️ Como Executar os Projetos

Cada projeto possui sua própria forma de execução:
- **Projetos Web (`reconhecimento-imagem` e `todo-app`):** Basta abrir o arquivo `index.html` correspondente no seu navegador ou utilizar uma extensão como o *Live Server* no VSCode.
- **Projetos Python (`space_shooter` e `teste-assistent-code`):** Certifique-se de ter o Python instalado. Para o jogo, instale as dependências executando `pip install pygame` e inicie com `python main.py`.

---
*Organizado e revisado pela IA.*
