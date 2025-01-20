document.addEventListener('DOMContentLoaded', function () {
  const addButton = document.querySelector('.add-button');
  const addImgButton = document.getElementById('add-img');
  const imgBox = document.getElementById('img-box');
  const backButton = document.querySelector('.back-button');

  if (!addImgButton) {
    console.error('add-imgボタンが見つかりません');
  } else {
    console.log('add-imgボタンが見つかりました');
    

    if(addButton){
      addButton.addEventListener('click', function () {
        let imgBoxForm = document.querySelector('.img-box');

        // img-boxフォームを表示
        imgBoxForm.style.display = 'block';
        this.style.display = 'none'; // 追加ボタンを非表示
      });
    }
    // 「画像新規追加」ボタンをクリックしたときの処理
    addImgButton.addEventListener('click', function () {
      let fileInputs = imgBox.querySelectorAll('input[type="file"]');

      if (fileInputs.length < 5) {
        let imgInputWrapper = document.createElement('div');
        imgInputWrapper.classList.add('img-input-wrapper');

        // ファイル入力フィールドを作成
        let input = document.createElement('input');
        input.type = 'file';
        input.name = 'image_file';
        input.required = true;
        input.accept = '.jpg, .png, .jpeg, .gif, .svg, .ico';

        // ファイルが選択されたときに容量をチェック
        input.addEventListener('change', function () {
          const file = input.files[0]; // 選択されたファイル
          if (file) {
            const fileSizeKB = file.size / 1024; // ファイルサイズをKBに変換
            if (fileSizeKB > 80) {
              alert('画像の容量は80KB以下にしてください。選択されたファイルは ' + Math.round(fileSizeKB) + 'KB です。');
              input.value = ''; // ファイル入力をリセット
            }
          }
        });

        // 削除ボタンを作成
        let deleteButton = document.createElement('button');
        deleteButton.type = 'button';
        deleteButton.classList.add('delete-img');
        deleteButton.textContent = '削除';

        // 削除ボタンが押されたときにフィールドを削除
        deleteButton.addEventListener('click', function () {
          imgBox.removeChild(imgInputWrapper);
        });

        imgInputWrapper.appendChild(input);
        imgInputWrapper.appendChild(deleteButton);

        imgBox.appendChild(imgInputWrapper);
      } else {
        alert('画像は最大5つまでです');
      }
    });
  }

  // 「やめる」ボタンを押したときにimg-boxを隠す処理
  backButton.addEventListener('click', function (event) {
    event.preventDefault(); // リンクのデフォルト動作を防ぐ
    let imgBoxForm = document.querySelector('.img-box');

    // img-boxフォームを隠し、add-buttonを再表示
    imgBoxForm.style.display = 'none';
    document.querySelector('.add-button').style.display = 'inline-block'; // 「画像新規追加」ボタンを再表示
  });
});
