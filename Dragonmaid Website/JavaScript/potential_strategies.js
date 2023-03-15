function toggleOverview (evt) {
    $(this).siblings('.item_overview').toggleClass('is_visible');
}

function displayContent (evt) {

    var strat;
    strat = parseInt(evt.target.id);


    function buildDisplayedContent (data) {
        var element, image, heading;

        // heading = $('<h3 class="sub_heading">' + + '</h3>');
        image = $('<img src="../Resources/chamber_dragonmaid.jpg" width="300" class="left_img">');
        // el = $('<p class="explanation_text">' + + '</p>');

        data.explanation.forEach(function (entry) {
            var contentPanel;
            heading = $('<h3 class="sub_heading">' + entry.heading + '</h3>');
            contentPanel = $('section.main_content', heading);
            contentPanel.append(heading);
        });

        heading = $('<h3 class="sub_heading">' + data.explanation + '</h3>');
        data.explanation[strat-1];
    }

    $.get('ajax/api/strategies.json', function (data) {

    },JSON);
    
    $.get('ajax/api/strategies.json', function (data) {

        $container.empty();
        $container.append(buildDisplayedContent(data[strat]));
        $('section.main_content').append($container);

    }, JSON);
}

$('.menu_item > a').mouseover(toggleOverview);
$('.menu_item > a').mouseout(toggleOverview);
// $('.menu_item > a').click(displayContent)