# Khanato — Kurultai, edição pública

Edição pública do **Khanato**, um método de coordenação de agentes de IA: Temüjin, o Grande Khan, coordena, executa e verifica com as competências pertinentes de produto, dados, plataforma, jurídico, marketing, segurança e IA. Há distribuições para **Codex** e **Claude**. O nome vem do kurultai, a assembleia em que o império mongol decidia seus rumos.

Nas instruções, **Imperador** é você: a pessoa que define mandato, preferências e exceções.

| Edição | Conteúdo | Versão |
|---|---|---|
| [Codex](codex/skills/khanato/SKILL.md) | Skill, metadados de descoberta, referências e auxiliares de avaliação | `2026.10.03-hermes-v1` |
| [Claude](claude/README.md) | Plugin com seis skills, 50 agentes e adaptadores de ambiente | plugin `2.0.0`, núcleo `2026.10.03-claude-v1` |

As duas edições compartilham Constituição, competências, segurança, memória, revisão e métodos Hermes. Ferramentas, permissões, caminhos e carregamento são adaptados à plataforma. Este repositório não contém um runtime Hermes nem promete comportamento idêntico entre modelos.

## Instalar

Clone este repositório ou use **Code → Download ZIP** no GitHub.

```sh
git clone https://github.com/S4ngu1nius/kurultai.git
cd kurultai
```

Os [pacotes prontos](packages/) são versionados junto com as fontes. Confira os hashes em [SHA256SUMS](packages/SHA256SUMS).

### Codex

Extraia `packages/khanato-codex.zip` e coloque a pasta `khanato` no diretório de skills da instalação, em geral `$CODEX_HOME/skills/khanato` (padrão `~/.codex/skills/khanato`). O pacote fonte equivalente é `codex/skills/khanato`.

Versões/superfícies que usam `~/.agents/skills` devem receber a mesma pasta no diretório que realmente descobrem. Confira a configuração vigente; não mantenha duas cópias divergentes do mesmo skill. Preserve a versão existente antes de substituir somente `khanato`, abra uma nova sessão e invoque `$khanato` para verificar o carregamento.

As preferências globais e as configurações de conta são independentes. Esta distribuição mantém a invocação implícita habilitada em `agents/openai.yaml`; isso não substitui uma instrução pessoal permanente para usar Khanato em toda demanda.

### Claude

Em **Customize → Plugins → Add → Upload plugin**, importe `packages/khanato-claude-plugin.zip` quando essa superfície oferecer upload. Confira `khanato` versão `2.0.0` após a instalação. O ZIP contém o manifesto e as pastas na raiz correta; não envie o ZIP do repositório inteiro como plugin.

No Claude Code, o marketplace pode ser adicionado e o plugin instalado:

```text
/plugin marketplace add S4ngu1nius/kurultai
/plugin install khanato@khanato-marketplace
```

Para ensaio local com a CLI já disponível, use `claude --plugin-dir ./claude`. A importação de `packages/khanato-claude-skill.zip` pela área de Skills é uma alternativa que contém o núcleo completo, mas não registra os 50 subagentes nem os cinco comandos adicionais.

Use uma forma de instalação por superfície para evitar cópias divergentes. A conta pode impor disponibilidade/permissões próprias; extração de arquivo não comprova ativação. Consulte o [guia Claude](claude/README.md) e confira a leitura da revisão instalada com uma tarefa pequena.

### Modo padrão e memória

Nas instruções pessoais da plataforma, preserve as outras preferências e acrescente: “Meu modo operacional padrão é Khanato. Use a skill Khanato instalada em toda demanda e apenas as referências pertinentes. A sessão principal coordena, executa e integra. Respeite instruções superiores, permissões, pedido direto e regras locais. Se a skill não estiver acessível, informe a ausência.”

O Khanato pode registrar decisões e alterações num cofre Obsidian. Nenhum cofre é distribuído aqui: indique o seu nas instruções locais (por exemplo, `<raiz>/Obsidian/<Organização>`) e confirme o acesso real em cada computador; sem acesso, o skill produz a nota pendente. O repositório guarda o método; cofre, dados de projetos, histórico de conversas e credenciais não fazem parte dele.

## Atualizar e verificar

Edite a distribuição apropriada e preserve a correspondência entre as duas versões. Mudanças comuns do núcleo devem ser refletidas na outra edição; diferenças de plataforma continuam explícitas. Execute na raiz, com Python 3 disponível:

```sh
python -B scripts/verify.py
python -B scripts/build_packages.py
python -B scripts/verify.py --packages
```

Git precisa estar disponível para os testes do materializador. Os scripts do repositório usam somente a biblioteca padrão. A verificação não executa Claude/Codex nem pontua comportamento de agentes.

Depois de revisar o diff, registre a mudança e publique o commit/tag no GitHub. Para recuperar uma revisão específica, clone e selecione seu tag antes de instalar. Use `git pull --ff-only` para atualizar uma cópia limpa; se houver alterações locais, revise-as antes. Este repositório não instala sincronização ou publicação em segundo plano. No Claude, confira a preferência de atualização automática do marketplace/plugin e mantenha-a desligada se quiser atualizações somente manuais; a escolha é do aplicativo. Um marketplace ligado a um clone local pode carregar os arquivos diretamente, portanto mudar esse checkout pode afetar a próxima sessão.

Leia [manutenção e proveniência](docs/MAINTENANCE.md), [mapa](docs/CODEBASE_MAP.md) e [verificação desta publicação](docs/VALIDATION.md).

## Licença

Distribuído sob a licença MIT; veja [LICENSE](LICENSE). Materiais de terceiros citados mantêm suas próprias licenças; as referências os descrevem como síntese ou adaptação, com crédito e link às fontes.

Fontes de instalação: [skills no Codex](https://developers.openai.com/codex/skills/), [plugins Claude](https://claude.com/docs/plugins/build), [marketplaces Claude Code](https://code.claude.com/docs/en/plugin-marketplaces).
