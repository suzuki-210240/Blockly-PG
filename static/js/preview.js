document.addEventListener('DOMContentLoaded', function () {
    // ファイルのプレビュー表示
    document.getElementById('file').addEventListener('change', function (event) {
        const file = event.target.files[0]; // ファイルを取得
        if (file) {
            const reader = new FileReader(); // FileReaderを作成
            reader.onload = function (e) {
                const iframe = document.getElementById('preview');
                const blob = new Blob([e.target.result], { type: 'text/html' }); // Blobに変換
                const url = URL.createObjectURL(blob); // BlobのURLを生成
                iframe.src = url; // iframeのsrcにURLを設定
            };
            reader.readAsText(file); // ファイルをテキストとして読み取る
        }
    });
});
