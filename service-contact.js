document.querySelectorAll('.copy-email').forEach(button => {
  button.addEventListener('click', async () => {
    const status = button.closest('section').querySelector('.copy-status');
    try {
      await navigator.clipboard.writeText('yuchien9489@gmail.com');
      status.textContent = '已複製信箱：yuchien9489@gmail.com';
    } catch (_) {
      status.textContent = '無法複製，請選取信箱：yuchien9489@gmail.com';
    }
  });
});
