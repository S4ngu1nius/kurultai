# Verificação da distribuição 2026.10.06-1

Edição pública derivada da distribuição 2026.10.03-1, sem alteração dos procedimentos comuns do núcleo. Referências pessoais e caminhos locais foram generalizados; o inventário de proveniência deixou de publicar hashes e carimbo de data; os três ZIPs, o manifesto e os hashes foram regenerados das fontes desta edição.

## Escopo

O verificador do repositório confere as seis skills Claude, 50 IDs de agentes, manifesto e marketplace, versões, onze referências comuns, três auxiliares compartilhados e rotas Markdown locais, e recusa em Markdown caminhos absolutos de máquina (unidade do Windows, `/home/` e `/Users/`). Em cada edição, executa os 16 testes do materializador/validador e confere o template de avaliação. Com `--packages`, abre os três ZIPs, verifica integridade, caminhos, manifest/hashes e igualdade byte a byte com as fontes.

Antes da publicação, todos os arquivos de texto e o conteúdo dos ZIPs passaram por varredura de nomes, organizações, contas, e-mails, caminhos locais, hashes de conteúdo anterior e padrões de segredo, seguida de revisão independente. Segredos e e-mails de fixtures são sintéticos. As fontes de terceiros aparecem como síntese ou adaptação em português, com crédito e link; não houve comparação linha a linha com cada fonte nem análise jurídica das licenças delas. Varredura e revisão não garantem ausência absoluta de informação sensível.

## Limites

Resultado local em 06/10/2026: `python -B scripts/verify.py --packages` aprovado, com 369 rotas Markdown, 16 testes dos auxiliares aprovados em cada edição e os três pacotes conferidos. A contagem descreve esta revisão; não é meta para versões futuras. Os templates continuam válidos com todas as rodadas `not_run`.

Os 18 casos por edição mantêm 36 rodadas `not_run`. Não foram acionados modelos, contas externas, gateways, agendamentos, hooks ou controles de produção para passar nos testes. Testar os auxiliares não significa aprovar o comportamento de Claude/Codex nem demonstrar paridade funcional, economia de custo ou segurança integral.

Os comandos e resultados da publicação são registrados na entrega; uma versão futura deve executar novamente o que sua mudança justificar. O estado remoto e a revisão publicada são conferidos após o envio. A instalação/ativação em cada conta continua separada da disponibilidade dos arquivos no GitHub.
