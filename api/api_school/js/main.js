method = document.querySelector('#method')

firstname = document.querySelector('#firstname')
lastname = document.querySelector('#lastname')
clas = document.querySelector('#class')
id = document.querySelector('#id')

p_firstname = document.querySelector('#p_firstname')
p_lastname = document.querySelector('#p_lastname')
p_clas = document.querySelector('#p_class')
p_id = document.querySelector('#p_id')

cbox_firstname = document.querySelector('#cbox_firstname')
cbox_lastname = document.querySelector('#cbox_lastname')
cbox_clas = document.querySelector('#cbox_class')
cbox_id = document.querySelector('#cbox_id')



function hide(){
    firstname.style.visibility = "hidden";
    p_firstname.style.visibility = "hidden";
    lastname.style.visibility = "hidden";
    p_lastname.style.visibility = "hidden";
    clas.style.visibility = "hidden";
    p_clas.style.visibility = "hidden";
    id.style.visibility = "hidden";
    p_id.style.visibility = "hidden";
    cbox_firstname.style.visibility = "hidden";
    cbox_lastname.style.visibility = "hidden";
    cbox_clas.style.visibility = "hidden";
    cbox_id.style.visibility = "hidden";
}

document.addEventListener('DOMContentLoaded', hide(), false);


function showget(){
    cbox_firstname.style.visibility = "visible";
    cbox_lastname.style.visibility = "visible";
    cbox_clas.style.visibility = "visible";
    cbox_id.style.visibility = "visible";
}

function showpost(){
    cbox_firstname.style.visibility = "visible";
    cbox_lastname.style.visibility = "visible";
    cbox_clas.style.visibility = "visible";
    cbox_id.style.visibility = "hidden";
}

function showput(){
    cbox_firstname.style.visibility = "visible";
    cbox_lastname.style.visibility = "visible";
    cbox_clas.style.visibility = "visible";
    cbox_id.style.visibility = "visible";
}

function showdel(){
    cbox_firstname.style.visibility = "hidden";
    cbox_lastname.style.visibility = "hidden";
    cbox_clas.style.visibility = "hidden";
    cbox_id.style.visibility = "visible";
}



function showhide_firstname(){
    if(cbox_firstname.checked){
    firstname.style.visibility = "visible";
    p_firstname.style.visibility = "visible";
    }
    else{
        firstname.style.visibility = "hidden";
        p_firstname.style.visibility = "hidden";
    }
}

function showhide_lastname(){
    if(cbox_lastname.checked){
        lastname.style.visibility = "visible";
        p_lastname.style.visibility = "visible";
        }
        else{
            lastname.style.visibility = "hidden";
            p_lastname.style.visibility = "hidden";
        }
}

function showhide_clas(){
    if(cbox_clas.checked){
        clas.style.visibility = "visible";
        p_clas.style.visibility = "visible";
        }
        else{
            clas.style.visibility = "hidden";
            p_clas.style.visibility = "hidden";
        }
}

function showhide_id(){
    if(cbox_id.checked){
        id.style.visibility = "visible";
        p_id.style.visibility = "visible";
        }
        else{
            id.style.visibility = "hidden";
            p_id.style.visibility = "hidden";
        }
}

function students_add() {
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://localhost:5000/students/add", headers = {'Access-Control-Allow-Origin': '*'},true);
    xhttp.send();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200) {
           document.getElementById("resultat").innerHTML = xhttp.responseText;
            }
        };
}