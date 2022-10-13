$(document).ready(function(){
    // initial variables
    let pointer = [0, 0];
    let guess = [];
    const answer = ["g", "r", "e", "a", "t"]; // for testing

    // checkAnswer while press on #enter
    function checkAnswer(guess, answer) {
        for (i=0; i<answer.length; i++) {
            if (answer[i]===guess[i]){
                $(`.gamerow[row=${pointer[0]}] .grid[col=${i}]`).addClass('correct');
            } else if (answer.includes(guess[i])) {
                $(`.gamerow[row=${pointer[0]}] .grid[col=${i}]`).addClass('halfcorrect');
            } else {
                $(`.gamerow[row=${pointer[0]}] .grid[col=${i}]`).addClass('none');
            }
        }
    }

    // add keyboard style while clicked on 
    $('.keyboard').on('click', 'button', function(event) {
        $(this).parent().parent().find('button').removeClass('activate');
        $(this).addClass('activate');
    });

    // show letter in grid by keyboard value
    $('.keyboard').on('click', '.btn', function(event) {
        if (pointer[1] >= 5) {
            alert("please press enter or delete!");
        } else {
            event.preventDefault();
            let letter = event.target.getAttribute("data-key");
            $(`.gamerow[row=${pointer[0]}] .grid[col=${pointer[1]}]`).html('<p>' + letter+ '</p>'); 
            $(`.gamerow[row=${pointer[0]}] .grid[col=${pointer[1]}]`).addClass('display slide-fwd-center'); 
            pointer[1]++;
            guess.push(letter);
        }
    });

    // while click on enter -> checkAnswer, next line
    $('.keyboard').on('click', '#enter', function(event) {
        event.preventDefault();
        if (pointer[1]>4){
            checkAnswer(guess, answer);
            pointer[1] = 0;
            guess = [];
            pointer[0]++;
        } else {
            $(`.gamerow[row=${pointer[0]}]`).addClass('animate__animated animate__headShake');
            // alert("Invalid move!");
        }
    });

    // while click on delete -> remove style and text in grid
    $('.keyboard').on('click', '#delete', function(event) {
        event.preventDefault();
        if (pointer[1]<=5 & pointer[1]>=0){
            pointer[1]--;
            $(`.gamerow[row=${pointer[0]}] .grid[col=${pointer[1]}] p`).remove(); 
            $(`.gamerow[row=${pointer[0]}] .grid[col=${pointer[1]}]`).removeClass('display'); 
            guess.pop();
        } else {
            pointer[1] = 0;
        }
    });

});