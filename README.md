
## Escolha seu idioma
<div style="text-align: center;">

[Transcrições originais :uk:](https://github.com/IaKee/Runelingual-Transcripts/tree/original-main) | [Español Argentino :argentina:](https://github.com/IaKee/Runelingual-Transcripts/tree/espanol-argentino-main) | **Português Brasileiro :brazil:** | [Norsk :norway:](https://github.com/IaKee/Runelingual-Transcripts/tree/norsk-main)

</div>

- Estes são os idiomas com os quais estamos trabalhando e damos suporte até o momento.
- Se você gostaria de contribuir, ou solicitar suporte para outro idioma que não está listado aí encima, por favor [entre em contato conosco](#entre-em-contato).
- Sinta-se à vontade para ajustar nossos pacotes de idiomas de acordo com sua preferência. Nosso objetivo é apoiar múltiplas variantes de pacotes de idiomas para acomodar diferentes preferências.

# Transcrições do RuneLingual

Bem-vindo ao repositório de transcrições do [plugin de tradução RuneLingual](https://github.com/IaKee/RuneLingual-Plugin)! Este repositório tem como objetivo ser um centro de contribuição, com tudo relacionado aos arquivos fonte utilizados no plugin principal.

RuneLingual é um plugin feito e mantido pela comunidade para o cliente RuneLite, que é [oficialmente suportado](https://secure.runescape.com/m=news/third-party-clients-update?oldschool=1) para [OldSchool RuneScape](https://oldschool.runescape.com), você pode ler mais sobre eles nos links aqui.

Nosso objetivo é unir a comunidade fornecendo traduções acessíveis em vários idiomas, garantindo que cada jogador possa desfrutar do jogo em seu idioma preferido.

[Contribuições são muito bem vindas!]()

## Perguntas Frequentes

### O que são essas transcrições?
Arquivos fontes das transcrições são arquivos contendo o texto usado no jogo.
Cada arquivo representa um aspecto diferente do jogo, como diálogos de NPC, descrições de itens e o conteúdo das diversas interfaces diferentes.

Eles são tipicamente armazenados em [formato JSON](https://pt.wikipedia.org/wiki/JSON), que é basicamente uma [string de texto simples](https://pt.wikipedia.org/wiki/Cadeia_de_caracteres) com um monte de símbolos extras [mapeando cada string original para um novo valor](https://pt.wikipedia.org/wiki/Tabela_de_dispersão), esse formato torna mais fácil para o computador do usuário ler e modificá-los.

A maioria das transcrições deve se parecer com algo assim:

<div style="text-align: center;">

```json
{
    "itemexamine": {
        "arazorsharpsword": "Uma espada bem afiada.",
        "arrowswithbronzeheads": "Flechas com pontas de bronze.",
        "shortbuteffective": "Curto, mas eficiente."
    },
    "welcomemessage": {
        "welcometooldschoolrunescape": "Boas vindas a OldSchool RuneScape!"
    }
}
```

</div>

### Como o plugin utiliza essas transcrições?

Quando qualquer objeto contendo uma string de texto é lido do jogo, seu nome é convertido para caracteres minúsculos, tem seus espaços e pontuações removidos e então pode ser usado como a chave de pesquisa (a string no início de cada linha no exemplo anterior).

Como exemplo, no jogo original em ingles, se tivermos uma espada de bronze em nosso inventário e a exarminarmos, o jogo nos mostra a frase:

> "A razor sharp sword."

Então esse texto passa por esse processamento inicial que descrevemos, e a nova chave deverá ser:

> "arazorsharpsword"

O plugin então usa esta chave para pesquisar através de seus arquivos de transcrição, entre muitas categorias de objetos diferentes, para verificar se há uma tradução correspondente para o objeto atual, [como no exemplo anterior](#o-que-são-essas-transcrições), para o português brasileiro vamos encontrar uma string correspondente como:

> "Uma espada bem afiada."

A nova string é então enviada para o widget original, substituindo o texto original antes mesmo de ser mostrado ao jogador, para que eles possam experimentar o jogo como se estivesse realmente em português brasileiro!

### Como posso contribuir?

Se você gostaria de contribuir de alguma forma, por favor, considere os itens abaixo:

- Junte-se ao nosso [servidor da comunidade no Discord](https://discord.gg/ehwKcVdBGS) para ficar por dentro do que está acontecendo com o projeto, como metas, atualizações de desenvolvimento e para entrar em contato com a gente.
- [Verifique a aba de issues do projeto](https://github.com/IaKee/Runelingual-Transcripts/issues) para tarefas em andamento e planejadas, sugestões e novas ideias, sinta-se à vontade para contribuir com as suas próprias.

Se você quiser contribuir melhorando qualquer um dos nossos pacotes de tradução, siga estes passos:
1. [Selecione o idioma que voce quer trabalhar no topo desta página](#escolha-seu-idioma-preferido), para acessar seu branch correspondente.
> **NOTA**: É importante observar que cada pacote de idioma deve ter seu próprio branch, assim também como dois outros sub-branches:
main - o branch principal para o pacote de idioma dado, onde a versão mais recente estável usada no plugin principal é armazenada.
dev - o branch de desenvolvimento, onde a versão mais recente e instável das transcrições é armazenada.

2. [Crie seu próprio fork](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) do branch de desenvolvimento do pacote de idioma com o qual você pretende trabalhar.
3. Ajuste sua versão de acordo com suas preferências.
4. [Envie um pull request com suas alterações](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
5. Aguarde para que suas alterações possam ser revisadas e [mescladas com o branch principal](https://docs.github.com/pt/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github).

Se você gostaria de ver seu idioma sendo suportado, mas sente que atualmente não pode contribuir, por favor, considere entrar em contato com seus amigos e colegas de clã compartilhando este projeto!

Até o momento, ainda não temos uma ferramenta de tradução para recomendar aos contribuidores, após o processamento inicial de dados brutos, o trabalho é feito manualmente na sua maioria.

> Até o momento, recomendo muito o uso do [Visual Studio Code](https://code.visualstudio.com) (que é basicamente um editor de texto como o [bloco de notas do Windows](https://pt.wikipedia.org/wiki/Bloco_de_Notas), com ferramentas extras para programação) com [tela dividida](https://stackoverflow.com/questions/40709351/visual-studio-code-how-to-split-the-editor-vertically) juntamente com a extensão [Sync Scroll](https://marketplace.visualstudio.com/items?itemName=dqisme.sync-scroll), para que seu workspace possa ficar assim:
![preview](https://i.imgur.com/mMJt8jZ.png)
A extensão de rolagem Sync Scroll vai garantir que os dois editores estejam sincronizados, para que você possa rolar pelo código e o editor de texto rolará com você, lado a lado, mostrando as entradas correspondentes no outro editor.

## Aviso Legal

Este repositório faz parte do projeto RuneLingual, um plugin de terceiros, de codigo aberto, e ainda em desenvolvimento. Não é afiliado à Jagex, os criadores do OldSchool RuneScape, ou RuneLite e seus criadores.

## Entre em Contato

Se você tiver alguma dúvida, sugestão, feedback ou qualquer outra coisa, sinta-se à vontade para entrar em contato em [nosso servidor Discord](https://discord.gg/ehwKcVdBGS) e por favor, [confira a aba de issues](https://github.com/IaKee/Runelingual-Transcripts/issues) deste projeto para quaisquer sugestões, perguntas ou até reclamações.