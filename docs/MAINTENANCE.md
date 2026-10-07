# Manutenção e proveniência

Esta edição pública reúne o skill Codex e o plugin Claude 2.0.0 revisados em 03/10/2026, com referências pessoais e caminhos locais substituídos por papéis e marcadores genéricos. O repositório versiona as duas distribuições para instalação e recuperação; instalações globais e cópias do Cowork são destinos de implantação, não sincronizam automaticamente com o GitHub.

## Fluxo de atualização

1. Confira o pedido, a edição afetada, os arquivos locais e a versão instalada. Preserve autorizações e os limites reais da plataforma.
2. Edite o núcleo comum e propague a mudança para a outra edição quando aplicável. Os adaptadores 12/16/17 do Claude preservam diferenças intencionais. IDs dos seis comandos e 50 agentes devem permanecer compatíveis.
3. Atualize `versions.json`, metadados e manifesto quando a versão correspondente mudar. O número da distribuição identifica o conjunto publicado; não implica alteração comportamental do núcleo.
4. Execute `scripts/verify.py`, regenere os ZIPs e execute `scripts/verify.py --packages`. Revise o conteúdo publicável e os limites do resultado; testes locais não atestam ativação em conta.
5. Quando houver cofre adotado, registre a entrega conforme a política. Faça commit/push no repositório autorizado e confira o SHA remoto. Tags preservam os marcos recuperáveis; não reescreva tags já publicadas.

O registro `claude/skills/khanato/docs/source-parity.json` é a proveniência da adaptação original: correspondência e situação de cada arquivo. Hashes e carimbo de data desse inventário não são publicados nesta edição; não trate esse inventário histórico como mecanismo de sincronização. Compare as fontes atuais no diff e use os manifests dos pacotes para verificar a distribuição real.

## Recuperação

Clone o repositório ou baixe o ZIP. Selecione a revisão desejada; confira `versions.json`, a fonte e `packages/SHA256SUMS`. Os três ZIPs são gerados exclusivamente dos diretórios indicados em `scripts/build_packages.py`. Não dependem de perfis do Windows, pastas de backup, código de outro projeto ou downloads durante a geração.

Antes de substituir uma instalação existente, preserve seu conteúdo e confira alterações posteriores. Restaure somente o escopo do Khanato. Não remova o plugin inteiro como regra universal de atualização nem escreva em arquivos de autenticação. Depois de instalar, confirme a revisão efetivamente carregada na superfície usada.

## Materiais de origem

O núcleo é uma redação de trabalho do Khanato mantida para o Imperador; referências externas e fontes oficiais permanecem próximas dos procedimentos. Ideias de Hermes, Cartographer e demais projetos citados foram adaptadas; seus runtimes, instaladores e catálogos externos não são distribuídos neste repositório. A documentação distingue prática incorporada de integração instalada e comportamento verificado.

O mapa Codex foi refeito para esta distribuição, substituindo referências a evidências locais indisponíveis. Nenhuma transcrição, configuração de autenticação ou conteúdo do cofre foi importado. Histórico detalhado de ensaios anteriores continua nos registros de origem; esta publicação registra apenas as verificações realmente repetidas ou examinadas nela.

A edição é pública e distribuída nos termos de [LICENSE](../LICENSE). A titularidade dos materiais de terceiros citados não foi alterada: eles mantêm suas próprias licenças. As referências descrevem esses trechos como síntese ou adaptação, com crédito e link às fontes; o alcance da conferência está em [verificação](VALIDATION.md). Mudanças de escopo de distribuição ou de licença exigem nova revisão.
