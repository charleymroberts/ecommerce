$(function(){
    $("#clear_form").on('click', function(event){
        event.preventDefault();
        $("#id_full_name").val('');
        $("#id_line_one").val('');
        $("#id_line_two").val('');
        $("#id_line_three").val('');
        $("#id_town_city_or_area").val('');
        $("#id_county").val('');
        $("#id_postcode").val('');
        $("#id_full_name").focus()
    });

    $(".address-card").on('click', function(event){
        const card=$(this)
        event.preventDefault();
        $("#id_full_name").val(card.find(".full-name").text());
        $("#id_line_one").val(card.find(".line-one").text());
        $("#id_line_two").val(card.find(".line-two").text());
        $("#id_line_three").val(card.find(".line-three").text());
        $("#id_town_city_or_area").val(card.find(".town-city-or-area").text());
        $("#id_county").val(card.find(".county").text());
        $("#id_postcode").val(card.find(".postcode").text());
        $("#id_full_name").focus()
    });

})