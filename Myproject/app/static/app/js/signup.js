function validate(event){
    console.log('Form Submission')
    var error = document.getElementById('message')
    var message = null


    var values =event.target.element;
    var name =event.name.element;
    var email =event.email.element;
    var phone =event.phone.element;
    var passward =event.passward.element;
    var repassward =event.repassward.element;

    if(!name.trim()){
        message='name is Requerd.'
    }else if(!email.trim()){
        message='email is Requerd.'
    }else if(!passward.trim()){
        message='passward is Requerd.'
    }else if(passward.trim() != repassward.trim()){
        message='Passward not matched.'
    }

    if(message){
        error.innerHTML =message
        error.hidden=false
    }else{
        error.innerHTML =""
    }


    console.log({
        name,email,phone,passward,repassward
    })

    event.stopPropagation();
    return false
}



//directory form:
//    name
//    IDBCursor,contact,photo,address,designation,reporting to,
//    session management


//    conveyance form : session management