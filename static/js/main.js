
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
