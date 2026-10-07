# Khanato — manutenção deste repositório

Use o skill Khanato disponível e apenas as referências pertinentes. Este repositório contém duas distribuições do mesmo método, não dois sistemas de agentes em execução.

- `codex/skills/khanato` mantém o núcleo para Codex; `claude` mantém o plugin adaptado. Mudança comum deve ser refletida na outra distribuição; não apague diferenças reais de ferramentas ou autoridade.
- Leia `docs/CODEBASE_MAP.md` e confira o estado real, incluindo arquivos staged, unstaged e novos. Aplique Cartographer conforme o adaptador canônico do Khanato, com leitura e revisão proporcionais.
- Respeite instruções superiores, permissões, pedido direto e regras locais. Preserve PostgreSQL, 5FN, identificadores descritivos em inglês e PK UUID v4 nos sistemas abrangidos pela Constituição; exceções somente por escrito do Imperador.
- Execute `python -B scripts/verify.py`; depois de mudar fontes, regenere pacotes com `python -B scripts/build_packages.py` e confira `python -B scripts/verify.py --packages`. Testes de auxiliares não comprovam comportamento no aplicativo.
- Nunca versionar credenciais, `.env` real, perfis de autenticação, cofre, conversas, logs de clientes ou cópias de outros projetos. `.local/` e `docs/obsidian-pending/` ficam fora da publicação. Dados das avaliações são sintéticos.
- Não mude visibilidade, permissões, licença de redistribuição ou configurações de conta como consequência de uma alteração de instruções. Não instale hooks, serviços ou rotinas de sincronização por conveniência.

## Registro no Obsidian (quando adotado)

Esta é uma tarefa transversal. Quando o ambiente adotar um cofre Obsidian como registro, antes de editar leia o `AGENTS.md` da raiz da organização e a política de atualização dos projetos do cofre, quando acessíveis. Ao entregar alterações, atualize a ficha e crie uma nota de alteração com identificador único, motivo, fontes, verificações reais, pendências e links na pasta compartilhada do Khanato no cofre canônico.

Use os modelos do cofre, releia arquivos compartilhados antes de salvar, preserve histórico e mudanças concorrentes. Mantenha código e documentação técnica aqui; não copie segredos para notas. Se o cofre estiver inacessível ou sem permissão, prepare `docs/obsidian-pending/` no projeto, informe destino e pendência, sem declarar incorporação ou sincronização. A coordenação consolida o trabalho dos subagentes. A regra não cria monitoramento em segundo plano.
