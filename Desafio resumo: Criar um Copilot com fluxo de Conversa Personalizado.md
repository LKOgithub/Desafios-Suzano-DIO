# Criando um Coplilot com Fluxo de Conversa Personalizado no Microsoft Studio

  ## Etapas do desafio
  URL: https://copilotstudio.microsoft.com
  Criar um Copilot em  branco
  Customizar um tópico
  Personalizar uma mensagem de erro de tópico
  Aumentar/diminuir a qualidade da resposta com GenAI

  ## Links de dúvidas
    Microsoft Learn: https://learn.microsoft.com/pt-br/microsoft-copilot-studio
    Romão's Learn:  https://romaos.com.br/learn
  
  ## Criar um Copilot em branco
      Acessar o copilotstuido.microsoft.com com a sua conta microsoft 365
      Criar um agente em branco (clicar em + new agent)
      Language: recomendado usar em English (en-US)
      Name: Agente da DIO (ou qualquer nome que queira dar ao agente)
      Descripton: Agente responsável por buscar conteúdos de copilot studio dentro da documentação oficial da microsoft
      Instructions: Você é o agente chamado "Agente da DIO", e vai agir em tom formal com o idioma em português para retomar informações relevantes da documentação oficial da microsft (Agente de prompt)
                    Ao retornar uma resposta para a pergunta do usuário você deve considerar:
                    - Buscar a melhor resposta na documentção
                    - Retornar a resposta apropriada e amigável de tom formal
                    - Retornar uma ou mais citações da documentação
      Knowledge: Não está na parte do desafio, mas pode adicionar arquivos
      Advanced Settings: pode escolher o padrão de solução
      Clicar Create (criou o agente)

  ## Customizar um tópico
      No agente criado, podemos utilizar o test your agent para conversar com nosso agente criado
      Clicar em + Add a topic para adicionar um tópico
      Phrases: buscar informações de ai builder (textos/termos que ativarão esse tópico)
               o que é ai builder
      Adicionar uma nova ação: Create generative answers
        Input Activity.Text string
        Data sources: adiconar o arquivo da microsoft learn ou site
      Adicionar uma nova ação: Message (essa parte é para testar se estamos caindo nesse tópico ao conversar com o agente)
        Text: Tópico de AI Builder encerrado!

      Em test your agent, podemos conversar com o agente criado para testar

  ## Personalizar uma mensagem de erro de tópico
      Por vezes o agente pode cair em respostas que não faz sentido ou não entender
      Utilizar o test your agent para testar essas configurações, mande kkkkkk e veja
      A IA pedirá para adicionar dados para parametrizar respostas
      Entre em Topics - Conversational boosting (é como ele irá responder para qualquer assunto que o agente não entender)
                    Create generative answers e configurar a resposta 
                    Outra configuração permite respostas usando conhecimento prévio da IA "Allow the AI to use its own general knowledge"
      Topics - system - Fallback - Tudo que acontecer e falhar ele cai vir para o Fallback (essa é outra maneira de também)
                    Create generative answers e configurar a resposta
      Uma das formas aocnselháveis seria colocar uma mensagem de contato para uma pessoa, email e outros dados para entrar em contato
 
  ## Aumentar e diminuir a qualidade da resposta com GenAI
      Na parte de topicos, em create generative answers, você pode usar o edit Data sources e selecionar novas fontes para resposta da IA
      O copilot utiliza o GPT4 atualmente 2022 (gravação da aula)
      Quando você utilizar o conhecimento prévio, ele utiliza o conhecimento que é atualizado ao GPT4 com os dados até a data de atualização do GPT
      Content moderation level: High, Medium. Low (high - ele tentará ser o menos criativo possível e o mais conciso de acordo com os documentos, data source)
      Content moderation level: low - a IA poderá tentar ser criativa e criar uma resposta
      {x} fx: Buscar dados do AI Builder com base na pergunta do pergunta do usuário (microsoft permite 8000 caracteres para adiconar nesse tópico)

      Settings: Generative AI
                Pode configurar se será mais criativo ou mais preciso, aqui afetará o agente todo, no topic era somente para responder aquele tópico    
