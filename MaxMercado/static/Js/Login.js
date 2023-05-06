$('#myForm').submit(function (e) {
   senha = document.querySelector('#password')
   login = document.querySelector('#login')
   
   if(senha.value == 0 || login.value == ''){
        alert('Verifique os campos e tente novamente')
        e.preventDefault();
   }
   
});

