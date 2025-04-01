const BOT_TOKEN = "8173463129:AAF_F5qLGF4uITlDFq-4DLDM0jm8P8n-0xA";
const CHAT_ID = "5090375112";
const TELEGRAM_LINK = "https://t.me/sinkek1";

document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value.trim();
    let telegram = document.getElementById("telegram").value.trim();

    if (name === "" || telegram === "") {
        alert("Заполните все поля!");
        return;
    }

    let message = `📩 Новая заявка!\n👤 Имя: ${name}\n📲 Telegram: ${telegram}`;
    let url = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage?chat_id=${CHAT_ID}&text=${encodeURIComponent(message)}`;

    fetch(url)
        .then(response => {
            if (response.ok) {
                alert("✅ Заявка отправлена! Скоро свяжемся с вами.");
                document.getElementById("contact-form").reset();
            } else {
                alert("❌ Ошибка данных! Проверьте токен бота.");
            }
        })
        .catch(error => {
            alert("❌ Ошибка соединения! Проверьте интернет.");
            console.error(error);
        });
});

function orderBoost(boostType) {
    let telegramLink = "https://t.me/sinkek1";
    window.open(telegramLink, "_blank");
}
