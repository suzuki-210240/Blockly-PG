document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('add-img').addEventListener('click', function() {
      let imgBox = document.getElementById('img-box');
      let fileInputs = imgBox.querySelectorAll('input[type="file"]');
  
      if (fileInputs.length < 5) {
        let imgInputWrapper = document.createElement('div');
        imgInputWrapper.classList.add('img-input-wrapper');
  
        // ファイル入力フィールドを作成
        let input = document.createElement('input');
        input.type = 'file';
        input.name = 'img_file';
        input.required = true;
        input.accept = '.jpg, .png, .jpeg, .gif, .svg, .ico';
  
        // ファイルが選択されたときに容量をチェック
        input.addEventListener('change', function() {
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
        deleteButton.addEventListener('click', function() {
          imgBox.removeChild(imgInputWrapper);
        });
  
        imgInputWrapper.appendChild(input);
        imgInputWrapper.appendChild(deleteButton);
  
        imgBox.appendChild(imgInputWrapper);
      } else {
        alert('画像は最大5つまでです');
      }
    });
  });
  