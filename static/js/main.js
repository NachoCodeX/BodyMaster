  // $('#test').click(()=>{
  //   $("#loading").dialog('open').html("<p>Producto agotado!...</p> <i class='icon-cross loading__icon loading-err'></i>");
  // });
  $("#loading").dialog({
    autoOpen:false,
    height:120,
    show:'fadeIn',
    hide:'fadeOut',
    modal:true
  });


$("#Addloading").dialog({
  autoOpen:false,
  height:120,
  show:'fadeIn',
  hide:'fadeOut',
  modal:true,
  open:function(){
    let foo=$(this);
    setTimeout(function(){
      foo.dialog('close')
    },900);
  }
});

$('#delete_compra').on('click',()=>{
  alert('Borrado!');
});

$("body")
  .on("click", function(e) {
    // $(".ui-dialog.clickoncloseoutside:visible").find(".ui-dialog-content").dialog("close");
    let target=e.target.className
    if(target != 'btn btn--compra' && target != 'ui-dialog-content ui-widget-content' && target != 'icon-cross loading__icon loading-err'){
      // console.log("CERRADO");
      $('#loading').dialog('close');
    }
    // console.log(target);
  })

  // SELECT
  $(function () {
    $('.select').on('change',function(e) {
      let typeProduct=$(this).val(),
          nameProduct=$(this).find(':selected').text();


      console.log(typeProduct);
      console.log(nameProduct);
      $.ajax({
        url:'/result_type/',
        type:'GET',
        data:{'type':typeProduct,'name':nameProduct},
        success:(data)=>{
          $('#result').html(data.html_result);
          let totalProducts=$('#result').children().lenght;
          $('#item__total').html('Total de '+nameProduct+' '+totalProducts);
          console.log('Total de '+nameProduct+' '+totalProducts);
          console.log($('#result'));
        }

      });
  });


  // CART
  $('#result').on('click','#comprar',function(e){
      e.preventDefault();
      let add=parseInt($('.cart__count').text()) +1,
      idCompra=$(this).attr('data-url'),
      auxCant=$(this).val().split('/');

      console.log(auxCant);

      if(auxCant[0]>0){
        cantidad=auxCant[0] > 0 ? $(this).val((auxCant[0]-1)+'/'+auxCant[1]).val():0;

        $.ajax({
          url:'/comprar/',
          type:'GET',
          data:{'add':add,'idCompra':idCompra},
          success:(data)=>{
            $('#cart').html(data.cart);
            $("#Addloading").dialog('open').html("<p>Agregado!...</p> <i class='loading__icon icon-checkmark loading-suc'></i>");
          }

        });
      }else{
        // console.log("AGOTADO");
        $("#Addloading").dialog('open').html("<p>Producto agotado!...</p> <i class='icon-cross loading__icon loading-err'></i>");
      }
    });
  });

  // ADD PRODUCT
  const load=function () {
    let btn=$(this);
    console.log(btn);
    $.ajax({
      url: btn.attr('data-url'),//'/add/product',
      type:'GET',
      dataType:'JSON',
      beforeSend:(data)=>{
        $('#modal').show();
      },
      success:(data)=>{
        $('#modal').html(data.html);
        $('.close').on('click',()=>{
          $('#modal').hide();
        });
      }

    });
  };

const saveForm=function(e){
  let form=$(this);
  e.preventDefault();
  $.ajax({
    url:form.attr('action'),
    data:form.serialize(),
    type:form.attr('method'),
    dataType:'JSON',
    success:(data)=>{
      if(data.form_is_valid){
        // let product=form.find('#id_tipo').val();
        // if(product==data.product){
          // $('#result').html(data.html_list);
        // }else{
        $(location).attr('href', '/home')
        // }
        $('#modal').hide();
      }else{
        alert('NO SAVE');
      }
    }
  });

  return false;

};





  $('#addProduct').on('click',load);
  $('#modal').on('submit','#formCreate',saveForm);
  $('#result').on('click','#product_delete',load);
  $('#modal').on('submit','#formDelete',saveForm);

  $('#deleteSession').click((e)=>{
    $.ajax({
      url:'/deleteSession/',
      type:'GET',
      success:(data)=>{
        $("#loading").dialog('open').html("<p>Compra reiniciada!...</p> <i class='loading__icon icon-checkmark loading-suc'></i>");
        setTimeout(function(){
          $(location).attr('href', '/home')
        },2000);

      }

    });
  });




  $('#finalizar').on('click',function(){
    let btn=$(this);
    $.ajax({
      url:btn.attr('data-url'),
      type:'GET',
      dataType:'JSON',
      beforeSend:()=>{
        setTimeout(function(){
          $("#loading").dialog('open').html("<p>Por favor espere...</p> <i class='loading__icon loading-sp icon-spinner'></i>");
        },500);
      },
      success:(data)=>{
        $('#loading').html("<p>Compra exitosa!...</p> <i class='loading__icon icon-checkmark loading-suc'></i>");
        $(location).attr('href', '/home')
      }
    });
  });
