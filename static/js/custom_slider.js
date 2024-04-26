$( function() {
    $(".numeric-slider-range").slider({
      range: true,
      min: 0,
      max: 100,
      slide: function( event, ui ) {
        $("#" + $(this).parent().attr("id") + "_min").val(ui.values[ 0 ]);
        $("#" + $(this).parent().attr("id") + "_max").val(ui.values[ 1 ]);
        $("#" + $(this).parent().attr("id") + "_text").text(ui.values[ 0 ] + ' - ' + ui.values[ 1 ]);
      },
      create: function( event, ui ) {
        $(this).slider("option",'min',$(this).parent().data("range_min"));
        $(this).slider("option",'max',$(this).parent().data("range_max"));
        $(this).slider("option",'values',[$(this).parent().data("cur_min"), $(this).parent().data("cur_max")]);
      }
    });
    $("#" + $(".numeric-slider").attr("id") + "_min").val( $(".numeric-slider").data("cur_min") );
    $("#" + $(".numeric-slider").attr("id") + "_max").val( $(".numeric-slider").data("cur_max") );
    $("#" + $(".numeric-slider").attr("id") + "_text").text(ui.values[ 0 ] + ' - ' + ui.values[ 1 ]);
  } );