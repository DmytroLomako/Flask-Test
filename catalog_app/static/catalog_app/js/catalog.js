const buttonList = document.querySelectorAll('.button-cart')

for (let i = 0; i < buttonList.length; i++) {
    buttonList[i].addEventListener('click', (event) => {
        let productId = buttonList[i].id.split('-')[1];
        if (document.cookie.includes('product')){
            let currentProducts = document.cookie.split('=')[1]
            document.cookie = `product = ${currentProducts},${productId}; path=/`
        }
        else {
            document.cookie = `product = ${productId}; path=/`
        }
    })
}