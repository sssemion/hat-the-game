var overlay = $(".popup-overlay");

// Регистрирует всплывающее окно по селектору кнопки (или любого другого элемента, 
// по нажатию на который, оно должно появиться) и селектору самого окна
function registerPopupWindow(triggerSelector, popupSelector) {
    $(triggerSelector).on("click", function() {
        $(popupSelector).addClass("active");
        overlay.addClass("active");
    });
}

$(".popup__close").on("click", function() {
    $(this).parent(".popup").removeClass("active");
    overlay.removeClass("active");
})