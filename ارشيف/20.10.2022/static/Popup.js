const openBtn = document.getElementById('openmodallBtn');
const closeBtn = document.getElementById('closemodallBtn');
const modall = document.getElementById('modall');

openBtn.addEventListener('click', () => {
  modall.classList.add('open');
});

closeBtn.addEventListener('click', () => {
  modall.classList.remove('open');
});