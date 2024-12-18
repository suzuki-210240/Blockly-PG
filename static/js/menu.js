document.addEventListener('DOMContentLoaded', function () {
  const userMenu = document.getElementById('userMenu');
  
  // userMenuが存在する場合のみイベントリスナーを追加
  if (userMenu) {
    userMenu.addEventListener('change', function (event) {
      const selectedValue = event.target.value; // 選択された値を取得
      if (selectedValue !== 'username') {
        // 任意の処理を書くことができます
      }
      // 常に「ユーザー名」に戻す
      event.target.value = 'username'; 
    });
  }

  // iframeサイズ調整の処理
  const iframe = document.querySelector('.preview'); // iframeのクラス名を指定
  
  if (iframe) {
    // リサイズ時にiframeのサイズを変更
    window.addEventListener('resize', function () {
      const aspectRatio = 16 / 9; // 16:9のアスペクト比
      iframe.style.width = window.innerWidth * 0.9 + 'px'; // 画面幅の90%
      iframe.style.height = (window.innerWidth * 0.9) / aspectRatio + 'px'; // 高さを計算
    });

    // 初期サイズの設定
    const aspectRatio = 16 / 9;
    iframe.style.width = window.innerWidth * 0.9 + 'px'; // 初期幅
    iframe.style.height = (window.innerWidth * 0.9) / aspectRatio + 'px'; // 初期高さ
  }
});
