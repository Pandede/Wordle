$(document).ready(function(){
    const grid = document.querySelector(".grid");
    let pointer = [0, 0];
    console.log(pointer[0], pointer[1]);

    // console.log(grid.getAttribute("row", "col"))
    $('.keyboard').on('click', 'button', function(event) {
        $(this).parent().parent().find('button').removeClass('activate');
        $(this).addClass('activate');
        
    });

    $('.keyboard').on('click', '.btn', function(event) {
        if (pointer[1] >= 5) {
            alert("please press enter or delete!");
        } else {
            event.preventDefault();
            let letter = event.target.getAttribute("data-key");
            console.log(event.target.getAttribute("data-key"));
            $(`.gamerow[row=${pointer[0]}] .grid[col=${pointer[1]}]`).html('<p>' + letter+ '</p>'); 
            $(`.gamerow[row=${pointer[0]}] .grid[col=${pointer[1]}]`).addClass('display'); 
            pointer[1]++;
        }
    });

    $('.keyboard').on('click', '#enter', function(event) {
        event.preventDefault();
        if (pointer[1]>4){
            pointer[1] = 0;
            pointer[0]++;
        } else {
            $(`.gamerow[row=${pointer[0]}]`).addClass('animate__animated animate__headShake');
            // alert("Invalid move!");
        }
    });

    $('.keyboard').on('click', '#delete', function(event) {
        event.preventDefault();
        if (pointer[1]<=5 & pointer[1]>=0){
            pointer[1]--;
            $(`.gamerow[row=${pointer[0]}] .grid[col=${pointer[1]}] p`).remove(); 
            $(`.gamerow[row=${pointer[0]}] .grid[col=${pointer[1]}]`).removeClass('display'); 
            console.log(pointer[1]);
        } else {
            pointer[1] = 0;
        }
    });

    
});