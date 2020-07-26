var overlay = $(".popup-overlay");
const animationDuration = 500;

// Регистрирует всплывающее окно по селектору кнопки (или любого другого элемента, 
// по нажатию на который, оно должно появиться) и селектору самого окна
function registerPopupWindow(triggerSelector, popupSelector) {
    $(triggerSelector).on("click", function() {
        //$(popupSelector).addClass("active");
        $(popupSelector).parent(".popup-wrapper").slideDown(animationDuration);
        overlay.fadeIn(animationDuration);
    });
}

$(".popup__close").on("click", function() {
    //$(this).parent(".popup").removeClass("active");
    $(this).parent(".popup").parent(".popup-wrapper").slideUp(animationDuration);
    overlay.fadeOut(animationDuration);
})