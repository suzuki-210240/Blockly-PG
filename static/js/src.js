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
    const output = document.getElementById('output');
    output.innerHTML = ""; // 実行ごとにクリア

    try {
        // console.log の出力を `output` に反映
        let oldLog = console.log;
        console.log = function (message) {
            const resultElement = document.createElement('span');
            resultElement.innerText = "結果: " + message + "\n";
            output.appendChild(resultElement);
            output.scrollTop = output.scrollHeight;
            oldLog.apply(console, arguments); // 元の console.log も実行
        };

        // `alert()` を `console.log()` に変換
        code = code.replace(/alert\(/g, "console.log(");

        // eval でコード実行
        eval(code);

        // console.log を元に戻す
        console.log = oldLog;
    } catch (e) {
        // エラー時の処理
        const errorElement = document.createElement('span');
        errorElement.style.color = "red";
        errorElement.innerText = "エラー: " + e.message;
        output.appendChild(errorElement);
        output.scrollTop = output.scrollHeight;
    }
}


function change(mode_id,tab_id){
    const modes = document.querySelectorAll('.mode');
    modes.forEach(mode => mode.classList.remove('active'));
    const show = document.getElementById(mode_id);
    if (show){
        show.classList.add('active');
    }
    const tabs = document.querySelectorAll('.tab h4 a');
    tabs.forEach(tab => tab.classList.remove('active-tab'));
    const activeTab = document.getElementById(tab_id);
    if (activeTab) {
        activeTab.classList.add('active-tab');
    }
}

window.onload = function() {
    change('mode1','tab-mode1');
}


function clearConsole() {
    document.getElementById('output').innerHTML = '--------ここに結果出力されます-------- '; // 出力エリアを空にする
    flg = 0;
}

function generateCode(event){
    // workspaceが未定義でないことを確認
if (typeof workspace !== 'undefined' && workspace !== null) {
    // BlocklyのワークスペースからPythonコードを生成
    var code = python.pythonGenerator.workspaceToCode(workspace);
    // 生成されたコードを表示する
    document.getElementById('codeOutput').value = code;
} else {
    console.error('workspaceが未定義です。');
    alert('Blocklyワークスペースが正しく初期化されていません。');
}
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
    startConfetti(); // 花吹雪を開始

    setTimeout(() => {
        const overlay = document.getElementById("overlay");
        const returnUrl = document.body.getAttribute("data-return-url");
        overlay.style.display = "block";
        overlay.innerHTML = `
        <h1 style="color: red; font-size: 48px;">正解！</h1>
        <a href="${returnUrl}" style="display: inline-block; margin-top: 20px; font-size: 20px; color: white; background: red; padding: 10px; text-decoration: none; border-radius: 5px;">戻る</a>
    `;
    },500);
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

function startConfetti() {
    const duration = 2.5 * 1000; // 紙吹雪を表示する時間（5秒）
    const end = Date.now() + duration;

    // 紙吹雪のループを作成
    (function frame() {
        confetti({
            particleCount: 3,
            angle: 60,
            spread: 55,
            origin: { x: 0 }, // 左から紙吹雪を発生
        });
        confetti({
            particleCount: 3,
            angle: 120,
            spread: 55,
            origin: { x: 1 }, // 右から紙吹雪を発生
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    })();
}
