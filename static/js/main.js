
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

      console.log("CANITDAD: "+cantidad);
      // console.log(add);
      $.ajax({
        url:'/comprar/',
        type:'GET',
        data:{'add':add,'idCompra':idCompra},
        success:(data)=>{
          $('#cart').html(data.cart);
          // console.log("SUCCESS");
        }

      });
    }else{
      alert('SOLO PUEDE COMPRAR '+auxCant[1]);

    }
  });
});

// ADD PRODUCT
const load=function () {
  let btn=$(this);
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
      console.log("SUCCESS PRODUCT");
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
        console.log(form.find('#id_imagen'));
        let product=form.find('#id_tipo').val();
        if(product==data.product){
          console.log("SEMOS IGUALES");
          $('#result').html(data.html_list);
        }else{console.log("NO SEMOS");}
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

$('#deleteSession').click((e)=>{
  $.ajax({
    url:'/deleteSession/',
    type:'GET',
    success:(data)=>{
      alert('BORRADO');
      $(location).attr('href', '/')
    }

  });
});


$('#finalizar').on('click',function(){
  let btn=$(this);
  $.ajax({
    url:btn.attr('data-url'),
    type:'GET',
    dataType:'JSON',
    success:(data)=>{
      alert("COMPRA SATISFACTORIA!");
      $(location).attr('href', '/')
    }
  });
});
