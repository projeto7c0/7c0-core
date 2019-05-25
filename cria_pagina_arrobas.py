def adiciona_tweet (html, timestamp, plaintext, id):
    item = """<li><p>Data do tweet: <!--timestamp--></p><p><!--plain_text--></p><a href='<!--id-->.html'><p>id: <!--id--></p></a></li><!--item-->"""
    item = item.replace("<!--timestamp-->", timestamp)
    item = item.replace("<!--plain_text-->", plaintext)
    item = item.replace("<!--id-->", str(id))

    html = html.replace("<!--item-->", item)

    return html



def cria(arroba, html):
    print("Criando arquivo...")
    f = open(r'/home/ec2-user/projeto7c0.github.io/politicians/'+arroba+"/index.html", "w+")
    f.write(html)
    f.close()


if __name__ == '__main__':
    import database, contas, os

    arrobas = contas.pega_contas()

    for arroba in arrobas:
        html = """<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <meta name="description" content="Website do Projeto 7C0.">
    <meta name="keywords" content="Projeto 7C0, monitoramento, políticos, atores públicos">
    <link rel="icon" type="image/x-icon" href="./img/eye.ico" />
    <title>Projeto 7C0 | <!--arroba--> | Tweets que sumiram</title>
    <link rel="stylesheet" href="../../css/style.css">
    <script type="text/javascript" src="../../js/scripts.js"></script>
</head>

<body>

    <header>
        <div class="container">
            <div id="branding">
                <h1>
                    Projeto 7C0 | <!--arroba--> | Tweets que sumiram
                </h1>
            </div>
            <nav>
                <ul>
                    <li><a href="../../index.html">Home</a></li>
                    <li><a href="../../about.html">Sobre</a></li>
                    <li><a href="../../source.html">Código-Fonte</a></li>
					<li class="current"><a href="../../politicians">Políticos</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="main">
        <div class="container">
            <article id="main-col-single">
				<h2>Tweets apagados</h2>
                <ul id="services">
                    <!--item-->
                </ul>
            </article>
        </div>
        </div>
    </section>

    <section id="newsletter">
        <div class="container">

            <h3>Receba atualizações do projeto &nbsp;</h3>
            <form action="https://projeto7c0.us20.list-manage.com/subscribe/post?u=984470f280d60b82c247e3d7b&amp;id=00a31b0d4a"
                method="post" target="_blank" novalidate>
                <input class="button_1" type="submit" value="Inscreva-se" name="subscribe">
            </form>
        </div>
    </section>

    <footer>
        <p>Projeto 7C0, Copyright &copy; 2019</p>
    </footer>

</body>

</html>

<!-- Browser Sync -->
<!-- 
    You can sync this code using VSCode Browser Sync by typing "Server mode in browser" and then
    chosing the following files to be sync "*.html|./css/*.css".
-->"""

        html = html.replace("<!--arroba-->", arroba)
        print(arroba)
        lista = database.list_apagados_novo(arroba)
        os.makedirs(arroba, exist_ok=True)

        for tweet in lista:
            html = adiciona_tweet(html, tweet[2], tweet[1], tweet[0])

        cria(arroba, html)


