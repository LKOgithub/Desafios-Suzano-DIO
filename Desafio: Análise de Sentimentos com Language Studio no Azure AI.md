# Análise de sentimentos com Language Studio no Azure AI

## Azure AI - Language Studio
É um ferramenta baseado no cenário do usuário, retira dados sobre o que está escrevendo
Exemplo: "Passei férias maravilhosas na França"
Dados: Idioma Predominante: Português
       Sentimento: 0,88 (positivo)
       Frases-chave: "férias maravilhosas"
       Entidades: França
Quando se fala sobre inteligência artificial precisa lembrar de repositório de informações: Tem muitos dados e não tem pessoas suficientes para fazer análise
Então a IA, por exemplo, poderia ser usado para analisar o feeback dos clientes de uma empresa para saber se estão positivas, ou negativas, mesmo com alto volume de mensagens

## Serviço de bot do Azure
É um serviço de criação de bot para conversa, muito usado, para suporte de tira-dúvidas
O serviço de bot vai ser eficiente conforme a base de dados que ele tem
Antigamente utilizava uma base de dados local, e alguns bots só traziam opções para o usuário e não podia ter uma conversa
Atualmente o azure melhorou e adquiriu diversos recursos:
  Plataforma baseada em nuvem para desenvolvimento e gerenciamento de bots
  Integração com AI Language e outros serviços
  Conectividade através de vários canais

## Compreensão da linguagem coloquial
Geralmente quando se fala deste modelo de linguagem temos 3 componentes:
  Exemplo: "Acenda a luz"
    Entidade: luz
    Declaração: "Acenda a luz"
    Intenção: Acenda
Ele precisa de um reconhecimento e síntese de fala
  Serve para converter texto em fala, para o bot poder responder

## Links úteis para buscar mais informações
  https://aka.ms/ai900-speech
  https://aka.ms/ai900-text-analysis

## Laboratório: Hands on
  URL: speech.microsoft.com/portal
  login é o mesmo para criação no portal
  Esse serviço pode fazer a conversão do áudio para escrita como escrita para o áudio
  Vai nas configurações (engrenagem):
  Vai em recurso, e criar um recurso e vai selecionar sua assinatura, região e selecionar Tipo de preço: Padrão S0
  Apartir desse momento vai surgir o recurso podendo selecionar ela
  Conversão de fala em texto em tempo real
    selecionar qual o idioma, e escolher qual arquivo de áudio que vai importar
    Aqui pode testar o bot
    Ele mostrará um texto que corresponde ao que está sendo dito no áudio
  
  Próxima etapas:
    Introdução: Recurso de fala e exemplo no github
    Cenários Comuns: Utilizar esse aplicativo para fazer um conteúdo em tempo real
                     Transcrição pode ser um call center
    Serviçoes relacionados: Podemos colocar diversas configurações para o uso
                            Aqui podemos importar diversos textos e automatizar isso para uma secretária eletrêonica
    Avaliar o preço: Terá o custo do serviço, geralmente o custo é por hora de áudio
    Uso responsável da IA: Manter os príncipios éticos: imparcialidade, confiabilidade, segurança, privacidade e proteção, inclusividade, transparência
    
    
  Mais informações: github.com/Azure-Samples/cognitive-services-speech-sdk
  No github tem todo um documento falando sobre como utlizar o serviço
  
  ## Language Studio - análise de sentimento
  O Language Studio pode nos ajudar a fazer uma análise semântica, uma análise de sentimento para entender
  Por exemplo: se eu tenho uma rede de hotéis, o bot pode ler os feedbacks e elencar os melhores comentários e os piores, podemos mostrar quais são os pontos negativos e os positivos
  Create resource *
    Create language
    pricing: esolher o plano e forma de pagamento
  Create New project: Classify text -> Analyze sentiment and mine opinions
  Select text language (coloque o idioma do texto)
  select your azure resource: O recurso que criamos anteriormente *
  Podemos inserir um texto para fazer um teste, e aperte RUN
  Result: mostra toda análise feita pela IA

  Next Steps (próximos passos)
  Get started - configurações gerais
  Run the code - configurar especialidade do bot
  See princing - forma de pagamento, qual o plano vai escolher
  Responsible use of AI - Manter os príncipios éticos: imparcialidade, confiabilidade, segurança, privacidade e proteção, inclusividade, transparência
  
  
