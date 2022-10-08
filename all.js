$(document).ready(function(){
    const grid = document.querySelector(".grid");
    let pointer = [0, 0];
    console.log(pointer[0], pointer[1]);
    // console.log(grid.getAttribute("row", "col"))
    $('.keyboard').on('click', 'button', function(event) {
        event.preventDefault();
        let letter = event.target.getAttribute("data-key");
        console.log(event.target.getAttribute("data-key"));
        $('.grid').html('<p>' + letter+ '</p>'); 
    });
});