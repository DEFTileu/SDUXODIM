
function updateCountdowns() {
    const quotes = document.querySelectorAll('.quote');
    quotes.forEach(quote => {
        const dateStr = quote.getAttribute('data-date');
        const countdownElem = quote.querySelector('.countdown');
        const targetTime = new Date(dateStr);

        const now = new Date();
        const diff = targetTime - now;

        if (diff <= 0) {
            countdownElem.innerText = 'You are late';
            return;
        }

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((diff / (1000 * 60)) % 60);
        const seconds = Math.floor((diff / 1000) % 60);

        countdownElem.innerText = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    });
}

setInterval(updateCountdowns, 1000);

updateCountdowns();