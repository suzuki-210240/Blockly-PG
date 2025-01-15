/**
 * This project uses Blockly, an open-source visual programming editor developed by Google.
 * 
 * Blockly is licensed under the Apache License, Version 2.0.
 * See: http://www.apache.org/licenses/LICENSE-2.0
 */


//-------------課題制作用javascript------------------
var flg = 0;
// Blockly で作成されたコードを実行する関数
function runCode() {
    var code = Blockly.JavaScript.workspaceToCode(workspace); // Blocklyからコードを取得
   
    try {
        // eval を使ってコードを実行し、結果を表示
        var result = eval(code);
        // 結果を表示

        const output = document.getElementById('output');
        const resultElement = document.createElement('span'); // 新しい行を作成
        if  (flg == 0) {
            resultElement.innerText = "\n" +"結果: " + result + "\n";
            flg = 1;
        }else{
            resultElement.innerText = "結果: " + result + "\n";
        }
        
        output.appendChild(resultElement); // 結果を追加

        // 自動スクロール
        output.scrollTop = output.scrollHeight;
    } catch (e) {
        // エラーが発生した場合
        const output = document.getElementById('output');
        const errorElement = document.createElement('span');
        errorElement.innerText = "エラー: " + e.message;
        output.appendChild(errorElement); // エラーメッセージを追加
        output.scrollTop = output.scrollHeight;
    }
}


function change(mode_id){
    const modes = document.querySelectorAll('.mode');
    modes.forEach(mode => mode.classList.remove('active'));
    const show = document.getElementById(mode_id);
    if (show){
        show.classList.add('active');
    }
}

window.onload = function() {
    change('mode1');
}


function clearConsole() {
    document.getElementById('output').innerHTML = '--------ここに結果出力されます-------- '; // 出力エリアを空にする
    flg = 0;
}


// ワークスペースを XML として保存する関数
function saveWorkspaceAsXML() {
    // Blockly ワークスペースの内容を XML としてエクスポート
    var xml = Blockly.Xml.workspaceToDom(workspace);
    var xmlText = Blockly.Xml.domToText(xml);

    // XML テキストを Blob に変換
    var blob = new Blob([xmlText], { type: 'application/xml' });

    // ダウンロードリンクを作成してクリック
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    file_name = kadaiId +'.xml'
    link.download = file_name;  // ダウンロードするファイル名
    link.click();
}


// XML ファイルを読み込んでワークスペースに展開する関数
function loadWorkspaceFromXML(event) {
    // 選択されたファイルを取得
    var file = event.target.files[0];
    if (!file) {
        console.error("ファイルが選択されていません！");
        return;
    }
    console.log(Blockly.Xml);  // これで Blockly.Xml が存在するか確認

    // FileReader でファイルを読み込む
    var reader = new FileReader();
    reader.onload = function(e) {
        // 読み込んだ XML テキスト
        var xmlText = e.target.result;

        // デバッグ: XML テキストをコンソールに表示
        console.log("読み込んだ XML: ", xmlText);

        try {
            // 修正後：Blockly.Xml.parse を使う
            // const parser = new DOMParser();
            // var xmlDom = parser.parseFromString(xmlText, 'application/xml');
            var xmlDom = Blockly.utils.xml.textToDom(xmlText); //xmlファイルをDOMに変換
            Blockly.Xml.clearWorkspaceAndLoadFromXml(xmlDom, workspace); //現在のワークスペースの内容を削除してXMLDOMの内容を展開
        } catch (error) {
            console.error("XML 読み込みエラー: ", error);
            alert("XML の読み込みに失敗しました。");
        }
    };

    // ファイルを読み込む
    reader.readAsText(file);
}




function checkCode(event){
    // workspaceが未定義でないことを確認
    if (typeof workspace !== 'undefined' && workspace !== null) {
        // BlocklyのワークスペースからPythonコードを生成
        var code = python.pythonGenerator.workspaceToCode(workspace);

        // サーバーにPythonコードを送信して一致を確認
        fetch('/user/check-code/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // CSRFトークンを追加
            },
            body: JSON.stringify({ code: code ,kadai_id:kadaiId})
        })
        .then(response => response.json())
        .then(data => {
            if (data.isCorrect) {
                displayCorrectOverlay(); // 正解時の処理
            } else {
                displayIncorrectOverlay(); // 不正解時の処理
            }
        })
        .catch(error => {
            console.error("エラーが発生しました:", error);
        });
    } else {
        console.error('workspaceが未定義です。');
        alert('Blocklyワークスペースが正しく初期化されていません。');
    }
}


// 正解時のオーバーレイ表示
function displayCorrectOverlay() {
    const overlay = document.getElementById("overlay");
    overlay.style.display = "block";
    overlay.innerHTML = `
        <h1 style="color: red; font-size: 48px;">正解！</h1>
        <a href="{% url 'UserApp:index' %}" style="display: inline-block; margin-top: 20px; font-size: 20px; color: white; background: red; padding: 10px; text-decoration: none; border-radius: 5px;">戻る</a>
    `;
    startConfetti(); // 花吹雪を開始
}

// 不正解時のオーバーレイ表示
function displayIncorrectOverlay() {
    const overlay = document.getElementById("overlay");
    overlay.style.display = "block";
    overlay.innerHTML = `<h1 style="color: blue;">不正解</h1>`;
    setTimeout(() => {
        overlay.style.display = "none"; // 1秒後にオーバーレイを非表示
    }, 1000);

    // クリックで非表示
    overlay.onclick = () => {
        overlay.style.display = "none";
    };
}

// 花吹雪の処理（変わらず）
function startConfetti() {
    const confettiContainer = document.getElementById("confetti-container");

    let confettiInterval = setInterval(() => {
        const confetti = document.createElement("div");
        confetti.style.position = "absolute";
        confetti.style.width = "10px";
        confetti.style.height = "10px";
        confetti.style.backgroundColor = getRandomColor();
        confetti.style.left = Math.random() * window.innerWidth + "px";
        confetti.style.bottom = "0";
        confetti.style.animation = "fall 3s linear";

        confettiContainer.appendChild(confetti);

        setTimeout(() => {
            confetti.remove();
        }, 3000);
    }, 50);

    setTimeout(() => {
        clearInterval(confettiInterval);
    }, 5000);
}

// ランダムな色を生成
function getRandomColor() {
    const colors = ["#FF5733", "#33FF57", "#5733FF", "#FFFF33", "#33FFFF", "#FF33FF"];
    return colors[Math.floor(Math.random() * colors.length)];
}