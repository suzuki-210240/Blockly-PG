document.getElementById('userMenu').addEventListener('change', function (event) {
    const selectedValue = event.target.value; // 選択された値を取得
    if (selectedValue !== 'username') {
    }
    // 常に「ユーザー名」に戻す
    event.target.value = 'username'; 
  });