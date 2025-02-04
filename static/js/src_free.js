/**
 * This project uses Blockly, an open-source visual programming editor developed by Google.
 * 
 * Blockly is licensed under the Apache License, Version 2.0.
 * See: http://www.apache.org/licenses/LICENSE-2.0
 */


//-------------自由制作用javascript------------------
 var flg = 0;
// Blockly で作成されたコードを実行する関数
/*function runCode() {
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
}*/

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

function clearConsole() {
    document.getElementById('output').innerHTML = '--------ここに結果出力されます-------- '; // 出力エリアを空にする
    flg = 0;
}

// function runText() {
//     var code = Blockly.JavaScript.workspaceToCode(workspace);
//     var output = '';
//     try {
//         // eval を使ってコードを実行し、結果を表示
//         output = eval(code);
//     } catch (e) {
//         // エラーが発生した場合
//         output = "エラー: " + e.message;
//     }

//     document.getElementById('output').textContent = output;
// }



// ワークスペースを XML として保存する関数
function saveWorkspaceAsXML() {
    // ユーザーにファイル名を入力させるダイアログを表示
    var fileName = prompt("保存するファイル名を入力してください:", "workspace");

    // ユーザーが入力しなかった場合はデフォルト名を使用
    if (!fileName) {
        fileName = "workspace";
    }

    // Blockly ワークスペースの内容を XML としてエクスポート
    var xml = Blockly.Xml.workspaceToDom(workspace);
    var xmlText = Blockly.Xml.domToText(xml);

    // XML テキストを Blob に変換
    var blob = new Blob([xmlText], { type: 'application/xml' });

    // ダウンロードリンクを作成してクリック
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = fileName + ".xml";  // ユーザーが指定したファイル名
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
    // 生成されたコードを表示する
    document.getElementById('codeOutput2').value = code;
} else {
    console.error('workspaceが未定義です。');
    alert('Blocklyワークスペースが正しく初期化されていません。');
}
}

function comment(event) {
    // コメントを追加する
    const tutorialSteps = [
        { text: "これが最初のステップです。", x: 50, y: 100 },
        { text: "次はここを確認してください。", x: 200, y: 150 },
        { text: "最後にこの部分をチェックします。", x: 350, y: 250 },
      ];
  
      let currentStep = 0;
  
      // チュートリアルボタンがクリックされたときの動作
      document.getElementById("tutorialButton").addEventListener("click", () => {
        const tutorialComment = document.getElementById("tutorialComment");
  
        if (currentStep < tutorialSteps.length) {
          const step = tutorialSteps[currentStep];
  
          // コメントの位置と内容を設定
          tutorialComment.style.left = step.x + "px";
          tutorialComment.style.top = step.y + "px";
          tutorialComment.innerHTML = step.text;
          tutorialComment.style.display = "block"; // 表示する
  
          currentStep++;
        } else {
          // チュートリアルが終了したら非表示に戻す
          tutorialComment.style.display = "none";
          currentStep = 0; // リセットする
        }
      });
}