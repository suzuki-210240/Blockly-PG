document.addEventListener('DOMContentLoaded', function () {
  // タイトル入力の表示/非表示
  const titleChoiceRadios = document.getElementsByName('title-choice');
  const newTitleBox = document.querySelector('.new-title-box');
  const newTitleInput = document.getElementById('new-title');
  
  function toggleTitleBox() {
    // radio == yes の状態
    const isTitleChange = Array.from(titleChoiceRadios).some(radio => radio.value === 'yes' && radio.checked);
    
    if (newTitleBox) {
      // "する" の場合はタイトル入力ボックスを表示、それ以外は非表示
      newTitleBox.style.display = isTitleChange ? 'block' : 'none';
    }

    // "しない"の場合はタイトルボックスにデフォルトメッセージを設定
    if (newTitleInput) {
      if (isTitleChange) {
        newTitleInput.value = "";
      } else {
        newTitleInput.value = "タイトルは変更しません";
      }
    }
  }

  // 初期表示の状態を設定
  toggleTitleBox();

  // ラジオボタンの変更時に toggleTitleBox を呼び出す
  titleChoiceRadios.forEach(radio => {
    radio.addEventListener('change', toggleTitleBox);
  });



  // ファイル選択の表示/非表示　 ファイルのPOST送信無効化/有効化
  const fileChoiceRadios = document.getElementsByName('file-choice');
  const fileInput = document.getElementById('file');

  function toggleFileInput() {
    if (fileInput) {
      // "しない" の場合に fileInput を非表示
      const fileisChecked = Array.from(fileChoiceRadios).some(radio => radio.value === 'yes' && radio.checked);
      fileInput.style.display = fileisChecked ? 'inline-block' : 'none';

      // "しない" の場合、ファイル選択を無効化し、フォーム送信時にエラーが出ないように設定
      if (!fileisChecked) {
        fileInput.disabled = true; // 入力を無効化
        fileInput.required = false; // ファイルが選ばれていなくてもエラーが出ないようにする
      } else {
        fileInput.disabled = false; // 入力を有効化
        fileInput.required = true;  // ファイルが必須になる
      }
    }
  }

  // 初期表示の状態を設定
  toggleFileInput();

  // ラジオボタンの変更時に toggleFileInput を呼び出す
  fileChoiceRadios.forEach(radio => {
    radio.addEventListener('change', toggleFileInput);
  });
});
