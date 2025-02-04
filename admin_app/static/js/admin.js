let editButtonList = document.querySelectorAll('.edit-button')
let cover = document.querySelector('.cover')
let modalWindow = document.querySelector('.modal-window')
let idProduct = document.querySelector('.id-product')
let productType = document.querySelector('.type-product')
let productText = document.querySelector('.product-text')

editButtonList.forEach(function(button){
    button.addEventListener('click', function(){
        cover.style.display = 'flex'
        modalWindow.style.display = 'flex'
        idProduct.value = button.id.split('-')[1]
        productType.value = button.id.split('-')[0]
        let text = button.previousElementSibling.textContent
        productText.value = text
        modalWindow.querySelector('h1').textContent = `${productType.value}:`
    })
})
cover.addEventListener('click', function(){
    cover.style.display = 'none';
    modalWindow.style.display = 'none';
})