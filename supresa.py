from flask import Flask, render_template_string

app = Flask(__name__)

PAGINA = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Uma surpresa para Raquel ❤️</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    background: linear-gradient(135deg, #ffb6d5, #ff75ae, #f7a5d0);
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow-x: hidden;
    color: #74304e;
    padding: 20px;
}

.container {
    width: 100%;
    max-width: 450px;
    text-align: center;
    padding: 30px 20px;
    background: rgba(255,255,255,0.75);
    border-radius: 25px;
    box-shadow: 0 10px 40px rgba(150, 30, 90, 0.2);
    position: relative;
    z-index: 2;
}

h1 {
    font-size: 27px;
    margin-bottom: 15px;
}

.subtitle {
    margin-bottom: 35px;
    font-size: 15px;
}

.gift {
    width: 170px;
    height: 130px;
    margin: 65px auto 45px;
    position: relative;
    cursor: pointer;
    perspective: 600px;
}

.box {
    width: 170px;
    height: 110px;
    position: absolute;
    bottom: 0;
    background: #ed4086;
    border-radius: 8px;
    box-shadow: 0 8px 15px rgba(0,0,0,0.15);
}

.box::before {
    content: "";
    position: absolute;
    width: 28px;
    height: 100%;
    background: #ffe1ec;
    left: 71px;
}

.lid {
    position: absolute;
    width: 190px;
    height: 35px;
    background: #ff5b9b;
    left: -10px;
    top: -15px;
    border-radius: 7px;
    transform-origin: left bottom;
    transition: transform 1s ease;
    z-index: 3;
}

.lid::before {
    content: "";
    position: absolute;
    width: 28px;
    height: 100%;
    background: #ffe1ec;
    left: 81px;
}

.ribbon {
    position: absolute;
    width: 65px;
    height: 65px;
    border: 10px solid #ffdfeb;
    border-radius: 50%;
    top: -65px;
    left: 53px;
    z-index: 4;
}

.gift.open .lid {
    transform: rotate(-115deg) translateY(-10px);
}

.gift.open .ribbon {
    transform: translateY(-25px);
    transition: 0.8s;
}

.hint {
    font-size: 14px;
    margin-bottom: 25px;
    animation: pulse 1.5s infinite;
}

button {
    border: none;
    background: #e83e83;
    color: white;
    padding: 14px 25px;
    border-radius: 30px;
    font-size: 15px;
    cursor: pointer;
    margin-top: 15px;
    transition: 0.3s;
}

button:hover {
    background: #c92869;
    transform: scale(1.05);
}

.letter {
    display: none;
    margin-top: 30px;
    padding: 22px;
    background: #fff0f6;
    border-radius: 18px;
    line-height: 1.8;
    text-align: left;
    animation: appear 1s ease;
}

.letter h2 {
    text-align: center;
    margin-bottom: 18px;
    color: #d93679;
}

.declaration {
    display: none;
    margin-top: 20px;
    font-size: 23px;
    font-weight: bold;
    color: #d93679;
    text-align: center;
    animation: appear 1s ease;
}

.heart {
    position: fixed;
    bottom: -30px;
    font-size: 22px;
    animation: float 6s linear forwards;
    pointer-events: none;
    z-index: 1;
}

@keyframes float {
    to {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0;
    }
}

@keyframes pulse {
    50% { opacity: 0.4; }
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
</head>

<body>

<div class="container">

    <h1>Uma surpresa para você ❤️</h1>

    <p class="subtitle">
        Preparei uma coisinha especial...
    </p>

    <div class="gift" id="gift" onclick="abrirPresente()">
        <div class="ribbon"></div>
        <div class="box"></div>
        <div class="lid"></div>
    </div>

    <p class="hint" id="hint">
        Toque na caixinha para abrir seu presente 🎁
    </p>

    <div class="letter" id="letter">

        <h2>Para minha Raquel ❤️</h2>

        <p>
            Meu amor, talvez isso seja apenas uma pequena
            surpresa na tela do seu celular, mas foi feito
            pensando em você.
        </p>

        <br>

        <p>
            Quero que você saiba o quanto é especial na minha
            vida. Sou grato a Deus por ter colocado você no
            meu caminho e por cada momento que podemos
            compartilhar.
        </p>

        <br>

        <p>
            Não quero apenas estar ao seu lado nos momentos
            bons. Quero construir uma história com você,
            enfrentar os desafios, realizar nossos sonhos
            e continuar escolhendo você todos os dias.
        </p>

        <br>

        <p>
            Espero conseguir fazer você feliz e ser alguém
            com quem você sempre possa contar.
        </p>

        <br>

        <p style="text-align:center;">
            Com todo meu amor,
            <br>
            <strong>Seu João ❤️</strong>
        </p>

        <button onclick="mostrarDeclaracao()">
            Tenho mais uma coisa pra te dizer...
        </button>

        <div class="declaration" id="declaration">
            EU TE AMO, RAQUEL! ❤️
        </div>

    </div>

</div>

<script>
let aberto = false;

function abrirPresente() {
    if (aberto) return;

    aberto = true;

    document.getElementById("gift").classList.add("open");

    document.getElementById("hint").innerText =
        "Seu presente está aqui, meu amor ❤️";

    criarCoracoes();

    setTimeout(() => {
        document.getElementById("letter").style.display = "block";
        document.getElementById("hint").style.display = "none";
    }, 1000);
}

function mostrarDeclaracao() {
    document.getElementById("declaration").style.display = "block";
    criarCoracoes();
}

function criarCoracoes() {
    for (let i = 0; i < 20; i++) {
        setTimeout(() => {
            const heart = document.createElement("div");

            heart.className = "heart";
            heart.innerHTML = Math.random() > 0.5 ? "❤️" : "💕";

            heart.style.left = Math.random() * 100 + "vw";
            heart.style.animationDuration = (3 + Math.random() * 4) + "s";

            document.body.appendChild(heart);

            setTimeout(() => heart.remove(), 7000);

        }, i * 120);
    }
}

setInterval(() => {
    const heart = document.createElement("div");

    heart.className = "heart";
    heart.innerHTML = "❤️";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = "6s";

    document.body.appendChild(heart);

    setTimeout(() => heart.remove(), 6000);
}, 1500);
</script>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(PAGINA)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)