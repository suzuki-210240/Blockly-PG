//-------------自由制作用javascript------------------

// Blockly で作成されたコードを実行する関数
function runCode() {
    var code = Blockly.JavaScript.workspaceToCode(workspace);
    try {
        // eval を使ってコードを実行し、結果を表示
        var result = eval(code);
        // 結果を表示
        document.getElementById('output').innerText = result;
    } catch (e) {
        // エラーが発生した場合
        document.getElementById('output').innerText = "エラー: " + e.message;
    }
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
    // Blockly ワークスペースの内容を XML としてエクスポート
    var xml = Blockly.Xml.workspaceToDom(workspace);
    var xmlText = Blockly.Xml.domToText(xml);

    // XML テキストを Blob に変換
    var blob = new Blob([xmlText], { type: 'application/xml' });

    // ダウンロードリンクを作成してクリック
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
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
    // 生成されたコードを表示する
    document.getElementById('codeOutput').value = code;
} else {
    console.error('workspaceが未定義です。');
    alert('Blocklyワークスペースが正しく初期化されていません。');
}
}