const tg = window.Telegram.WebApp;
tg.expand();
tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37";

let products = new Map();
let total_count = 0;
let total_price = 0.00;

const card_buttons = document.querySelectorAll(".card-btn");
const send_button = document.querySelector(".btn-send");

function card_buttons_handler(evt) {
    let card = evt.target.closest(".card");
    let card_counter = card.querySelector(".card-counter");
    let counter = card.querySelector(".card-counter > div");
    let price = card.querySelector(".card .price")
    let id = card.id.split("_")[1];

    if (evt.target.classList.contains("btn-plus")) {
        counter.innerText = Number(counter.innerText) + 1;
        total_count++;
        total_price += Number(price.innerText);
    } else if (counter.innerText > 0) {
        counter.innerText = Number(counter.innerText) - 1;
        total_count--;
        total_price -= Number(price.innerText);
    }

    if (counter.innerText > 0) {
        card_counter.classList.remove("d-none");
        products.set(id, counter.innerText);
    } else {
        card_counter.classList.add("d-none");
        products.delete(id)
    }

    if (total_count == 0) {
        send_button.classList.add("disabled");
        tg.MainButton.setText(`Total ${total_count} pc.\n${total_price.toFixed(2)} $`);
        tg.MainButton.show();
    } else {
        send_button.classList.remove("disabled");
        tg.MainButton.hide();
    }

    send_button.innerHTML = `<span>Total ${total_count} pc.</span><br>${total_price.toFixed(2)} $`;
}

card_buttons.forEach((btn) => {
    btn.addEventListener("click", card_buttons_handler);
});


Telegram.WebApp.onEvent("mainButtonClicked", () => {
    tg.sendData(JSON.stringify(Object.fromEntries(products)));
});

