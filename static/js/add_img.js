document.addEventListener('DOMContentLoaded', function () {
  const addButton = document.querySelector('.add-button');
  const addImgButton = document.getElementById('add-img');
  const imgBox = document.querySelector('.img-box'); // class を取得
  const backButton = document.getElementById('yameru-button');
  const inputImg = document.getElementById('input-img');

  if (!imgBox || !inputImg) {
    console.error('エラー: .img-box または #input-img が見つかりません');
    return;
  }

  if (addButton) {
    addButton.addEventListener('click', function () {
      imgBox.style.display = 'block';
      this.style.display = 'none'; // 追加ボタンを非表示
    });
  }

  // 「フォーム追加」ボタンをクリックしたときの処理
  addImgButton.addEventListener('click', function () {
    let fileInputs = inputImg.querySelectorAll('input[type="file"]');

    if (fileInputs.length < 5) {
      let imgInputWrapper = document.createElement('div');
      imgInputWrapper.classList.add('img-input-wrapper');

      let input = document.createElement('input');
      input.type = 'file';
      input.name = 'image_files';
      input.required = true;
      input.accept = '.jpg, .png, .jpeg, .gif, .svg, .ico';

      input.addEventListener('change', function () {
        const file = input.files[0];
        if (file) {
          const fileSizeKB = file.size / 1024;
          if (fileSizeKB > 80) {
            alert(`画像の容量は80KB以下にしてください。選択されたファイルは ${Math.round(fileSizeKB)}KB です。`);
            input.value = ''; // ファイル入力をリセット
          }
        }
      });

      let deleteButton = document.createElement('button');
      deleteButton.type = 'button';
      deleteButton.classList.add('delete-img');
      deleteButton.textContent = '削除';

      deleteButton.addEventListener('click', function () {
        inputImg.removeChild(imgInputWrapper);
      });

      imgInputWrapper.appendChild(input);
      imgInputWrapper.appendChild(deleteButton);
      inputImg.appendChild(imgInputWrapper);
    } else {
      alert('画像は最大5つまでです');
    }
  });

  if (backButton) {
    backButton.addEventListener('click', function (event) {
      event.preventDefault();
      imgBox.style.display = 'none';
      if (addButton) {
        addButton.style.display = 'inline-block';
      }
    });
  } else {
    console.error('エラー: やめるボタン (#yameru-button) が見つかりません');
  }
});
