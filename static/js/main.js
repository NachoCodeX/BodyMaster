
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
    let add=parseInt($('.cart__count').text()) +1;
    console.log(add);
    $.ajax({
      url:'/comprar/',
      type:'GET',
      data:{'add':add},
      success:(data)=>{
        $('#cart').html(data.cart);
        console.log("SUCCESS");
      }

    });
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


const saveFormImage=function(e){
  let form=$(this),
  formData=new FormData(this);
  console.log(formData);
  // console.log($.cookie('csrftoken'));
  $.cookie('csrftoken');
  e.preventDefault();
  $.ajax({
    url:form.attr('action'),
    data:form.serialize(),
    type:form.attr('method'),
    dataType:'JSON',
    cache:false,
    contentType:false,
    processData:false,
    beforeSend:(xhr,settings)=>{
      let token=$.cookie('csrftoken');
      console.log(token);
      xhr.setRequestHeader('X-CSRFToken',token);
    },
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
$('#modal').on('submit','#formCreate',saveFormImage);
