function toggleOverview (evt) {
    $(this).siblings('.item_overview').toggleClass('is_visible');
}

function displayContent (evt) {

    var eventID = $(this).attr('id');
    var strat = parseInt(eventID.slice(-1));
    console.log("Monkey " + strat);

    $('.main_content').addClass('show_content');

    $.getJSON('../JavaScript/strategies.json', function (data) {
        console.log(data["explanation"][0]["heading"]);


        $('.sub_heading').text(data["explanation"][strat-1]["heading"]);
        $('.explanation').replaceWith(data['explanation'][strat-1]['info']);
    }).fail(function () {
        console.log("An error has occured.");
    });
    
}

$('.menu_item > a').mouseover(toggleOverview);
$('.menu_item > a').mouseout(toggleOverview);
$('.menu_item > a').click(displayContent)