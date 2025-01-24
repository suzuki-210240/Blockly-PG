document.addEventListener('DOMContentLoaded', function () {
  // ユーザーメニューの処理
  const userMenu = document.getElementById('userMenu');
  if (userMenu) {
    userMenu.addEventListener('change', function (event) {
      const selectedValue = event.target.value;
      if (selectedValue !== 'username') {
        // 必要な処理を書く
      }
      event.target.value = 'username';
    });
  }

  // iframeのサイズ調整
  const iframe = document.querySelector('.preview');
  if (iframe) {
    const resizeIframe = () => {
      const aspectRatio = 16 / 9;
      iframe.style.width = window.innerWidth * 0.9 + 'px';
      iframe.style.height = (window.innerWidth * 0.9) / aspectRatio + 'px';
    };

    window.addEventListener('resize', resizeIframe);
    resizeIframe(); // 初期設定
  }

  const menuCheckbox = document.getElementById('menu');
  const container = document.querySelector('.container');
  const main = document.querySelector('main');
  const logo = document.querySelector('.logo');

  // チェックボックスの状態が変わったときの処理
  menuCheckbox.addEventListener('change', function () {
    if (!menuCheckbox.checked) {
      container.classList.add('collapsed');
      main.classList.add('collapsed-main');
      logo.classList.add('collapsed-logo');
    } else {
      container.classList.remove('collapsed');
      main.classList.remove('collapsed-main');
      logo.classList.remove('collapsed-logo');
    }
  });
});
