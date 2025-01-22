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

  // サイドバーのメニュー開閉
  const menu = document.getElementById('menu');
  const container = document.querySelector('.container');
  const mainContent = document.querySelector('main');
  const logo = document.querySelector('.logo');

  if (menu && container) {
    menu.addEventListener('change', function () {
      // チェックボックスがチェックされたかどうかでサイドバーの状態を変更
      if (menu.checked != true) {
        container.classList.add('collapsed');
        menu.nextElementSibling.textContent = '>';

        // サイドメニューの状態に応じてmainのpaddingを変更
        if (mainContent) {
          mainContent.style.marginLeft = '50px'; // サイドメニューが縮まったときのmargin
        }

        if (logo) {
          logo.style.paddingLeft = '60px';
        }
      } else {
        container.classList.remove('collapsed');
        menu.nextElementSibling.textContent = '<'; // テキスト変更

        if (mainContent) {
          mainContent.style.marginLeft = '200px'; // 通常時のpadding
        }

        if (logo) {
          logo.style.paddingLeft = '200px';
        }
      }
    });
  }
});
