$(document).ready(function() {

  var locatorID;

  $('.voucher-barcode').each(function() {

    locatorID = $(this).find('.barcode').attr('data-id');

    $(this).find('img').JsBarcode(locatorID, {
      format: 'CODE128',
      displayValue: true,
      fontSize: 30,
      height: 50
    });

  })

  $('.personnel').each(function() {

    locatorID = $(this).find('img').attr('data-id');

    $(this).find("img").JsBarcode(locatorID, {
      format: 'CODE128',
      displayValue: true,
      fontSize: 20,
      height: 40
    });

  });

});