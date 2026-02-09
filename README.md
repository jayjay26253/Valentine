<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Will You Be My Valentine?</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
    body {
        margin: 0;
        height: 100vh;
        font-family: Arial, sans-serif;
        background: linear-gradient(to bottom, #d9b6ff, #ffd6c9);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        width: 90%;
        max-width: 350px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    h2 {
        color: #555;
        margin-bottom: 8px;
    }

    h1 {
        color: #ff4f9a;
        margin-bottom: 15px;
        font-size: 24px;
    }

    p {
        color: #666;
        font-size: 14px;
    }

    .buttons {
        margin-top: 30px;
        position: relative;
        height: 140px;
    }

    button {
        padding: 14px 26px;
        border: none;
        border-radius: 30px;
        font-size: 16px;
        cursor: pointer;
        position: absolute;
    }

    #yesBtn {
        background: linear-gradient(to right, #ff5fa2, #ff87c2);
        color: white;
        left: 50%;
        transform: translateX(-50%);
    }

    #noBtn {
        background: white;
        color: #555;
        border: 1px solid #ccc;
        top: 70px;
        left: 50%;
        transform: translateX(-50%);
    }
</style>
</head>

<body>

<div class="card">
    <h2>Dear Hala,</h2>
    <h1>Will you be my Valentine?</h1>

    <p>
        I promise I would never leave you,<br>
        you’re the perfect girl in my eyes 💋
    </p>

    <p><strong>– Yousef</strong></p>

    <div class="buttons">
        <button id="yesBtn" onclick="yesClicked()">Yes ❤️</button>
        <button id="noBtn">No</button>
    </div>
</div>

<script>
    const noBtn = document.getElementById("noBtn");

    function moveButton() {
        const x = Math.random() * 200 - 100;
        const y = Math.random() * 100 - 50;
        noBtn.style.transform = `translate(${x}px, ${y}px)`;
    }

    noBtn.addEventListener("mouseenter", moveButton);
    noBtn.addEventListener("touchstart", moveButton);

    function yesClicked() {
        document.body.innerHTML = `
            <div style="
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                flex-direction:column;
                background:linear-gradient(to bottom, #ffb6e6, #ffd6c9);
                font-family:Arial;
                text-align:center;
            ">
                <h1 style="color:#ff4f9a;">YAY 💖💖💖</h1>
                <p style="font-size:18px;">Best Valentine ever 🥰</p>
            </div>
        `;
    }
</script>

</body>
</html>
