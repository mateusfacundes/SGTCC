const baseUrl = 'http://127.0.0.1:8000/'

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function register(){
    var csrftoken = getCookie('csrftoken');

    var form = document.getElementById('submit');
    form.addEventListener('click', function(e){
        var nomecompleto = document.getElementById('nomecompleto').value;
        var username = document.getElementById('username').value;
        var email = document.getElementById('email').value;
        var matricula = document.getElementById('matricula').value;
        var password = document.getElementById('password1').value;
        var passwordconf = document.getElementById('password2').value;
        
        url = baseUrl+'contas/register';
        fetch(url, {
            method:'POST',
            headers:{
                'content-type': 'application/json',
                'X-CSRFtoken': csrftoken,
            },
            body:JSON.stringify({
                'username': username,
                'email': email,
                'password': password,
                'password2': passwordconf,
                'aluno': {
                    'nome': nomecompleto,
                    'matricula': matricula,
                    'curso': 1,
                    'equipe': 1,
                    'usuario': 1
                }
            })
        }).then(response => response.json())
        .then(data => {
            if (data.username == 'A user with that username already exists.'){
                alert('Usuario já existe');
            }else{
                document.cookie = 'token = token '+ data.token;
                document.cookie = 'user = '+ data.username;
                window.location.href = baseUrl+'cursos';
                           
            }
        })
    })    
}

function login(button){
    var csrftoken = getCookie('csrftoken');

    var form = document.getElementById(button);
	form.addEventListener('click', function(e){
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        url = baseUrl+'contas/login';
        fetch(url, {
            method:'POST',
            headers:{
                'content-type': 'application/json',
                'X-CSRFtoken': csrftoken,
            },
            body:JSON.stringify({
                'username': username,
                'password': password,
            })
        }).then(response => response.json())
        .then(data => {
            if(data.response == 'Falha ao logar' ){
                alert('login falhou')
            }else{
                document.cookie = 'token = token '+ data.token;
                document.cookie = 'user = '+ data.username;
                window.location.href = baseUrl+'cursos';
            }

        })
    })
}

function logout(){
    var csrftoken = getCookie('csrftoken');
	var token = getCookie('token');

    url = baseUrl+'contas/logout';
    fetch(url, {
        method: "GET",
        headers:{
            'content-type': 'application/json',
            'X-CSRFtoken': csrftoken,
            'Authorization': token
        }
      }).then(function(e){
        token = "";
        window.location.href = baseUrl;
      })
}

function carregarCursos(tabela){
    var csrftoken = getCookie('csrftoken');
	var token = getCookie('token');

    tabela = document.getElementById(tabela)

    if(token != null){
        url = baseUrl+'gerenciamento/cursos/'
        fetch(url, {
            method:'GET',
                headers:{
                    'content-type': 'application/json',
                    'X-CSRFtoken': csrftoken,
                    'Authorization': token
                }
        }).then(response => response.json())
        .then(data =>{
            if(data.detail == 'Invalid token.'){
                window.location.href = baseUrl;
            }else{
                for (var i in data){
                    var info = `
                        <tr>
                            <td>${data[i].nome}</td>
                        </tr>
                    `
                    tabela.innerHTML += info;
                }
            }
        })
    }else{
        window.location.href = baseUrl;
    }
}

