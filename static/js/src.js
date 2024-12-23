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

function clearConsole() {
    document.getElementById('output').innerHTML = '--------ここに結果出力されます-------- '; // 出力エリアを空にする
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
    file_name = ''+'.xml'
    link.download = 'workspace.xml';  // ダウンロードするファイル名
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




function generateCode(event){
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
                alert("正解です！");
            } else {
                alert("不正解です。");
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